#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CONTENT_ROOT = REPO_ROOT / "content"
LANGUAGES = {"en", "zh", "es"}
REQUIRED_FIELDS = {
    "id",
    "title",
    "slug",
    "summary",
    "seo_title",
    "seo_description",
    "seo_keywords",
    "permalink",
    "robots",
    "language",
    "article_type",
    "author_agent",
    "native_language",
    "audience",
    "theme",
    "premise",
    "source_articles",
    "related_articles",
    "fact_sources",
    "publish_to",
    "stage",
    "review_state",
    "last_updated",
}
ALLOWED_ARTICLE_TYPES = {"original", "citation", "response", "brief", "series"}
ALLOWED_STAGES = {"draft", "review", "revision", "published"}
ALLOWED_REVIEW_STATES = {"pending", "in-review", "addressed", "approved"}
FRONT_MATTER_BOUNDARY = "---"
REVIEW_TRAIL_HEADER = "## Review Trail / 审核记录"


def parse_front_matter(text: str) -> dict[str, object]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != FRONT_MATTER_BOUNDARY:
        raise ValueError("missing YAML front matter")

    try:
        end_index = lines[1:].index(FRONT_MATTER_BOUNDARY) + 1
    except ValueError as error:
        raise ValueError("unclosed YAML front matter") from error

    metadata: dict[str, object] = {}
    current_list_key: str | None = None

    for raw_line in lines[1:end_index]:
        if not raw_line.strip():
            continue

        if raw_line.startswith("  - "):
            if current_list_key is None:
                raise ValueError(f"list item without key: {raw_line}")
            metadata.setdefault(current_list_key, [])
            assert isinstance(metadata[current_list_key], list)
            metadata[current_list_key].append(raw_line[4:].strip())
            continue

        current_list_key = None

        if ":" not in raw_line:
            raise ValueError(f"invalid front matter line: {raw_line}")

        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            metadata[key] = []
            current_list_key = key
            continue

        metadata[key] = strip_quotes(value)

    return metadata


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def extract_markdown_targets(file_path: Path) -> set[str]:
    text = file_path.read_text(encoding="utf-8")
    matches = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    targets: set[str] = set()

    for raw_target in matches:
        target = raw_target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (file_path.parent / target).resolve()
        try:
            targets.add(resolved.relative_to(REPO_ROOT).as_posix())
        except ValueError:
            continue

    return targets


def article_files() -> list[Path]:
    files: list[Path] = []
    for language in LANGUAGES:
        language_root = CONTENT_ROOT / language
        for file_path in language_root.rglob("*.md"):
            if file_path.name in {"index.md", "README.md"}:
                continue
            files.append(file_path)
    return sorted(files)


def validate() -> list[str]:
    errors: list[str] = []
    article_index_targets = extract_markdown_targets(CONTENT_ROOT / "indexes" / "article-index.md")
    citation_targets = extract_markdown_targets(CONTENT_ROOT / "indexes" / "citation-map.md")
    language_index_targets = {
        language: extract_markdown_targets(CONTENT_ROOT / language / "index.md") for language in LANGUAGES
    }
    seen_ids: set[str] = set()

    for file_path in article_files():
        relative_path = file_path.relative_to(REPO_ROOT).as_posix()
        text = file_path.read_text(encoding="utf-8")

        try:
            metadata = parse_front_matter(text)
        except ValueError as error:
            errors.append(f"{relative_path}: {error}")
            continue

        missing_fields = sorted(REQUIRED_FIELDS.difference(metadata.keys()))
        if missing_fields:
            errors.append(f"{relative_path}: missing required fields: {', '.join(missing_fields)}")
            continue

        article_id = str(metadata["id"])
        if article_id in seen_ids:
            errors.append(f"{relative_path}: duplicate article id {article_id}")
        seen_ids.add(article_id)

        language = str(metadata["language"])
        if language not in LANGUAGES:
            errors.append(f"{relative_path}: unsupported language {language}")
        else:
            parent_language = file_path.relative_to(CONTENT_ROOT).parts[0]
            if parent_language != language:
                errors.append(
                    f"{relative_path}: language field {language} does not match directory {parent_language}"
                )

        article_type = str(metadata["article_type"])
        if article_type not in ALLOWED_ARTICLE_TYPES:
            errors.append(f"{relative_path}: invalid article_type {article_type}")

        stage = str(metadata["stage"])
        if stage not in ALLOWED_STAGES:
            errors.append(f"{relative_path}: invalid stage {stage}")

        review_state = str(metadata["review_state"])
        if review_state not in ALLOWED_REVIEW_STATES:
            errors.append(f"{relative_path}: invalid review_state {review_state}")

        permalink = str(metadata["permalink"])
        if language in LANGUAGES and not permalink.startswith(f"/{language}/"):
            errors.append(f"{relative_path}: permalink should start with /{language}/")

        publish_to = metadata["publish_to"]
        if not isinstance(publish_to, list) or "github-pages" not in publish_to:
            errors.append(f"{relative_path}: publish_to must include github-pages")

        source_articles = metadata["source_articles"]
        if not isinstance(source_articles, list):
            errors.append(f"{relative_path}: source_articles must be a list")
            source_articles = []

        if article_type in {"citation", "response"} and not source_articles:
            errors.append(f"{relative_path}: {article_type} article must include source_articles")

        if REVIEW_TRAIL_HEADER not in text:
            errors.append(f"{relative_path}: missing '{REVIEW_TRAIL_HEADER}' section")

        if relative_path not in article_index_targets:
            errors.append(f"{relative_path}: not registered in content/indexes/article-index.md")

        if language in LANGUAGES and relative_path not in language_index_targets[language]:
            errors.append(f"{relative_path}: not registered in content/{language}/index.md")

        if source_articles and relative_path not in citation_targets:
            errors.append(f"{relative_path}: citation/response article not registered in content/indexes/citation-map.md")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Content validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
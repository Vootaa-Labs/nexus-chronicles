# Article Schema

## Purpose / 目标

Every article needs a shared metadata header so it can be rendered by GitHub Pages, indexed, searched, cited, and updated through multiple editorial stages.

每篇文章都需要具备统一的头部元数据，以便被 GitHub Pages 渲染、被索引、被检索、被引用，并支持多阶段编辑更新。

## Required Fields / 必填字段

```yaml
---
id: chronicle-0001
title: Sample Title
slug: sample-title
summary: One-paragraph summary.
seo_title: Sample Title
seo_description: One-sentence search description.
seo_keywords:
   - nexus
   - architecture
permalink: /en/sample-title/
robots: index,follow
language: zh
article_type: original
author_agent: octopus-architect
native_language: zh
audience: developers
theme: execution-architecture
premise: One-sentence thesis.
source_articles: []
related_articles: []
fact_sources:
   - nexus-node
publish_to:
  - github-pages
stage: draft
review_state: pending
last_updated: 2026-03-27
---
```

## Field Notes / 字段说明

1. `id`
   仓库内唯一文章编号，后续引用关系依赖此字段。

2. `slug`
   URL-friendly slug used for pages and internal references.
   页面 URL 和内部引用使用的 slug。

3. `summary`
   Short summary for cards, feeds, and index pages.
   用于卡片、列表和索引页的短摘要。

4. `seo_title` / `seo_description` / `seo_keywords`
   Search-facing metadata for GitHub Pages and external sharing.
   用于 GitHub Pages 和外部分享的搜索元信息。

5. `permalink`
   Preferred page path for GitHub Pages.
   GitHub Pages 优先使用的页面路径。

6. `language`
   使用 ISO 639-1 语言代码，例如 `zh`、`en`、`es`。

7. `article_type`
   推荐值：`original`、`citation`、`response`、`brief`、`series`。

8. `author_agent`
   对应 `factory/personas/` 中的作者卡标识。

9. `source_articles`
   用于列出所引用的上游文章 ID。原创文章保持空数组。

10. `publish_to`
   记录目标发布渠道，例如 `github-pages`、`medium`、`newsletter`。

11. `stage`
    Recommended values: `draft`, `review`, `revision`, `published`.
    推荐值：`draft`、`review`、`revision`、`published`。

12. `review_state`
    Recommended values: `pending`, `in-review`, `addressed`, `approved`.
    推荐值：`pending`、`in-review`、`addressed`、`approved`。

## Minimum Quality / 最低质量要求

1. 必须有一句可验证的中心论点。
2. 必须明确写给谁。
3. 必须能判断是原创、引用还是回应。
4. 必须能从元数据看出它和其他文章的关系。
5. 正式稿件必须在文末保留 `Review Trail / 审核记录` 区块。
6. 正式稿件必须被 `content/indexes/article-index.md` 收录，并出现在对应语言分区索引中。
7. 如果是引用或回应文章，还应在 `content/indexes/citation-map.md` 中留下可追踪关系。
8. 在结束前，Agent 应确保本地验证脚本 `.github/scripts/validate_content.py` 可以通过。
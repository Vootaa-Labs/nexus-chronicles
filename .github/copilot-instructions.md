# Project Guidelines

## Scope

This repository is a shared Vootaa-Labs editorial system, not a personal workspace and not a software monorepo.

Read `.github/README.md` first when entering the repository as an AI agent.

## Structure

1. `content/` stores published or draft articles.
2. `factory/` stores workflows, standards, review rules, templates, and author personas.
3. `.github/agents/` stores GitHub Copilot custom agents.
4. `.github/prompts/` stores user-invocable prompts for drafting and review.
5. `factory/topic-board/topic-pool.md` stores candidate topics and board states.
6. `.github/README.md` is the agent entry guide and read order summary.

## Writing Conventions

1. Repository-facing instructions and shared workflow documents should be written in English or bilingual English/Chinese.
2. AI-agent-facing prompts and instructions should be written in English.
3. Treat repository readers and article audiences as different groups.
4. Treat multilingual content as native-language authorship plus citation chains, not direct translation.
5. Keep author persona, target audience, and article type explicit in metadata.
6. Prefer small, focused edits and preserve established terminology once chosen.
7. When creating new language zones, use ISO 639-1 folder names under `content/`.
8. If the article makes technical claims about Nexus, prefer evidence from `nexus-node` and `nexus-move` before asserting implementation details.
9. If the user gives only a rough direction, infer intent first and narrow the topic before drafting.
10. If the user gives no direction at all, discover a candidate topic from the topic pool, language gaps, and code-backed theme gaps.
11. Personal local materials may be read only when the contributor explicitly requests it; do not commit local-only paths, notes, or assumptions into the shared repository.
12. Keep the public site surface reader-facing: topic boards belong to `factory/`, while public navigation pages belong to `content/indexes/`.
13. Before considering an article task complete, make sure it would pass `.github/scripts/validate_content.py`, including index registration requirements.
14. Before making a git commit that includes article work, run `.github/scripts/validate_content.py` locally and resolve failures first.
15. Before changing an article to `stage: published`, run `.github/scripts/validate_content.py` locally and do not publish if it fails.
16. Prefer `make validate-content` as the standard local validation command when available.

## Agent Usage

1. Use `GPT`-oriented agents for drafting and structure.
2. Use `Claude`-oriented agents for critique, coherence, and weak-argument detection.
3. Use `Gemini`-oriented agents for topic scouting, comparison, and relationship discovery.
4. Default to the current GitHub Copilot model setting unless the user explicitly wants a manual model split between drafting and review.
5. Allow drafting agents enough autonomy to choose a sharper topic, article form, and evidence path, as long as they stay within the user's requested direction.
6. In no-direction mode, prefer ready candidate topics and language-gap citation opportunities before inventing new topics.

## Boundaries

1. Do not flatten different language articles into one canonical translation set.
2. Do not create articles without a clear audience and thesis.
3. Do not mix factory rules with published content.
4. Do not present technical guesses as verified Nexus facts.
5. Do not drift so far from the user's direction that the resulting article solves a different problem.
6. Do not treat a contributor's personal workspace files as shared repository sources unless they also exist in shared or public locations.
7. Keep the top-level repository model simple: `content/` for output, `factory/` for production, `.github/` for AI agent entry.
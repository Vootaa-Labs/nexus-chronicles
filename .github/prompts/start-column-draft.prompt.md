---
name: Start Column Draft
description: "Use when starting a new column draft for nexus-chronicles with a topic, persona, language, and optional source materials. Keywords: draft article, start article, first draft, write column, new chronicle."
agent: "agent"
argument-hint: "Topic, target audience, language, author persona, article type, and optional sources."
---
Create a first draft for nexus-chronicles.

Requirements:

1. Treat English instructions as the default operating mode for this shared repository.
2. Treat the user's message as a direction, not always as a fully formed topic.
3. Infer or confirm the user's real intent, target audience, language, article type, and author persona from the instruction.
4. Before drafting, perform a short internal topic-selection step guided by `factory/workflows/topic-selection.md` and `factory/templates/editorial-brief-template.md`.
5. If the user selected a custom drafting agent manually, preserve that role choice.
6. Use the repository factory rules, current article structure, and existing content zones.
7. If the user gave no concrete direction, discover a candidate topic from `factory/topic-board/topic-pool.md`, the public content indexes, and the language indexes.
8. Treat multilingual output as native-language authorship, not translation.
9. If the topic involves Nexus implementation details, prefer code evidence from `nexus-node` and `nexus-move` before making technical claims.
10. If the user explicitly provides personal local materials, treat them as private background only and do not turn local-only paths or claims into shared repository facts.
11. Only start drafting after the topic is narrowed enough to satisfy audience, thesis, evidence, and persona constraints.
12. Output using the repository article metadata format.
13. Before finishing, ensure the draft would pass `.github/scripts/validate_content.py`, including article-index and language-index registration.
14. If the work is going to be committed, require a local run of `.github/scripts/validate_content.py` before commit.
15. Do not set `stage: published` unless the local validation script passes.

If the user provided source material, incorporate it explicitly.
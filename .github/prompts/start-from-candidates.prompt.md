---
name: Start From Candidates
description: "Use when the user does not provide a specific direction and wants the agent to choose a suitable candidate topic from the repository topic pool and start drafting. Keywords: choose topic and start, candidate topic, no direction, topic pool, start from board."
agent: "agent"
argument-hint: "Optional language, persona, audience, or source constraints."
---
Start a nexus-chronicles draft from the repository's candidate topics.

Requirements:

1. Treat English instructions as the default operating mode for this shared repository.
2. Read `factory/topic-board/topic-pool.md`, the public content indexes, and the language indexes before choosing a topic.
3. If the user gave no direction, select a topic using the scoring and board rules in `factory/workflows/topic-board-mechanism.md` and `factory/standards/topic-scoring.md`.
4. Prefer `ready` topics, then promote the strongest `watching` topic if needed.
5. If a language gap exists for a strong upstream article, that citation opportunity should be considered first.
6. If the user explicitly provides personal local materials, treat them as private background only and do not convert them into shared repository references.
7. Produce a short internal brief, then start the draft.
8. Output using the article metadata format.
9. Before finishing, ensure the resulting draft would pass `.github/scripts/validate_content.py`, including article-index and language-index registration.
10. If the work is going to be committed, require a local run of `.github/scripts/validate_content.py` before commit.
11. Do not set `stage: published` unless the local validation script passes.

If the user provides any constraints such as language or persona, honor them while choosing the candidate topic.
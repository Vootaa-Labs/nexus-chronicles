---
name: Run Column Review
description: "Use when entering the review stage for a draft in nexus-chronicles. Keywords: review draft, editorial review, audit article, critique article, reviewer notes."
agent: "agent"
argument-hint: "Draft path, reviewer persona, review language, and what to focus on."
---
Review the target draft for nexus-chronicles.

Requirements:

1. Treat English instructions as the default operating mode for this shared repository.
2. Produce a short review note using the repository review unit format.
3. If the user selected a custom reviewer agent or manually switched models, preserve that review setup.
4. Check thesis clarity, evidence quality, persona consistency, and empty narrative.
5. If the article makes technical claims about Nexus, call out missing or weak code evidence.
6. Prefer a reviewer persona different from the drafting persona.
7. Append the review note to the manuscript tail under `Review Trail / 审核记录` when the user wants the review carried on the same draft.
8. Keep the review actionable and specific.
9. If the review leads to a publishable revision, ensure the revised manuscript would pass `.github/scripts/validate_content.py` before marking the work complete.
10. Do not approve a change to `stage: published` unless the local validation script has been run successfully.
11. If the user plans to commit the reviewed manuscript, require a local validation run before commit.

If the user asks for a revised draft after the review, propose targeted revisions instead of rewriting the entire article by default.
# Project Guidelines

## Scope

This repository is a multilingual content system, not a software monorepo.

## Structure

1. `playbook/` stores workflows and standards.
2. `content/` stores published or draft articles.
3. `agents/` stores author personas.
4. `.github/agents/` stores GitHub Copilot custom agents.

## Writing Conventions

1. Treat multilingual content as native-language authorship plus citation chains, not direct translation.
2. Keep author persona, target audience, and article type explicit in metadata.
3. Prefer small, focused edits and preserve established terminology once chosen.
4. When creating new language zones, use ISO 639-1 folder names under `content/`.

## Agent Usage

1. Use `GPT`-oriented agents for drafting and structure.
2. Use `Claude`-oriented agents for critique, coherence, and weak-argument detection.
3. Use `Gemini`-oriented agents for topic scouting, comparison, and relationship discovery.

## Boundaries

1. Do not flatten different language articles into one canonical translation set.
2. Do not create articles without a clear audience and thesis.
3. Do not mix playbook rules with published content.
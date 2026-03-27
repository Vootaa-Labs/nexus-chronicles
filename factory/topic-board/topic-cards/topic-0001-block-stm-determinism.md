# topic-0001 Block-STM Determinism

```yaml
topic_id: topic-0001
status: ready
desk: architecture
language_priority:
  - en
  - zh
topic_type: original
proposed_title: Why Parallel Execution Is Worth the Verification Cost
theme: execution-architecture
candidate_personas:
  - octopus-architect
  - orca-auditor
target_audience:
  - developers
  - performance-engineers
  - formal-verification-researchers
primary_sources:
  - nexus-node/crates/nexus-execution
secondary_sources:
  - nexus-node/README.md
  - Vootaa-Labs/nexus-move
upstream_articles: []
signals:
  - code-hotspot
  - verification-gap
scores:
  reader_value: 5
  evidence_strength: 4
  persona_fit: 5
  citation_potential: 4
  novelty: 4
```

## Why This Topic

Block-STM is one of the few themes that can make Nexus look technically distinctive without relying on slogans.

## Writing Angle

Explain why parallel execution is not just a performance claim but a verification burden, and why Nexus has to make that burden legible.

## Risks

Do not imply verification is already complete if the evidence is still partial.
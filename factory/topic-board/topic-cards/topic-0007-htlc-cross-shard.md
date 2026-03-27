# topic-0007 HTLC Cross Shard Coordination

```yaml
topic_id: topic-0007
status: watching
desk: execution
language_priority:
  - en
  - zh
topic_type: original
proposed_title: Atomicity Without Global Locks
theme: execution-architecture
candidate_personas:
  - octopus-architect
  - nautilus-researcher
target_audience:
  - distributed-systems-engineers
  - contract-auditors
  - app-developers
primary_sources:
  - nexus-node/crates/nexus-execution
secondary_sources:
  - nexus-node/README.md
  - Vootaa-Labs/nexus-move
upstream_articles: []
signals:
  - execution-gap
  - cross-shard-mechanics
scores:
  reader_value: 4
  evidence_strength: 3
  persona_fit: 5
  citation_potential: 4
  novelty: 5
```

## Why This Topic

Cross-shard coordination is one of the hardest things to explain clearly, which is exactly why it deserves a card.

## Writing Angle

Make the article about how to preserve atomicity without hiding complexity under vague protocol language.

## Risks

This article can become hand-wavy very quickly if the exact flow is not grounded in evidence.
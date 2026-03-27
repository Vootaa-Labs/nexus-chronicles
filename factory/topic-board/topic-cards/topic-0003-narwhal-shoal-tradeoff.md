# topic-0003 Narwhal Shoal Tradeoff

```yaml
topic_id: topic-0003
status: ready
desk: consensus
language_priority:
  - en
  - zh
topic_type: original
proposed_title: Why Nexus Uses Narwhal and Shoal Instead of Pretending One Consensus Layer Solves Everything
theme: consensus-design
candidate_personas:
  - octopus-architect
  - orca-auditor
target_audience:
  - protocol-researchers
  - validator-operators
  - security-reviewers
primary_sources:
  - nexus-node/crates/nexus-consensus
secondary_sources:
  - nexus-node/README.md
  - Vootaa-Labs/nexus-move
upstream_articles: []
signals:
  - consensus-gap
  - verification-gap
scores:
  reader_value: 5
  evidence_strength: 4
  persona_fit: 5
  citation_potential: 5
  novelty: 5
```

## Why This Topic

Consensus essays are often vague. This one can be concrete and strategic at the same time.

## Writing Angle

Explain the separation of throughput and finality concerns, then confront the formal verification pressure honestly.

## Risks

Do not flatten Narwhal and Shoal into buzzwords with no operational implications.
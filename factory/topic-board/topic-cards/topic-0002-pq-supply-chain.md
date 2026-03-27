# topic-0002 PQ Supply Chain

```yaml
topic_id: topic-0002
status: ready
desk: crypto
language_priority:
  - en
  - zh
  - es
topic_type: original
proposed_title: Eliminating the C Attack Surface in Post-Quantum Crypto
theme: crypto-engineering
candidate_personas:
  - dolphin-explainer
  - orca-auditor
target_audience:
  - security-engineers
  - devsecops
  - general-technical-readers
primary_sources:
  - nexus-node/crates/nexus-crypto/Cargo.toml
secondary_sources:
  - nexus-node/README.md
  - Vootaa-Labs/nexus-move
upstream_articles: []
signals:
  - crypto-migration
  - supply-chain-risk
scores:
  reader_value: 5
  evidence_strength: 5
  persona_fit: 5
  citation_potential: 5
  novelty: 4
```

## Why This Topic

This is concrete, understandable, security-relevant, and easy to reuse across languages.

## Writing Angle

Treat the migration as a supply-chain and engineering-trust story, not just a dependency update.

## Risks

Avoid turning it into a generic Rust-good C-bad article.
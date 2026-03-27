# Topic Pool

## Purpose / 说明

This is the internal topic board for editorial planning and no-direction drafting.

这是仓库级选题池与选题看板的结合入口。

当用户不给定方向时，Agent 应优先从这里和公开内容索引中挑选合适主题，再进入起稿流程。

## Editorial Desk Snapshot

- Total tracked topics: 16
- Ready to commission: 13
- Watching for more evidence or timing: 3
- Citation opportunities: 0
- Highest cross-language potential: `topic-0002`, `topic-0005`, `topic-0006`, `topic-0008`, `topic-0011`, `topic-0013`, `topic-0015`, `topic-0016`

## Column Families / 专栏家族

### Industry Observation / 行业观察专栏

Track the shifting context around blockchains, AI systems, and agent ecosystems.

跟踪区块链、人工智能系统与智能体生态之间正在变化的行业环境。

Priority angles:

1. blockchain industry structure and protocol positioning
2. AI infrastructure and agent-control-plane shifts
3. where on-chain systems intersect with AI-native products

### Technical Explainers / 技术科普专栏

Turn hard systems topics into readable essays without surrendering precision.

把高门槛系统主题写成可读文章，同时保持技术精度。

Priority angles:

1. Rust and Haskell
2. formal verification
3. post-quantum cryptography
4. consensus mechanisms, including PoW and PoS
5. sharding
6. parallel architecture

## Commissioning Now

| Topic ID | Desk | Priority Languages | Persona | Why Now |
|---|---|---|---|---|
| [topic-0001](./topic-cards/topic-0001-block-stm-determinism.md) | Architecture | en, zh | octopus-architect | Parallel execution is a strong differentiator and needs a code-backed explanation |
| [topic-0002](./topic-cards/topic-0002-pq-supply-chain.md) | Crypto | en, zh, es | dolphin-explainer | Pure Rust PQ migration is concrete, timely, and broadly understandable |
| [topic-0003](./topic-cards/topic-0003-narwhal-shoal-tradeoff.md) | Consensus | en, zh | octopus-architect, orca-auditor | Consensus design plus formal verification gap makes this strategically important |
| [topic-0005](./topic-cards/topic-0005-formal-evidence-surfaces.md) | Audit | en, zh, es | orca-auditor | Proof claims need an auditable evidence narrative before public scaling |
| [topic-0006](./topic-cards/topic-0006-pq-p2p-handshake.md) | Network | en, zh, es | orca-auditor | Post-quantum networking is both concrete and externally legible |
| [topic-0008](./topic-cards/topic-0008-evidence-driven-narrative.md) | Narrative | en, zh, es | manta-observer | This is the editorial philosophy of the whole repository |
| [topic-0010](./topic-cards/topic-0010-validator-hardware.md) | Operations | en, zh | manta-observer | Validator operators need practical expectations, not abstract TPS claims |
| [topic-0011](./topic-cards/topic-0011-ai-agents-blockchain-industry.md) | Industry | en, zh, es | manta-observer, swordfish-critic | Blockchain, AI, and agent infrastructure are colliding into one public narrative surface |
| [topic-0012](./topic-cards/topic-0012-rust-vs-haskell-verifiable-systems.md) | Technical Explainers | en, zh | nautilus-researcher, dolphin-explainer | Readers need a serious but readable comparison of language tradeoffs for verifiable systems |
| [topic-0013](./topic-cards/topic-0013-formal-verification-practical-guide.md) | Technical Explainers | en, zh, es | orca-auditor, nautilus-researcher | Formal verification has strong signaling power but weak public understanding |
| [topic-0014](./topic-cards/topic-0014-post-quantum-crypto-for-builders.md) | Technical Explainers | en, zh, es | dolphin-explainer, orca-auditor | Post-quantum crypto is moving from abstract concern to builder-facing design pressure |
| [topic-0015](./topic-cards/topic-0015-consensus-pow-pos-tradeoffs.md) | Technical Explainers | en, zh, es | dolphin-explainer, manta-observer | Readers still confuse labels like PoW and PoS with actual system tradeoffs |
| [topic-0016](./topic-cards/topic-0016-sharding-parallel-architecture.md) | Technical Explainers | en, zh, es | octopus-architect, dolphin-explainer | Sharding and parallel architecture remain central but widely misunderstood scaling stories |

## Watching Desk

| Topic ID | Desk | Suggested Trigger | Why Not Ready Yet |
|---|---|---|---|
| [topic-0004](./topic-cards/topic-0004-move-shard-boundaries.md) | Move | More concrete deployment examples | Strong topic, but benefits from at least one end-to-end developer walkthrough |
| [topic-0007](./topic-cards/topic-0007-htlc-cross-shard.md) | Execution | More explicit code references during drafting | Valuable, but needs careful explanation to avoid overclaiming mechanics |
| [topic-0009](./topic-cards/topic-0009-intent-first-rpc.md) | Developer Tools | More API surface evidence | Good builder-facing topic, but current evidence should be tightened during drafting |

## Citation Expansion Lane

当前仓库还没有正式发布文章，因此这一列暂时为空。

后续一旦某个语言区出现原创文章，就应新增对应的 `needs-citation` 卡，优先推动：

1. 英文原创 -> 中文引用解读
2. 英文原创 -> 西班牙语引用解读
3. 中文原创 -> 英文回应或对照文章

## Research Backlog

| Topic ID | Desk | Why It Stays In Backlog |
|---|---|---|
| [topic-0001](./topic-cards/topic-0001-block-stm-determinism.md) | Architecture | High value, but better if paired with formal verification progress |
| [topic-0003](./topic-cards/topic-0003-narwhal-shoal-tradeoff.md) | Consensus | Excellent flagship essay, but should be written carefully to avoid vague consensus writing |

## Candidate Board

| Topic ID | Status | Type | Priority Languages | Suggested Persona | Signal | Why It Matters |
|---|---|---|---|---|---|---|
| [topic-0001](./topic-cards/topic-0001-block-stm-determinism.md) | ready | original | en, zh | octopus-architect | code-hotspot | Block-STM determinism is a flagship technical theme that deserves evidence-backed treatment |
| [topic-0002](./topic-cards/topic-0002-pq-supply-chain.md) | ready | original | en, zh, es | dolphin-explainer | crypto-migration | Pure Rust PQ migration is concrete, technical, and easy to cite across languages |
| [topic-0003](./topic-cards/topic-0003-narwhal-shoal-tradeoff.md) | ready | original | en, zh | octopus-architect, orca-auditor | consensus-gap | Narwhal plus Shoal++ is a strong design story with real verification pressure |
| [topic-0004](./topic-cards/topic-0004-move-shard-boundaries.md) | watching | original | en, zh | dolphin-explainer | developer-gap | Move-in-sharded-execution needs a developer-facing explanation |
| [topic-0005](./topic-cards/topic-0005-formal-evidence-surfaces.md) | ready | original | en, zh, es | orca-auditor | audit-surface | Formal claims need auditable evidence artifacts and a public explanation |
| [topic-0006](./topic-cards/topic-0006-pq-p2p-handshake.md) | ready | original | en, zh, es | orca-auditor | network-security | PQ handshakes are both a real differentiator and a strong security narrative |
| [topic-0007](./topic-cards/topic-0007-htlc-cross-shard.md) | watching | original | en, zh | octopus-architect | execution-gap | Cross-shard HTLC mechanics are important but need careful grounding |
| [topic-0008](./topic-cards/topic-0008-evidence-driven-narrative.md) | ready | original | en, zh, es | manta-observer | narrative-strategy | Evidence-driven storytelling can become the editorial signature of Nexus |
| [topic-0009](./topic-cards/topic-0009-intent-first-rpc.md) | watching | original | en, zh | dolphin-explainer | builder-gap | RPC and intent design are useful, but the article should avoid vague API promises |
| [topic-0010](./topic-cards/topic-0010-validator-hardware.md) | ready | original | en, zh | manta-observer | operations-gap | Validator hardware guidance translates protocol ambition into operational reality |
| [topic-0011](./topic-cards/topic-0011-ai-agents-blockchain-industry.md) | ready | original | en, zh, es | manta-observer, swordfish-critic | industry-convergence | AI agents, control planes, and blockchains are starting to overlap in public narratives and product design |
| [topic-0012](./topic-cards/topic-0012-rust-vs-haskell-verifiable-systems.md) | ready | original | en, zh | nautilus-researcher, dolphin-explainer | language-tradeoff | Rust and Haskell make a strong explainer pair for verifiable systems thinking |
| [topic-0013](./topic-cards/topic-0013-formal-verification-practical-guide.md) | ready | original | en, zh, es | orca-auditor, nautilus-researcher | verification-education | Formal verification needs a practical public explanation, not just prestige signaling |
| [topic-0014](./topic-cards/topic-0014-post-quantum-crypto-for-builders.md) | ready | original | en, zh, es | dolphin-explainer, orca-auditor | pq-builder-education | Builder audiences need a plain-language bridge into post-quantum system design |
| [topic-0015](./topic-cards/topic-0015-consensus-pow-pos-tradeoffs.md) | ready | original | en, zh, es | dolphin-explainer, manta-observer | consensus-education | PoW, PoS, and other consensus labels are widely cited but poorly distinguished |
| [topic-0016](./topic-cards/topic-0016-sharding-parallel-architecture.md) | ready | original | en, zh, es | octopus-architect, dolphin-explainer | scaling-education | Sharding and parallel architecture are still the core scaling story most readers only partially understand |

## Discovery Rules

Agent should add or promote topics here when it sees one of these patterns:

1. An original article exists in one language but no citation article exists in another language.
2. A code-heavy theme exists in `nexus-node` or `nexus-move` but has no dedicated article.
3. A recurring misconception or narrative gap appears across drafts.
4. A topic fits a strong persona and has clear reader value.

## No-Direction Mode

当用户只说“从候选主题中挑选合适的主题，并开始即可”时，Agent 应：

1. 优先读取本文件
2. 结合当前语言区和现有文章缺口筛选主题
3. 优先选择 `ready` 状态主题
4. 若没有 `ready` 主题，再从 `watching` 中提升一个最强候选题

## Notes

当前仓库尚无正式文章，因此 `language-gap` 类型主题先以占位形式存在。
当英文原创文章出现后，应把对应跨语言引用机会回填到本池中。

具体写作角度、读者、证据路径和风险，请进入各主题卡查看。
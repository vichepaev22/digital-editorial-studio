# Digital Editorial Studio

Reusable Agent Skill for creating and auditing interactive digital research publications. Inspired by [Beyond Language / ITMO LLM atlas](https://vichepaev22.github.io/continuum-motion-atlas/itmo-llm-2026/), not affiliated with ITMO.

## Use
Clone or download the repository. Copy the skill directory (including SKILL.md, references, assets, scripts and examples) into the skills location supported by your agent; name the directory digital-editorial-studio. If automatic discovery is unavailable, attach SKILL.md and referenced materials and explicitly ask your agent to apply them. Installation paths and supported runtimes differ by client.

Example: “Apply Digital Editorial Studio to this research PDF. Create a source-grounded interactive edition, test the primary reader journeys and report what could not be verified.”

## Contents
- [SKILL.md](SKILL.md): workflow and activation criteria.
- [Editorial methodology](references/editorial.md), [design](references/design.md), [engineering](references/engineering.md), [acceptance](references/acceptance.md).
- [Project brief](assets/brief.md), [ITMO example](examples/itmo.md).
- [Production playbook](references/production-playbook.md): create, audit, and revise modes.
- [Claim ledger](assets/claim-ledger.csv), [QA register](assets/qa-register.csv), and [HTML starter](assets/edition-starter.html).
- [Seven evaluation cases](examples/evaluation-cases.md): a proposed controlled evaluation, not completed cross-agent tests.
- Static smoke check: python3 scripts/check_edition.py path/to/index.html (standard library only).

This is version 0.2.0, a published operational skill, not a certified accessibility tool or a guarantee of deployment. Live evaluation and cross-agent testing remain necessary. The MIT license applies to original material in this repository; third-party sources and images retain their own terms.

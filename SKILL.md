---
name: digital-editorial-studio
description: Create, audit, or upgrade an interactive digital magazine, research atlas, evidence-based web publication, or scrollytelling edition from a PDF, report, dataset, or existing site. Use for source-grounded editorial storytelling, accessible interactions, data visualization, visual art direction, and verified web deployment.
license: MIT
compatibility: Works with agents supporting local files; browser, network and Git are optional for local drafting but required for corresponding live verification.
metadata:
  version: "0.2.0"
---
# Digital Editorial Studio

Transform complex source material into a credible, readable, distinctive, interactive web edition. Preserve the author's meaning, distinguish interpretation and measured evidence, and ship a tested artifact rather than a decorative mockup.

## Modes and activation
Use for creating, revising, or auditing report-derived digital publications. Do not activate for a plain summary, unrelated landing page, or routine social post unless the user explicitly asks for the publication workflow. See [production playbook](references/production-playbook.md).

## Operating procedure
1. Discover the reader, task, source edition, language, target devices, publishing permissions, and acceptance criteria. Use adaptive depth; state assumptions and competing hypotheses. For a revision, inventory current capabilities and keep a baseline commit.
2. Read the source in full when feasible, including figures and footnotes. Build a claim ledger with exact page/section, units, date, uncertainty, and status. Check primary sources for material claims; preserve contradictions and avoid inventing evidence. See [editorial method](references/editorial.md).
3. Design the story: one clear thesis, executive reading route, thematic chapters, contextual visualizations, glossary and transparent source notes. Choose interactions that answer real reader questions, with static alternatives.
4. Establish art direction from the topic rather than copying the reference project. Use a distinctive cover, typography, restrained palette, consistent image language, responsive grids, and purposeful editorial rhythm. See [design system](references/design.md).
5. Implement a working edition. Prefer semantic HTML and progressive enhancement; use a framework only when the problem requires it. Localize critical assets when rights permit. Keep secrets out of client code. Clearly label simulated, qualitative and illustrative content. See [engineering and QA](references/engineering.md).
6. Validate before publishing: source traceability, keyboard and screen reader behavior, mobile and desktop, interactions, external links, local storage resilience, privacy, performance, and regression checks. Report each as passed, failed or not run. Run the included static checker; it does not prove accessibility or truth.
7. Publish only to the authorized destination, use a review branch for existing production work, verify deployment independently, document rollback and limits. If tools are missing, deliver an honest local artifact, never invent a commit or test result.
8. Evaluate effectiveness with reading-comprehension tasks and consent-respecting aggregate events, not clicks alone. For substantial projects compare alternatives and prioritize changes by impact, confidence and effort.

## Output contract
Deliver a source-grounded edition, source ledger, design decisions, verification evidence, limitations and a reproducible handoff. A public URL is a success only after deployment is verified. Use [acceptance checklist](references/acceptance.md) and [brief template](assets/brief.md). See [ITMO case](examples/itmo.md) for the reference project. Do not make its palette or Android motif mandatory for other subjects.

## Reusable resources
- [Claim ledger](assets/claim-ledger.csv) and [QA register](assets/qa-register.csv): fill with real evidence.
- [Semantic starter](assets/edition-starter.html): use only as scaffold; replace all placeholders and design a topic-specific identity.
- [Evaluation cases](examples/evaluation-cases.md): run comparative evaluations before claiming general quality gains.

## Tool selection
Use available PDF extraction and page rendering; source search and manual verification; browser DevTools/Playwright and axe-core; Lighthouse for lab performance and field data only when available; Git and CI for traceability. Use image tools only for editorial images requested or justified in the edition. Verify actual capabilities first; never claim tools ran when they did not.

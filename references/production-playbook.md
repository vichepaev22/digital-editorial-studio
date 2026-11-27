# Production playbook — three operating modes

## Create
1. Freeze source edition, rights and audience. Build evidence ledger before authoring numbers.
2. Map readers' jobs: orient in 60 seconds, understand in 5 minutes, inspect evidence in depth.
3. Outline chapters and choose the smallest interaction that answers each reader question. A filter is useful only if it changes a meaningful decision; a chart must answer a question.
4. Prototype cover, one evidence spread and one interaction. Compare against actual browser render at 390 and 1440 CSS px before extending the design. Do not ship a screenshot as a web page.
5. Build source and evidence as structured data; render accessible HTML; progressively enhance. Provide caption, text alternative, and source link adjacent to each material chart.
6. Verify each release gate and deliver actual website plus source and handoff.

## Audit or revise
1. Preserve baseline URL, commit, routes, capabilities and screenshots. Separate observed failures from speculative opportunities.
2. Rank by severity, evidence, reader impact and effort. Do not replace a successful design merely because a newer model is available.
3. Make small reversible patches with regression tests; use a review branch and compare against baseline before merging.
4. Verify actual deployed bytes and behavior. Recheck the source if editorial claims change; distinguish updated facts from the original study.

## Deliverable quality
Minimum artifacts: brief, claim ledger, rights ledger, production site, test evidence, limitations, release/rollback note. For a short/simple brief, combine ledgers into one table; for complex material, use CSV or JSON. Use `assets/claim-ledger.csv` and `assets/qa-register.csv`.
Do not turn an unverified estimate into data, illustrative image into a chart, or manual ratings into a scientific benchmark.
Use `assets/edition-starter.html` only as a semantic scaffold; define a topic-specific original visual identity and replace every placeholder before publication.

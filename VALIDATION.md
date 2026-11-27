# Validation — 2026-11-27

Version 0.2.0 was downloaded from the public repository and checked in an isolated Python environment.

- 15 package files retrieved, including LICENSE, HTML scaffold and the static checker.
- Skill name and description lengths and name syntax checked against the Agent Skills specification; all 11 relative Markdown references in SKILL.md resolved.
- Static checker executed on the starter HTML: exit 0, no flagged issues.
- Static checker executed on an intentionally broken fixture: exit 1, detected six expected issues (missing language, missing main, duplicate ID, invalid fragment, missing alt, missing local asset).

These are **structural and smoke checks**, not an official certification. The official skills-ref library was not installed in that environment. Full accessibility, real reader evaluation, independent research-input trials and controlled comparison with/without the skill have not yet been performed. The evaluation plan is in [examples/evaluation-cases.md](examples/evaluation-cases.md).

The ITMO case served as a source-code audit and regression-fix pilot, not as a controlled comparison of GPT model versions.

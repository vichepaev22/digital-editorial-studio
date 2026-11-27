# Engineering and quality verification

Baseline: capture commit, route list, key screenshots and interaction behavior. For production revisions, use a branch and compare changes. Avoid unnecessary stack migrations.

Implement semantic landmarks, progressive enhancement, robust local state validation (malformed JSON, wrong schema, quota, unavailable storage), useful errors and safe output encoding. No client-side secrets; avoid injecting raw user strings into HTML. External links must identify login requirements and version differences. A 200 HTTP response is not proof of a working service.

Test with Playwright across desktop/mobile and keyboard; use axe-core for automated accessibility findings plus manual keyboard, zoom, screen reader and contrast checks. Target WCAG 2.2 AA without claiming conformance from automation alone. Include no-JS fallback, loading/error states and reduced motion. Test interactions, export/import if implemented, local persistence, share links, search, navigation, and third-party failure.
Use Lighthouse for lab observations; Core Web Vitals field targets at the 75th percentile: LCP <=2.5 s, INP <=200 ms, CLS <=0.1. No field data means no field verdict. Record environment and run date.
Privacy: external analytics off by default unless appropriate configuration and legal basis are established; minimize events, never send free-text inputs, secrets or private content. Test opt-in/withdrawal and network requests. Third-party fonts/images may still make network requests; document or remove them.
Deploy via authorized repository workflow; check live URL, asset responses, build commit and CI status. Record rollback target. Do not mark a queued CI run as passed.

Sources: https://www.w3.org/TR/WCAG22/ ; https://playwright.dev/docs/accessibility-testing ; https://web.dev/articles/vitals ; https://agentskills.io/specification .

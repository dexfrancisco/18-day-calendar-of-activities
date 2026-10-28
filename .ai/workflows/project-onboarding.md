# Existing Project Onboarding Workflow
1. Inspect without changing implementation.
2. Detect stack/version.
3. Map architecture.
4. Map DB/schema/migrations.
5. Map authentication/authorization/roles.
6. Map UI/component system.
7. Map tests/build tooling.
8. Map existing logging/audit.
9. Map integrations/deployment.
10. Populate missing memory from observed facts.
11. Populate state and known issues.
12. Record important decisions.
13. Review existing documentation before modifying it.
14. Make no code changes merely because onboarding ran.


## Global skill integration
- Discover and read the actual installed global skills relevant to the project; do not copy global skills into the repository.
- For UI/UX tasks, follow `.ai/workflows/skill-selection-and-design-quality.md`, prioritizing `design-taste-frontend` and `ui-ux-pro-max` if installed.
- After onboarding, record only facts verified from source code, configuration, tests, and explicit user statements. Mark unknowns as unverified.
- Before finishing onboarding, follow `.ai/workflows/memory-update.md`, reread edited files, and report exactly what was updated.

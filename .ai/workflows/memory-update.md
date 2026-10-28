# Required Memory Update Workflow

Run this before finishing every meaningful development or design task.

1. Identify durable, verified changes: requirements, architecture, schema/API, dependencies, security/audit behavior, design system, component patterns, bugs, decisions, and verification results.
2. Choose only the affected files. Use `.ai/memory/` for durable project knowledge, `.ai/planning/` for planned requirements/features/roles/workflows/roadmap, and `.ai/state/` for current progress and next steps.
3. Update `.ai/memory/ui-ux.md` when design tokens, components, layouts, interaction patterns, accessibility requirements, or design decisions change.
4. Update `.ai/memory/decisions.md` when a durable choice is made or confirmed, including its reason and impact.
5. Update `.ai/state/CURRENT.md`, `PROGRESS.md`, `TASKS.md`, and `NEXT.md` when status changes. Do not rewrite state files if the task did not affect them.
6. For substantial sessions or likely handoffs, add a concise note under `.ai/sessions/` using `.ai/templates/session.md`. Never save full transcripts, secrets, or large logs.
7. Keep verified facts separate from assumptions and unknowns. A code change does not prove production deployment; a test not run must not be recorded as passed.
8. Re-read every file changed and inspect the diff. Verify persistence, accuracy, and lack of duplication.
9. In the final response, list exact memory/state/planning files changed and the tests/checks actually performed. If no update is warranted, state why. If a write or verification fails, disclose the blocker.

Memory maintenance is part of completing meaningful work. Do not silently skip it after coding.

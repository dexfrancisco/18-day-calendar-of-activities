# Project AI Instructions — V5 Global Skills Integration

This project uses the V5 project-local context system together with the global Antigravity skills installed on this machine. Project files describe THIS repository; global skills provide reusable capabilities. Do not copy global skills into this project.

## Mandatory start-of-task behavior

For every substantial engineering or design task:

1. Confirm the project root and inspect the existing repository before making assumptions.
2. Read relevant `.ai/memory/`, `.ai/state/`, `.ai/planning/`, and `.ai/rules/` files. For a new project, follow `.ai/workflows/new-project.md`; for an existing project receiving these files for the first time, follow `.ai/workflows/project-onboarding.md`; for an already established project, follow `.ai/workflows/existing-project.md`.
3. Discover and read the actual installed global `SKILL.md` files relevant to the task. Do not assume skill names, locations, or availability. The global mandatory-skill-usage rule remains authoritative.
4. Select skills based on the task and use their procedures, not just their names. In the task summary, state the most relevant skills actually consulted when meaningful.
5. Preserve existing architecture, components, conventions, and user decisions unless a deliberate change is required and explained.

## Skill selection — especially UI/UX and frontend design

For any task involving a page, screen, dashboard, component, layout, visual styling, design system, or frontend experience:

1. Before coding, inspect the installed skills and consult the most relevant design skills. Prioritize `design-taste-frontend` and `ui-ux-pro-max` when installed; also consult applicable skills such as `ui-ux-design`, `design-system`, `typography-and-color`, `layout-and-component-design`, `responsive-design`, `accessibility`, `dashboards`, `data-dense-ui`, `forms`, and `audit-ui`.
2. Read the repository's existing design system, component library, tokens, and patterns. Reuse the actual project stack and component library rather than introducing a competing system.
3. Establish a concise design direction before implementation: product context, target users, information hierarchy, density, typography, color roles, spacing, interaction states, responsive behavior, and accessibility.
4. Avoid generic “AI-generated” visual defaults. Do not automatically reach for a generic SaaS dashboard, arbitrary gradients, excessive rounded cards, decorative charts, uniform card grids, oversized headings, or meaningless icons. Use them only when they serve a clear product-specific purpose.
5. Make intentional, coherent choices grounded in the product's users and domain. Prioritize strong hierarchy, useful density, restrained color, deliberate typography, consistent spacing, meaningful empty/loading/error states, keyboard support, and responsive behavior.
6. Use real project data shapes and meaningful labels. Never invent metrics or fill the interface with fake content merely to make it look populated.
7. Verify the result in the actual app when tools and environment permit. Use the installed browser-testing skill / Chrome DevTools MCP when appropriate and authorized. Check common viewport sizes, interactions, console/runtime errors, and accessibility basics. Report any checks not performed.
8. Before finishing, compare the implementation against the selected design skills and the project's design rules. Correct obvious generic patterns and inconsistencies before declaring completion.

If the preferred design skills are not installed or cannot be accessed, say so briefly and use the closest available installed skills. Never claim to have consulted a skill that was not actually read.

## Mandatory completion and project-memory maintenance

For every meaningful change—feature, bug fix, schema/API change, dependency/configuration change, design-system change, security/audit change, confirmed requirement, or material verification result:

1. Evaluate which project memory, planning, rule, known-issue, and state files are affected.
2. Update only those files with verified facts. Keep assumptions and unresolved questions clearly labeled. Do not rewrite unrelated files or store the full conversation.
3. Update `.ai/state/` when task status, progress, blockers, or next steps change.
4. Record durable decisions in `.ai/memory/decisions.md`; update `.ai/memory/ui-ux.md` when design tokens, components, patterns, or interaction decisions materially change.
5. For substantial sessions or handoffs, write a concise note under `.ai/sessions/` using the available template.
6. Re-read every changed documentation file and inspect the diff to verify that changes were actually saved and are accurate.
7. In the final response, list the exact project memory/state/docs files updated. If no update was warranted, say so. If writing or verification was blocked, disclose it; never claim an update or test that did not happen.

Use `.ai/workflows/project-handoff.md` when handing work to a future session. Use `.ai/workflows/audit-feature.md` when asked to audit a feature.

## Truth, safety, and scope

- Repository code, migrations, tests, configuration, and explicit user decisions are evidence. Old memory is helpful but can be stale.
- Do not invent project requirements, architecture, APIs, database facts, design tokens, test results, or deployment status.
- Never store credentials, tokens, private keys, or secret values in project memory.
- Follow the real stack and installed component library. React/shadcn and Laravel/Livewire/Flux/Filament are options only when supported by the repository or selected by the user.
- Make the smallest coherent change; avoid unrelated refactors.
- Use global skills for reusable methods and this project's `.ai/` files for project-specific knowledge.

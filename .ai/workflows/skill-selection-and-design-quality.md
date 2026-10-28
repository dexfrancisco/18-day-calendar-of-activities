# Skill Selection and Design Quality Workflow

Use this workflow for substantial tasks, and always for frontend/UI/UX work.

## A. Identify the task
- Classify the work: discovery, planning, backend, database, security, UI/UX, testing, refactoring, documentation, or deployment.
- Inspect the repository and identify the actual framework, component library, and relevant project rules.
- Discover installed global skills using the configured global skills directory and follow the global mandatory-skill rule.

## B. Select skills deliberately
- Read the `SKILL.md` for each relevant installed skill before implementation.
- For UI/UX/frontend tasks, prioritize `design-taste-frontend` and `ui-ux-pro-max` when present. Add relevant skills such as `ui-ux-design`, `design-system`, `typography-and-color`, `layout-and-component-design`, `responsive-design`, `accessibility`, `dashboards`, `data-dense-ui`, `forms`, `audit-ui`, `browser-testing-with-devtools`, and `testing` as applicable.
- For other tasks, select skills that match the actual work: architecture, project analysis, planning, domain modeling, database engineering, security, debugging, code review, testing, performance, refactoring, Git, documentation, memory maintenance, and project handoff.
- Do not load every skill indiscriminately. Select the smallest useful set, and do not claim a skill was used unless its instructions were read.

## C. Design before coding
For UI work, write a short internal design brief before implementation:
- user and task context;
- content hierarchy and density;
- visual direction and rationale;
- typography and color roles;
- layout and spacing;
- component reuse;
- responsive behavior;
- interaction, empty/loading/error states;
- accessibility and reduced motion.
Then implement the design using the project's existing stack and component library.

## D. Avoid generic AI-looking interfaces
- Avoid unmotivated gradients, excessive rounded cards, repeated identical card grids, gratuitous icons, decorative data visualizations, and generic SaaS layouts.
- Do not ban these patterns categorically; use them only when justified by the product and design direction.
- Use clear hierarchy, domain-appropriate density, restrained color, purposeful whitespace, intentional typography, realistic content, and consistent interaction behavior.
- Never invent real-looking business metrics or records to decorate a page.
- Prefer a distinctive but usable result over novelty for its own sake.

## E. Verify and record
- Run available tests and relevant browser checks when possible.
- Check responsive behavior, interactive states, accessibility basics, and console errors where tooling permits.
- Update `.ai/memory/ui-ux.md` when durable design decisions change.
- Follow `.ai/workflows/memory-update.md` (if present) or the memory-maintenance rule before finishing meaningful work.
- Report skills actually consulted, checks actually run, documentation updated, and any blockers.

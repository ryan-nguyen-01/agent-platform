# Structure & conventions

How this codebase is organized and the patterns Kiro must follow so generated code fits in seamlessly.
**Scan the area before editing and keep this file current** — it is the project's living style guide.
Match what exists; never impose a different style.

## Backend (Java / Spring Boot)

```text
- Layering:          <controller → service → repository?>  package-by-feature or package-by-layer?
- DTO & mapping:     <MapStruct / manual>; entities never leak out of the service layer
- Error handling:    <@ControllerAdvice + error response shape>
- Validation:        <Bean Validation @Valid / custom>
- Persistence:       <Spring Data repositories / query style>; transactions on the service layer
- Config & secrets:  <application.yml profiles / env>; never hard-code secrets
- Logging:           <SLF4J pattern, levels>
- Naming:            <Controller/Service/RepositoryImpl suffixes, package names>
- Tests:             <where, naming, JUnit/Testcontainers patterns>
```

## Frontend (ReactJS)

```text
- Folder layout:     <feature folders / atomic / by-type>
- Components:        function components; naming PascalCase; one component per file?
- Shared/common:     WHERE shared components live and how to import them — reuse, don't recreate
- Hooks:             custom hooks location + patterns (use*, single responsibility)
- State:             <Redux Toolkit slices / Zustand stores / Context> — the project's choice
- Data fetching:     <React Query keys/conventions / service layer>
- Styling:           <Tailwind classes / shadcn / styled-components> — the existing approach only
- Imports/aliases:   <@/ alias, import ordering>
- Tests:             <Vitest/RTL + Playwright e2e conventions>
```

## Shared

```text
- Lint/format:       <ESLint/Prettier, Checkstyle/Spotless>
- Branch/commit:     <convention>
- Build/run:         <commands to build, run, test BE and FE>
- Gotchas:           <anything surprising future-you should know>
```

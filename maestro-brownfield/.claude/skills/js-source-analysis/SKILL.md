---
name: js-source-analysis
description: "Analyze JavaScript/TypeScript source files to build tooling and extensions — parse to AST, traverse and query, resolve symbols/scopes, build import/export and call graphs, and run codemods. Use when writing browser extensions, VS Code/editor extensions, Tauri desktop tools, or Node CLIs that read or transform JS/TS source. Triggers: analyze JS source, parse AST, codemod, dependency graph, extension that inspects code, static analysis."
category: meta-process
version: "1.0.0"
license: MIT
metadata:
  author: Maestro
---

# JS/TS Source Analysis for Tools & Extensions

Analyze JavaScript/TypeScript source to power tools and extensions. The job is always: **parse →
query/understand → (optionally) transform → emit**, with correctness and incremental performance.

## Pick the right parser

| Need | Use |
|------|-----|
| Fast JS/JSX/TS AST, ESTree-compatible | `acorn` (+ `acorn-jsx`), `@babel/parser`, or `oxc-parser` (Rust-fast) |
| Full TS type info (types, symbols, checker) | TypeScript Compiler API (`typescript`) — `createProgram`, `TypeChecker` |
| High-level codemods with type-aware edits | `ts-morph` (wraps the TS compiler) |
| Cross-language / editor-grade incremental | `tree-sitter` (+ `tree-sitter-javascript`/`-typescript`) — great for editors |
| Bundler-speed transform | `swc` (`@swc/core`), `esbuild` (transform/metafile only, not a full AST) |

Rule: if you only need structure (imports, calls, exported names) use a fast ESTree parser
(acorn/babel/oxc). If you need **types** (is this symbol a Promise? where is it defined across files?)
you need the **TS compiler `Program` + `TypeChecker`** — a single-file AST cannot give types.

## Core analysis patterns

```text
- AST traversal: @babel/traverse (visitor pattern) or estree-walker; TS uses ts.forEachChild recursion.
- Symbol & scope: TS TypeChecker.getSymbolAtLocation / getTypeAtLocation; for plain AST track scopes
  with eslint-scope to resolve bindings (avoid naive name matching).
- Imports/exports & dependency graph: collect ImportDeclaration/ExportNamedDeclaration/dynamic import();
  resolve specifiers with the project's resolver (tsconfig paths, package "exports", node resolution —
  use enhanced-resolve or oxc-resolver, never hand-roll path joins).
- Call graph: map CallExpression callees to resolved declarations; needed for dead-code / impact analysis.
- Codemods: jscodeshift (ESTree) or ts-morph (type-aware). Preserve formatting (recast / ts-morph keeps
  trivia); re-print only changed nodes; round-trip through tests.
- Source maps: when transforming, emit source maps (magic-string for surgical edits keeps mappings cheap).
```

## Per target

```text
- Browser extension (MV3): content scripts can read the page's DOM but NOT the page's module source
  reliably at runtime — analyze bundled/served JS by fetching it, or instrument at build time. Heavy
  parsing belongs in the background/service worker or offscreen document, not the content script.
- VS Code / editor extension: prefer the TS language service / LSP instead of re-parsing — reuse the
  editor's incremental program. Use tree-sitter for fast, error-tolerant highlighting/folding. Run
  expensive analysis in a separate process/worker; debounce on document change.
- Tauri desktop tool: do JS analysis in the JS frontend (or a sidecar Node process) and pass results
  to Rust; or call a Rust parser (oxc/swc bindings) from the Rust side for speed. See rust-browser-profile
  and tauri-knowledge-patch for the Rust half.
- Node CLI / build tool: stream files, parse in a worker_threads pool for large repos, cache by content
  hash + mtime so re-runs are incremental.
```

## Correctness & performance

```text
- Set the parser to the right ecmaVersion/sourceType (module vs script) + JSX/TS plugins, or you get
  silent mis-parses. Decorators, import attributes, and TS `satisfies` need the right plugin flags.
- Handle parse errors per-file (error-tolerant for editors; fail-loud for codemods) — never crash the
  whole run on one bad file.
- Don't regex JS to "understand" it (comments/strings/template literals will bite you) — parse.
- Cache ASTs/type info by content hash; only re-analyze changed files; for monorepos respect tsconfig
  project references.
- After any codemod: run the project's typecheck + tests; diff must be minimal (formatting preserved).
```

Pairs with `legacy-code-comprehension` (understanding an unfamiliar codebase first),
`typescript-advanced-types`, and `rust-browser-profile` / `tauri-knowledge-patch` for the native side.

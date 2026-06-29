# R-026: Change Integrity & Dead-Code Removal

## Applies to

Service/built-in coders, Coder Leader, Dev Verification. The defect class this prevents: an agent
updates logic to a new approach but reads the surrounding code shallowly — leaving outdated code that
still runs, orphan references, or two conflicting paths, which compiles/passes yet errors later.

## Rules

```text
R-026-01: READ THE WHOLE UNIT FIRST. Before editing a function/module, read it in full — every branch,
  early return, side effect, and the types it touches. No blind partial edits to a fragment you have
  not understood end to end.
R-026-02: TRACE EVERY CALLER. When you change a signature, return shape, behavior, or remove/rename a
  symbol, find ALL its callers/references (grep imports, usages, routes, events, configs, tests) and
  update or consciously confirm each. An updated definition with un-updated callers is INCOMPLETE work.
R-026-03: REMOVE DEAD CODE the change creates: now-unused variables, imports, parameters, branches,
  helper functions, feature flags, config keys, and commented-out old logic. Do not leave outdated
  code "just in case" — version control is the safety net.
R-026-04: ONE PATH, NOT TWO. Replace the old logic, do not append the new beside it. The old and new
  code paths must never both be reachable/executing — that is the exact cause of "it still runs and
  throws". If a transition period is truly needed, gate it explicitly and journal why (R-024).
R-026-05: VERIFY THE CLEANUP (evidence, R-023-03):
  - grep for every removed/renamed symbol -> expect ZERO remaining references.
  - run typecheck/lint/build -> resolve unused/unreachable warnings, do not suppress them.
  - tests exercise the CHANGED branch, not only the happy path that was already green.
R-026-06: DONE BAR. "Done" is invalid if dead code, orphan references, duplicate old/new paths, or
  un-updated callers remain — even when tests pass. Leaving outdated reachable code is a defect, not a
  style nit (it will error in a path the current test did not hit).
```

## Dev verification

```text
Dev Verification runs the CHANGE-INTEGRITY critical check (R-007): reject Code Done when a changed
symbol still has stale references, when removed logic left unused imports/vars/branches, or when an
old code path remains reachable next to the new one. Require the coder's grep + build/lint evidence.
```

## Violation handling

Return the change to the coder with the specific orphan/dead-code findings. Recurring occurrences feed
the feedback loop (R-010) as an anti-pattern.

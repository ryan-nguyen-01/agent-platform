---
name: playwright-best-practices
description: Use when writing Playwright tests, fixing flaky tests, debugging failures, implementing Page Object Model, configuring CI/CD, optimizing performance, mocking APIs, handling authentication or OAuth, testing accessibility (axe-core), file uploads/downloads, date/time mocking, WebSockets, geolocation, permissions, multi-tab/popup flows, mobile/responsive layouts, touch gestures, GraphQL, error handling, offline mode, multi-user collaboration, third-party services (payments, email verification), console error monitoring, global setup/teardown, test annotations (skip, fixme, slow), test tags (@smoke, @fast, @critical, filtering with --grep), project dependencies, security testing (XSS, CSRF, auth), performance budgets (Web Vitals, Lighthouse), iframes, component testing, canvas/WebGL, service workers/PWA, test coverage, i18n/localization, Electron apps, or browser extension testing. Covers E2E, component, API, visual, accessibility, security, Electron, and extension testing.
license: MIT
metadata:
  author: currents.dev
  version: "1.1"
  category: qc-testing
  summary: Test e2e Playwright
---

# Playwright Best Practices

This skill provides comprehensive guidance for all aspects of Playwright test development, from writing new tests to debugging and maintaining existing test suites.

## Activity-Based Reference Guide

Consult these references based on what you're doing:

### Writing New Tests

**When to use**: Creating new test files, writing test cases, implementing test scenarios

| Activity                            | Reference Files                                                                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Writing E2E tests**               | [test-suite-structure.md](references/core/test-suite-structure.md), [locators.md](references/core/locators.md), [assertions-waiting.md](references/core/assertions-waiting.md) |
| **Writing component tests**         | [component-testing.md](references/testing-patterns/component-testing.md), [test-suite-structure.md](references/core/test-suite-structure.md)                        |
| **Writing API tests**               | [api-testing.md](references/testing-patterns/api-testing.md), [test-suite-structure.md](references/core/test-suite-structure.md)                                    |
| **Writing GraphQL tests**           | [graphql-testing.md](references/testing-patterns/graphql-testing.md), [api-testing.md](references/testing-patterns/api-testing.md)                                  |
| **Writing visual regression tests** | [visual-regression.md](references/testing-patterns/visual-regression.md), [canvas-webgl.md](references/testing-patterns/canvas-webgl.md)                            |
| **Structuring test code with POM**  | [page-object-model.md](references/core/page-object-model.md), [test-suite-structure.md](references/core/test-suite-structure.md)                                    |
| **Setting up test data/fixtures**   | [fixtures-hooks.md](references/core/fixtures-hooks.md), [test-data.md](references/core/test-data.md)                                                                |
| **Handling authentication**         | [authentication.md](references/advanced/authentication.md), [authentication-flows.md](references/advanced/authentication-flows.md)                                  |
| **Testing date/time features**      | [clock-mocking.md](references/advanced/clock-mocking.md)                                                                                                 |
| **Testing file upload/download**    | [file-operations.md](references/testing-patterns/file-operations.md), [file-upload-download.md](references/testing-patterns/file-upload-download.md)                |
| **Testing forms/validation**        | [forms-validation.md](references/testing-patterns/forms-validation.md)                                                                                   |
| **Testing drag and drop**           | [drag-drop.md](references/testing-patterns/drag-drop.md)                                                                                                 |
| **Testing accessibility**           | [accessibility.md](references/testing-patterns/accessibility.md)                                                                                         |
| **Testing security (XSS, CSRF)**    | [security-testing.md](references/testing-patterns/security-testing.md)                                                                                   |
| **Using test annotations**          | [annotations.md](references/core/annotations.md)                                                                                                         |
| **Using test tags**                 | [test-tags.md](references/core/test-tags.md)                                                                                                             |
| **Testing iframes**                 | [iframes.md](references/browser-apis/iframes.md)                                                                                                         |
| **Testing canvas/WebGL**            | [canvas-webgl.md](references/testing-patterns/canvas-webgl.md)                                                                                           |
| **Internationalization (i18n)**     | [i18n.md](references/testing-patterns/i18n.md)                                                                                                           |
| **Testing Electron apps**           | [electron.md](references/testing-patterns/electron.md)                                                                                                   |
| **Testing browser extensions**      | [browser-extensions.md](references/testing-patterns/browser-extensions.md)                                                                               |

### Mobile & Responsive Testing

**When to use**: Testing mobile devices, touch interactions, responsive layouts

| Activity                        | Reference Files                                                                  |
| ------------------------------- | -------------------------------------------------------------------------------- |
| **Device emulation**            | [mobile-testing.md](references/advanced/mobile-testing.md)                                  |
| **Touch gestures (swipe, tap)** | [mobile-testing.md](references/advanced/mobile-testing.md)                                  |
| **Viewport/breakpoint testing** | [mobile-testing.md](references/advanced/mobile-testing.md)                                  |
| **Mobile-specific UI**          | [mobile-testing.md](references/advanced/mobile-testing.md), [locators.md](references/core/locators.md) |

### Real-Time & Browser APIs

**When to use**: Testing WebSockets, geolocation, permissions, multi-tab flows

| Activity                        | Reference Files                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| **WebSocket/real-time testing** | [websockets.md](references/browser-apis/websockets.md)                                              |
| **Geolocation mocking**         | [browser-apis.md](references/browser-apis/browser-apis.md)                                          |
| **Permission handling**         | [browser-apis.md](references/browser-apis/browser-apis.md)                                          |
| **Clipboard testing**           | [browser-apis.md](references/browser-apis/browser-apis.md)                                          |
| **Camera/microphone mocking**   | [browser-apis.md](references/browser-apis/browser-apis.md)                                          |
| **Multi-tab/popup flows**       | [multi-context.md](references/advanced/multi-context.md)                                            |
| **OAuth popup handling**        | [third-party.md](references/advanced/third-party.md), [multi-context.md](references/advanced/multi-context.md) |

### Debugging & Troubleshooting

**When to use**: Test failures, element not found, timeouts, unexpected behavior

| Activity                                          | Reference Files                                                                                                                                |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Debugging test failures**                       | [debugging.md](references/debugging/debugging.md), [assertions-waiting.md](references/core/assertions-waiting.md)                                                    |
| **Fixing flaky tests**                            | [flaky-tests.md](references/debugging/flaky-tests.md), [debugging.md](references/debugging/debugging.md), [assertions-waiting.md](references/core/assertions-waiting.md)        |
| **Debugging flaky parallel runs**                 | [flaky-tests.md](references/debugging/flaky-tests.md), [performance.md](references/infrastructure-ci-cd/performance.md), [fixtures-hooks.md](references/core/fixtures-hooks.md) |
| **Ensuring test isolation / avoiding state leak** | [flaky-tests.md](references/debugging/flaky-tests.md), [fixtures-hooks.md](references/core/fixtures-hooks.md), [performance.md](references/infrastructure-ci-cd/performance.md) |
| **Fixing selector issues**                        | [locators.md](references/core/locators.md), [debugging.md](references/debugging/debugging.md)                                                                        |
| **Investigating timeout issues**                  | [assertions-waiting.md](references/core/assertions-waiting.md), [debugging.md](references/debugging/debugging.md)                                                    |
| **Using trace viewer**                            | [debugging.md](references/debugging/debugging.md)                                                                                                         |
| **Debugging race conditions**                     | [flaky-tests.md](references/debugging/flaky-tests.md), [debugging.md](references/debugging/debugging.md), [assertions-waiting.md](references/core/assertions-waiting.md)        |
| **Debugging console/JS errors**                   | [console-errors.md](references/debugging/console-errors.md), [debugging.md](references/debugging/debugging.md)                                                       |

### Error & Edge Case Testing

**When to use**: Testing error states, offline mode, network failures, validation

| Activity                       | Reference Files                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Error boundary testing**     | [error-testing.md](references/debugging/error-testing.md)                                                        |
| **Network failure simulation** | [error-testing.md](references/debugging/error-testing.md), [network-advanced.md](references/advanced/network-advanced.md)   |
| **Offline mode testing**       | [error-testing.md](references/debugging/error-testing.md), [service-workers.md](references/browser-apis/service-workers.md) |
| **Service worker testing**     | [service-workers.md](references/browser-apis/service-workers.md)                                                 |
| **Loading state testing**      | [error-testing.md](references/debugging/error-testing.md)                                                        |
| **Form validation testing**    | [error-testing.md](references/debugging/error-testing.md)                                                        |

### Multi-User & Collaboration Testing

**When to use**: Testing features involving multiple users, roles, or real-time collaboration

| Activity                       | Reference Files                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| **Multiple users in one test** | [multi-user.md](references/advanced/multi-user.md)                                              |
| **Real-time collaboration**    | [multi-user.md](references/advanced/multi-user.md), [websockets.md](references/browser-apis/websockets.md) |
| **Role-based access testing**  | [multi-user.md](references/advanced/multi-user.md)                                              |
| **Concurrent action testing**  | [multi-user.md](references/advanced/multi-user.md)                                              |

### Architecture Decisions

**When to use**: Choosing test patterns, deciding between approaches, planning test architecture

| Activity                     | Reference Files                                           |
| ---------------------------- | --------------------------------------------------------- |
| **POM vs fixtures decision** | [pom-vs-fixtures.md](references/architecture/pom-vs-fixtures.md)     |
| **Test type selection**      | [test-architecture.md](references/architecture/test-architecture.md) |
| **Mock vs real services**    | [when-to-mock.md](references/architecture/when-to-mock.md)           |
| **Test suite structure**     | [test-suite-structure.md](references/core/test-suite-structure.md)   |

### Framework-Specific Testing

**When to use**: Testing React, Angular, Vue, or Next.js applications

| Activity                  | Reference Files                     |
| ------------------------- | ----------------------------------- |
| **Testing React apps**    | [react.md](references/frameworks/react.md)     |
| **Testing Angular apps**  | [angular.md](references/frameworks/angular.md) |
| **Testing Vue/Nuxt apps** | [vue.md](references/frameworks/vue.md)         |
| **Testing Next.js apps**  | [nextjs.md](references/frameworks/nextjs.md)   |

### Refactoring & Maintenance

**When to use**: Improving existing tests, code review, reducing duplication

| Activity                             | Reference Files                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Refactoring to Page Object Model** | [page-object-model.md](references/core/page-object-model.md), [test-suite-structure.md](references/core/test-suite-structure.md) |
| **Improving test organization**      | [test-suite-structure.md](references/core/test-suite-structure.md), [page-object-model.md](references/core/page-object-model.md) |
| **Extracting common setup/teardown** | [fixtures-hooks.md](references/core/fixtures-hooks.md)                                                                |
| **Replacing brittle selectors**      | [locators.md](references/core/locators.md)                                                                            |
| **Removing explicit waits**          | [assertions-waiting.md](references/core/assertions-waiting.md)                                                        |
| **Creating test data factories**     | [test-data.md](references/core/test-data.md)                                                                          |
| **Configuration setup**              | [configuration.md](references/core/configuration.md)                                                                  |

### Infrastructure & Configuration

**When to use**: Setting up projects, configuring CI/CD, optimizing performance

| Activity                                | Reference Files                                                                                                          |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Configuring Playwright project**      | [configuration.md](references/core/configuration.md), [projects-dependencies.md](references/core/projects-dependencies.md)                     |
| **Setting up CI/CD pipelines**          | [ci-cd.md](references/infrastructure-ci-cd/ci-cd.md), [github-actions.md](references/infrastructure-ci-cd/github-actions.md)                   |
| **GitHub Actions setup**                | [github-actions.md](references/infrastructure-ci-cd/github-actions.md)                                                              |
| **GitLab CI setup**                     | [gitlab.md](references/infrastructure-ci-cd/gitlab.md)                                                                              |
| **Other CI providers**                  | [other-providers.md](references/infrastructure-ci-cd/other-providers.md)                                                            |
| **Docker/container setup**              | [docker.md](references/infrastructure-ci-cd/docker.md)                                                                              |
| **Global setup & teardown**             | [global-setup.md](references/core/global-setup.md)                                                                                  |
| **Project dependencies**                | [projects-dependencies.md](references/core/projects-dependencies.md)                                                                |
| **Optimizing test performance**         | [performance.md](references/infrastructure-ci-cd/performance.md), [test-suite-structure.md](references/core/test-suite-structure.md)           |
| **Configuring parallel execution**      | [parallel-sharding.md](references/infrastructure-ci-cd/parallel-sharding.md), [performance.md](references/infrastructure-ci-cd/performance.md) |
| **Isolating test data between workers** | [fixtures-hooks.md](references/core/fixtures-hooks.md), [performance.md](references/infrastructure-ci-cd/performance.md)                       |
| **Test coverage**                       | [test-coverage.md](references/infrastructure-ci-cd/test-coverage.md)                                                                |
| **Test reporting/artifacts**            | [reporting.md](references/infrastructure-ci-cd/reporting.md)                                                                        |

### Advanced Patterns

**When to use**: Complex scenarios, API mocking, network interception

| Activity                             | Reference Files                                                                                              |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Mocking API responses**            | [test-suite-structure.md](references/core/test-suite-structure.md), [network-advanced.md](references/advanced/network-advanced.md) |
| **Network interception**             | [network-advanced.md](references/advanced/network-advanced.md), [assertions-waiting.md](references/core/assertions-waiting.md)     |
| **GraphQL mocking**                  | [network-advanced.md](references/advanced/network-advanced.md)                                                          |
| **HAR recording/playback**           | [network-advanced.md](references/advanced/network-advanced.md)                                                          |
| **Custom fixtures**                  | [fixtures-hooks.md](references/core/fixtures-hooks.md)                                                                  |
| **Advanced waiting strategies**      | [assertions-waiting.md](references/core/assertions-waiting.md)                                                          |
| **OAuth/SSO mocking**                | [third-party.md](references/advanced/third-party.md), [multi-context.md](references/advanced/multi-context.md)                     |
| **Payment gateway mocking**          | [third-party.md](references/advanced/third-party.md)                                                                    |
| **Email/SMS verification mocking**   | [third-party.md](references/advanced/third-party.md)                                                                    |
| **Failing on console errors**        | [console-errors.md](references/debugging/console-errors.md)                                                             |
| **Security testing (XSS, CSRF)**     | [security-testing.md](references/testing-patterns/security-testing.md)                                                  |
| **Performance budgets & Web Vitals** | [performance-testing.md](references/testing-patterns/performance-testing.md)                                            |
| **Lighthouse integration**           | [performance-testing.md](references/testing-patterns/performance-testing.md)                                            |
| **Test annotations (skip, fixme)**   | [annotations.md](references/core/annotations.md)                                                                        |
| **Test tags (@smoke, @fast)**        | [test-tags.md](references/core/test-tags.md)                                                                            |
| **Test steps for reporting**         | [annotations.md](references/core/annotations.md)                                                                        |

## Quick Decision Tree

```
What are you doing?
│
├─ Writing a new test?
│  ├─ E2E test → references/core/test-suite-structure.md, references/core/locators.md, references/core/assertions-waiting.md
│  ├─ Component test → references/testing-patterns/component-testing.md
│  ├─ API test → references/testing-patterns/api-testing.md, references/core/test-suite-structure.md
│  ├─ GraphQL test → references/testing-patterns/graphql-testing.md
│  ├─ Visual regression → references/testing-patterns/visual-regression.md
│  ├─ Visual/canvas test → references/testing-patterns/canvas-webgl.md, references/core/test-suite-structure.md
│  ├─ Accessibility test → references/testing-patterns/accessibility.md
│  ├─ Mobile/responsive test → references/advanced/mobile-testing.md
│  ├─ i18n/locale test → references/testing-patterns/i18n.md
│  ├─ Electron app test → references/testing-patterns/electron.md
│  ├─ Browser extension test → references/testing-patterns/browser-extensions.md
│  ├─ Multi-user test → references/advanced/multi-user.md
│  ├─ Form validation test → references/testing-patterns/forms-validation.md
│  └─ Drag and drop test → references/testing-patterns/drag-drop.md
│
├─ Testing specific features?
│  ├─ File upload/download → references/testing-patterns/file-operations.md, references/testing-patterns/file-upload-download.md
│  ├─ Date/time dependent → references/advanced/clock-mocking.md
│  ├─ WebSocket/real-time → references/browser-apis/websockets.md
│  ├─ Geolocation/permissions → references/browser-apis/browser-apis.md
│  ├─ OAuth/SSO mocking → references/advanced/third-party.md, references/advanced/multi-context.md
│  ├─ Payments/email/SMS → references/advanced/third-party.md
│  ├─ iFrames → references/browser-apis/iframes.md
│  ├─ Canvas/WebGL/charts → references/testing-patterns/canvas-webgl.md
│  ├─ Service workers/PWA → references/browser-apis/service-workers.md
│  ├─ i18n/localization → references/testing-patterns/i18n.md
│  ├─ Security (XSS, CSRF) → references/testing-patterns/security-testing.md
│  └─ Performance/Web Vitals → references/testing-patterns/performance-testing.md
│
├─ Architecture decisions?
│  ├─ POM vs fixtures → references/architecture/pom-vs-fixtures.md
│  ├─ Test type selection → references/architecture/test-architecture.md
│  ├─ Mock vs real services → references/architecture/when-to-mock.md
│  └─ Test suite structure → references/core/test-suite-structure.md
│
├─ Framework-specific testing?
│  ├─ React app → references/frameworks/react.md
│  ├─ Angular app → references/frameworks/angular.md
│  ├─ Vue/Nuxt app → references/frameworks/vue.md
│  └─ Next.js app → references/frameworks/nextjs.md
│
├─ Authentication testing?
│  ├─ Basic auth patterns → references/advanced/authentication.md
│  └─ Complex flows (MFA, reset) → references/advanced/authentication-flows.md
│
├─ Test is failing/flaky?
│  ├─ Flaky test investigation → references/debugging/flaky-tests.md
│  ├─ Element not found → references/core/locators.md, references/debugging/debugging.md
│  ├─ Timeout issues → references/core/assertions-waiting.md, references/debugging/debugging.md
│  ├─ Race conditions → references/debugging/flaky-tests.md, references/debugging/debugging.md
│  ├─ Flaky only with multiple workers → references/debugging/flaky-tests.md, references/infrastructure-ci-cd/performance.md
│  ├─ State leak / isolation → references/debugging/flaky-tests.md, references/core/fixtures-hooks.md
│  ├─ Console/JS errors → references/debugging/console-errors.md, references/debugging/debugging.md
│  └─ General debugging → references/debugging/debugging.md
│
├─ Testing error scenarios?
│  ├─ Network failures → references/debugging/error-testing.md, references/advanced/network-advanced.md
│  ├─ Offline (unexpected) → references/debugging/error-testing.md
│  ├─ Offline-first/PWA → references/browser-apis/service-workers.md
│  ├─ Error boundaries → references/debugging/error-testing.md
│  └─ Form validation → references/testing-patterns/forms-validation.md, references/debugging/error-testing.md
│
├─ Refactoring existing code?
│  ├─ Implementing POM → references/core/page-object-model.md
│  ├─ Improving selectors → references/core/locators.md
│  ├─ Extracting fixtures → references/core/fixtures-hooks.md
│  ├─ Creating data factories → references/core/test-data.md
│  └─ Configuration setup → references/core/configuration.md
│
├─ Setting up infrastructure?
│  ├─ CI/CD → references/infrastructure-ci-cd/ci-cd.md
│  ├─ GitHub Actions → references/infrastructure-ci-cd/github-actions.md
│  ├─ GitLab CI → references/infrastructure-ci-cd/gitlab.md
│  ├─ Other CI providers → references/infrastructure-ci-cd/other-providers.md
│  ├─ Docker/containers → references/infrastructure-ci-cd/docker.md
│  ├─ Sharding/parallel → references/infrastructure-ci-cd/parallel-sharding.md
│  ├─ Reporting/artifacts → references/infrastructure-ci-cd/reporting.md
│  ├─ Global setup/teardown → references/core/global-setup.md
│  ├─ Project dependencies → references/core/projects-dependencies.md
│  ├─ Test performance → references/infrastructure-ci-cd/performance.md
│  ├─ Test coverage → references/infrastructure-ci-cd/test-coverage.md
│  └─ Project config → references/core/configuration.md, references/core/projects-dependencies.md
│
├─ Organizing tests?
│  ├─ Skip/fixme/slow tests → references/core/annotations.md
│  ├─ Test tags (@smoke, @fast) → references/core/test-tags.md
│  ├─ Filtering tests (--grep) → references/core/test-tags.md
│  ├─ Test steps → references/core/annotations.md
│  └─ Conditional execution → references/core/annotations.md
│
└─ Running subset of tests?
   ├─ By tag (@smoke, @critical) → references/core/test-tags.md
   ├─ Exclude slow/flaky tests → references/core/test-tags.md
   ├─ PR vs nightly tests → references/core/test-tags.md, references/infrastructure-ci-cd/ci-cd.md
   └─ Project-specific filtering → references/core/test-tags.md, references/core/configuration.md
```

## Test Validation Loop

After writing or modifying tests:

1. **Run tests**: `npx playwright test --reporter=list`
2. **If tests fail**:
   - Review error output and trace (`npx playwright show-trace`)
   - Fix locators, waits, or assertions
   - Re-run tests
3. **Only proceed when all tests pass**
4. **Run multiple times** for critical tests: `npx playwright test --repeat-each=5`

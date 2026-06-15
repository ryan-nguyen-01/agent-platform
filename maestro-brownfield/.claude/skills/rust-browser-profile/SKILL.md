---
name: rust-browser-profile
description: "Control and read browser profiles from Rust — locate Chrome/Chromium/Firefox profile directories per OS, read cookies/history/bookmarks/localStorage/preferences, decrypt encrypted cookies, and drive a browser launched with a specific profile (CLI flags or CDP). Use when building a Rust tool that inspects or automates a browser profile. Triggers: read chrome profile, firefox profile, cookies sqlite, user-data-dir, CDP, browser automation in Rust."
category: backend
version: "1.0.0"
license: MIT
metadata:
  author: Maestro
---

# Rust: Control & Read Browser Profiles

Build a Rust tool that locates a browser profile, reads its data, and/or drives a browser running on
that profile. Two distinct modes — **read at rest** (parse the profile's files) and **control live**
(launch/automate the browser) — do not mix them on the same running profile (file locks + corruption).

## Locate the profile (per OS)

```text
Chrome/Chromium "User Data" root:
  macOS   ~/Library/Application Support/Google/Chrome
  Linux   ~/.config/google-chrome   (chromium: ~/.config/chromium)
  Windows %LOCALAPPDATA%\Google\Chrome\User Data
  Profiles: "Default", "Profile 1", ... ; "Local State" lists them (and holds the cookie key).
Firefox:
  macOS   ~/Library/Application Support/Firefox/Profiles/<id>.<name>
  Linux   ~/.mozilla/firefox/<id>.<name>   Windows %APPDATA%\Mozilla\Firefox\Profiles
  profiles.ini at the parent lists profiles + the default.
```

Resolve paths with `dirs`/`directories` crate (never hard-code `$HOME`). Pick the profile by name from
`Local State` (Chrome) or `profiles.ini` (Firefox); don't assume "Default".

## Read at rest

```text
- The profile DBs are SQLite — read them with rusqlite. COPY the file first (the browser holds a lock;
  open the copy read-only with `?immutable=1` or after copy). Never write to a live profile's DB.
    Chrome:  Cookies (table cookies), History (urls/visits), Bookmarks (JSON file, not SQLite),
             "Web Data" (autofill), Login Data (credentials — treat as secret, R-013).
    Firefox: cookies.sqlite, places.sqlite (history+bookmarks), key4.db+logins.json (credentials).
- localStorage / IndexedDB are LevelDB, not SQLite → use the `rust-leveldb`/`rusty-leveldb` crate or
  drive the browser via CDP to read them; LevelDB is also locked while the browser runs.
- Preferences: Chrome "Preferences"/"Secure Preferences" are JSON → parse with serde_json
  (see serde-knowledge-patch). Firefox prefs.js is `user_pref(...)` lines → parse line-wise.
```

### Encrypted cookies (the part people miss)

```text
Chrome cookie values are encrypted (column encrypted_value), prefixed v10/v11:
  - macOS:   key = PBKDF2(HMAC-SHA1, password from Keychain "Chrome Safe Storage", salt="saltysalt",
             1003 iters, 16 bytes); AES-128-CBC. Use security-framework to read the Keychain item.
  - Linux:   key derived from Secret Service ("Chrome Safe Storage") or fallback "peanuts"; AES-128-CBC.
  - Windows: DPAPI-unwrap the key in "Local State" os_crypt.encrypted_key, then AES-256-GCM (v10).
  Crates: aes-gcm / cbc + pbkdf2 + hmac + sha1; keyring/security-framework/windows for the OS key.
Firefox: cookies are NOT encrypted (cookies.sqlite plain); logins use NSS (key4.db) — out of scope
unless you bind to NSS.
```

## Control live (automation)

```text
- Launch with a chosen profile (don't parse files while doing this):
    Chrome:  --user-data-dir=<User Data root> --profile-directory="Profile 1"
             (use a COPIED user-data-dir if you must not disturb the real one)
    add --remote-debugging-port=<n> to attach via CDP.
- Drive via Chrome DevTools Protocol from Rust: `chromiumoxide` (async, tokio) or `headless_chrome`.
  CDP lets you read cookies (Network.getAllCookies), storage, DOM, and run JS in-page — the clean way
  to read localStorage/IndexedDB without touching LevelDB on disk.
- Async I/O, watching, and concurrent reads: use tokio (see tokio-knowledge-patch). Use notify crate to
  watch the profile dir for changes.
```

## Safety & correctness

```text
- Credentials/cookies are secrets: never log or write them into artifacts (R-013); destructive actions
  on a profile need explicit confirmation (R-011-07).
- Detect a running browser before touching files at rest (locked DB / partial writes) — prefer copy +
  read-only, or switch to CDP.
- Profile schemas change across browser versions — pin/version-detect; degrade gracefully on unknown
  columns instead of panicking.
- Cross-platform paths/keychain differ — gate with cfg(target_os) and test each OS path.
```

Pairs with `rust`, `rust-knowledge-patch`, `serde-knowledge-patch` (parse JSON/prefs),
`tokio-knowledge-patch` (async CDP/watch), and `tauri-knowledge-patch` (ship it as a desktop tool).

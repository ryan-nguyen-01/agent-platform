# intake/

Drop ANY raw project material here: specs, notes, bug reports, error logs, screenshots, data dumps.
Run `/intake` (or `/onboard`, which triages first): every file is classified and indexed in
`intake/INDEX.md` — nothing is moved or edited without your approval.

This folder is for MATERIAL, not code. The project's own source code goes in `source/`. If you drop
code here by mistake, intake flags it and asks before moving it into `source/`.

WARNING: do NOT drop real secrets (.env, credentials, tokens, dumps with passwords). Intake flags
them and their contents are never quoted into any artifact (R-013) — but the safest secret is one
that never lands here.

# Single-paper root and materials handoff

The `feat/paper-site-root-20261113` consumer update installs the optional upstream
site hook from the combined template and Mathesis layer **0.3.0**, using the
normal `./tbook template update --layer upstream|mathesis --source … --to …`
commands. The layer's `v0.3.0.py` migration adds only the owned site post-build
setting; the existing canonical base URL is retained. Reading, mathematical
mappings and frozen catalog bytes are unchanged.

`./tbook build site --book chen-chen-step-m-eulerian-parity-positivity` succeeds.
The repository root is now a relative redirect to the existing book landing at
`chen-chen-step-m-eulerian-parity-positivity/`. All nested book/media URLs remain.
`mathesis-materials.json` is emitted at the site root, with the real work/version,
repository/site URLs, exact-version DOI, language-indexed reading URLs, per-deck
PDF/notes URLs and visualization URLs.

This local site has **no built HTML reading editions**; `reading` is empty rather
than advertising missing output. It has one English seminar with audience and
notes PDFs, and the step-triangle visualization. Missing Typst uses the existing
CSS cover fallback. Full reader/toolchain build and deployment remain CI work.
The site assembly may refresh reproducible build-directory slide artifacts; it
does not change the frozen `paper.pdf`, manuscript or durable source material.

Validation completed:

- `python3 docs/layer-mathesis/scripts/paper.py check --complete`: 16 hashes OK,
  8 mapped results, 0 pending, complete.
- `./tbook check`: 1 visible book, 0 errors, 0 warnings.
- Both upstream and Mathesis manifests: current (0.7.0 and 0.3.0).
- `./tbook build site --book …`: exit 0, root redirect and manifest emitted.
- `python3 docs/project/audit-site.py`: exit 0; media bytes/hashes, original
  nested URLs, root redirect, DOI and materials agree with built files.
- A temporary `./tbook serve --port 0` served the root, original landing,
  manifest, visualization and both PDFs: all six HTTP probes returned 200.
  Evidence: `evidence/publisher-site-http.json`, `site-qa.json`,
  `site-manifest.json` and `mathesis-materials.json`.

Browser automation was unavailable, so this update does not claim fresh visual
QA at desktop/mobile widths or in both themes. No push, authenticated external
request, PR, App operation or deployment was performed. The temporary server was
stopped after the probes. The dispatcher must push the upstream/layer/combined
template dependency objects before this consumer and the pinned catalog
publisher; see the catalog repository's `docs/PUBLISHER.md` for the full order.

# Upstream 0.8.2 / Mathesis 0.4.0 migration validation

The paper branch starts at main `1fabe0c` and consumes the upstream release
`85e533c20bad105dbb6999b2919bda2a6ddcb1d1`, plus Mathesis layer source
`af3d76085a17199f8d7b088587ba428c50f3e94f`. The corresponding combined
publisher template is `951a020ef0e64f2d259196cc165f0d381729c54a`.

Both updates used `./tbook template update` with explicit layer selection.
Upstream added 7 files and updated 57; the layer updated 7 files. Neither update
produced conflicts, preserved local managed-file changes or `.template-new`
files. All 241 upstream-managed files, `template.toml` and the tool-generated
manifest are byte-identical to the release (symlink targets also compared).
All 21 layer-managed files, configuration and manifest match the layer source.
Both manifest checks pass. No upstream compatibility patch remains.

The written-proof citation behavior of local `690ec33` is in the release:
purple badges without Lean verification links, no GIDs, and rejection of missing
or empty associated proofs and simultaneous Lean references. A temporary probe
of all four scenarios passed. Upstream also adds DOI, source and request links.
Its academic validator checks evidence policy on cited written-proof results;
the old local patch checked the entire edition in that function. Whole-book
`tbook check` continues to validate all environments. The film sandbox's
`root=self.root` correction and its test file are already present upstream.

## Test results

- Full template suite: **1,083 tests in 706.307 seconds; 1,026 passed,
  57 skipped, no failures or errors**, using Python 3.12.13. The skips concern
  hidden example-book coverage and platform-specific cases. `template-tests.log`
  is the complete successful run.
- Mathesis integration suite: **21 tests passed**, both in the source against
  upgraded tools and in this consumer with the existing real-paper projection.
- Catalog publisher suite: **7 discovered, 6 passed, 1 skipped**. Its optional
  full SDK preflight requires a local catalog binary and was not configured.
- Additional mdBook-dependent validation: **148 tests, 142 passed, 6 skipped**.
- The four compatibility-probe scenarios passed. The 8 reader browser checks,
  both manifest checks, and `git diff --check` passed.

Earlier full attempts exposed host tool dependencies: missing Java, system Bash
without `mapfile`, a different Chrome renderer, and the application-bundled
Node's native-library signing restriction. The successful run uses the tools
listed below and the existing Homebrew Node. No upstream code, shared workflow
or global installation was changed to resolve those local execution issues.

## Paper migration and remaining gate

The paper's eight results retain their statements and written proofs. Both
editions now carry the recorded version-2 DOI `10.5281/zenodo.23957560` and
original theorem/lemma/corollary locations, checked against the frozen TeX labels.
The catalog-owned projection, generated manifest, manuscript, receipts, identity,
author metadata, result mapping, book metadata, site configuration and Lean pin
were not modified.

Upstream 0.8.2 additionally requires canonical formalization-request URLs and
registration of the repository/book/result in each issue. An anonymous read of
the complete public issue queue found only the unrelated golden-deficit issue
#1. The eight Chen–Chen results have no registrations, and this work package
permits no authenticated requests or external writes. No URL was fabricated.
See `REQUESTS.md` and the unmodified `tbook requests --json` output.

Consequently:

- `paper.py check --complete` exits 1 at the Chinese edition's eight missing
  requests. The existing hash, identity, claim and proof checks are not bypassed.
- `./tbook check` exits 1 with 26 errors, all missing-request diagnostics:
  16 book environments plus 10 deck citations (two results are cited twice).
- `./tbook build slides --book chen-chen-step-m-eulerian-parity-positivity`
  exits 1 before Tectonic compilation because its evidence-policy check fails.
  Tectonic 0.16.9 is available, but the upgraded paper deck is not verified.
- `./tbook build site --book chen-chen-step-m-eulerian-parity-positivity`
  exits 1 with one reported problem, the same deck failure. It assembles partial
  output but does not complete the Mathesis post-build hook/materials manifest.
- Fresh Chinese and English HTML builds pass with mdBook 0.5.4.

## Visual review

The fresh reader pages were served with `./tbook serve` and inspected in Chinese
and English, light and dark themes, at 390 px and 1280 px. All eight browser
checks show the written-proof badge, the recorded DOI link and no page-wide
horizontal overflow. Screenshots remain under the task's temporary directory;
`reader-browser-qa.json` records the checks.

Because the upgraded deck cannot pass validation, the requested PNG inspection
uses the surviving previous deck, not a newly built 0.8.2 deck. Its SHA-256 is
`a873d66fbeee7c9cb66d5944d70cf6ff972fb69cbf60d4ef95090244f89a01e5`.
Page 4 (main theorem) and page 20 (ledger) were rendered with Poppler at 150 dpi
and visually inspected. The theorem is readable with a purple WRITTEN PROOF
badge, and the ledger has eight written-proof rows with no GIDs. These images
cannot establish the layout of the new DOI/source/request ledger.

## Execution scope

Python 3.12.13 and pinned project requirements are installed in the paper's
local `.venv`; npm dependencies and its cache are local. mdBook 0.5.4, Java
21.0.13, Bash 5.3 and a fresh Playwright Chromium 141.0.7390.37 headless shell
were prepared under the temporary task directory. Node 26.3.0 is the existing
Homebrew executable. The pre-existing Playwright browser copy was incomplete;
the fresh pinned shell passes the film checks. The macOS system Bash lacks
`mapfile`; the temporary Bash passes both workflow tests. No shared CI or global
installation was changed. Doctor reports no required dependency missing; the
optional Noto CJK SC font remains unavailable.

All network reads were anonymous. Git credential helpers, extra authorization
headers and prompts were disabled for public fetches; token environment variables
were unset for checks. No push, remote mutation, `gh` or `nyxid` command was used.
PID 764 was not modified. The local preview server and obsolete temporary
browser installer were stopped after use.

Temporary evidence directory: `/var/folders/jd/5x6vvk8d4yzcmtmp7mjw_9nw0000gn/T/mathesis-v082-fqjv1qhi`.

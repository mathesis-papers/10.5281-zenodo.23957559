# Recorded validation and build commands

The later layer 0.3.1 CI repair has its own command/results record in
[POST-BUILD-FIX.md](POST-BUILD-FIX.md) and
[validation/post-build-fix/](validation/post-build-fix/). The table below records
the original paper preparation.

Working directory: `/Users/lexa/Desktop/lexa/omega/mathesis-paper-chen-chen`. Each command was invoked through
`python3 docs/project/run-command.py <log-label> <command...>`; the table shows
the exact child arguments. Commands use the recorded existing Chrome and Tectonic,
repository-local caches and the task temporary directory. No credentials were
passed. Exit codes below are actual, including superseded failures.

| # | Child command | Exit | Log |
|---|---|---:|---|
| 1 | `python3 docs/layer-mathesis/scripts/paper.py fill --input /Users/lexa/Desktop/lexa/omega/mathesis-evidence/2026-11-12-catalog-dry-run/output/papers/chen-chen-step-m-eulerian-parity-positivity --slug chen-chen-step-m-eulerian-parity-positivity --title-zh 'Chen 和 Chen 的奇偶正性猜想的证明：OEIS A392664–A392666 的 COMMENTS 及猜想 2（第 1 页）' --title-en 'Proof of Chen and Chen'"'"'s parity-positivity conjectures: OEIS A392664–A392666, COMMENTS, and Conjecture 2 (p. 1)' --repository mathesis-papers/chen-chen-step-m-eulerian-parity-positivity` | 0 | [fill.txt](validation/fill.txt) |
| 2 | `./tbook pin 2a8e85703420116c8f07e1eebebd34fa221c8d55` | 0 | [pin.txt](validation/pin.txt) |
| 3 | `python3 docs/project/prepare-reading.py` | 0 | [prepare-reading.txt](validation/prepare-reading.txt) |
| 4 | `python3 docs/layer-mathesis/scripts/paper.py check --complete` | 0 | [check-reading.txt](validation/check-reading.txt) |
| 5 | `./tbook check --offline` | 0 | [check-book.txt](validation/check-book.txt) |
| 6 | `./tbook template update --layer upstream --source /Users/lexa/Desktop/lexa/omega/mathesis-paper-template-combined --to main` | 0 | [integrate-upstream.txt](validation/integrate-upstream.txt) |
| 7 | `./tbook template update --layer mathesis --source /Users/lexa/Desktop/lexa/omega/mathesis-paper-template --to main` | 0 | [integrate-layer.txt](validation/integrate-layer.txt) |
| 8 | `node tools/node/viz-thumbs.mjs chen-chen-step-m-eulerian-parity-positivity step-triangle` | 0 | [viz-thumbnails.txt](validation/viz-thumbnails.txt) |
| 9 | `./tbook slides snapshots chen-chen-step-m-eulerian-parity-positivity` | 0 | [academic-snapshots.txt](validation/academic-snapshots.txt) |
| 10 | `./tbook check --offline` | 0 | [check-media.txt](validation/check-media.txt) |
| 11 | `node tools/node/viz-shots.mjs chen-chen-step-m-eulerian-parity-positivity step-triangle` | 0 | [viz-shots.txt](validation/viz-shots.txt) |
| 12 | `node tools/node/viz-test.mjs chen-chen-step-m-eulerian-parity-positivity` | 0 | [viz-tests.txt](validation/viz-tests.txt) |
| 13 | `python3 docs/project/audit-reading.py` | 0 | [reading-fidelity.txt](validation/reading-fidelity.txt) |
| 14 | `node tools/node/viz-validate.mjs chen-chen-step-m-eulerian-parity-positivity` | 0 | [viz-validate.txt](validation/viz-validate.txt) |
| 15 | `python3 docs/layer-mathesis/scripts/paper.py check --complete` | 0 | [complete-check.txt](validation/complete-check.txt) |
| 16 | `./tbook check` | 0 | [final-book-check.txt](validation/final-book-check.txt) |
| 17 | `./tbook doctor` | 1 | [doctor.txt](validation/doctor.txt) |
| 18 | `./tbook build html pdf epub viz --book chen-chen-step-m-eulerian-parity-positivity` | 1 | [build-reader-formats.txt](validation/build-reader-formats.txt) |
| 19 | `node tools/node/viz-test.mjs chen-chen-step-m-eulerian-parity-positivity --slow` | 0 | [viz-tests-slow.txt](validation/viz-tests-slow.txt) |
| 20 | `python3 manuscript/verify.py` | 0 | [manuscript-finite-check.txt](validation/manuscript-finite-check.txt) |
| 21 | `./tbook build slides --book chen-chen-step-m-eulerian-parity-positivity` | 1 | [build-slides.txt](validation/build-slides.txt) |
| 22 | `env TBOOK_CACHE=0 ./tbook build slides --book chen-chen-step-m-eulerian-parity-positivity` | 0 | [build-slides-corrected.txt](validation/build-slides-corrected.txt) |
| 23 | `env TBOOK_CACHE=0 ./tbook build slides --book chen-chen-step-m-eulerian-parity-positivity` | 0 | [build-slides-layout.txt](validation/build-slides-layout.txt) |
| 24 | `./tbook template update --layer mathesis --source /Users/lexa/Desktop/lexa/omega/mathesis-paper-template --to main` | 0 | [refresh-layer-final.txt](validation/refresh-layer-final.txt) |
| 25 | `env TBOOK_CACHE=0 ./tbook build slides --book chen-chen-step-m-eulerian-parity-positivity` | 0 | [build-slides-repeat.txt](validation/build-slides-repeat.txt) |
| 26 | `python3 docs/project/review-deck.py` | 0 | [deck-pdf-qa.txt](validation/deck-pdf-qa.txt) |
| 27 | `./tbook template manifest --layer mathesis --check` | 0 | [mathesis-manifest-final.txt](validation/mathesis-manifest-final.txt) |
| 28 | `./tbook template manifest --check` | 0 | [upstream-manifest-final.txt](validation/upstream-manifest-final.txt) |
| 29 | `python3 docs/layer-mathesis/scripts/paper.py check --complete` | 0 | [complete-check-final.txt](validation/complete-check-final.txt) |
| 30 | `./tbook check` | 0 | [book-check-final.txt](validation/book-check-final.txt) |
| 31 | `./tbook build site --book chen-chen-step-m-eulerian-parity-positivity` | 0 | [build-site-final.txt](validation/build-site-final.txt) |
| 32 | `python3 docs/project/audit-site.py` | 0 | [site-media-qa.txt](validation/site-media-qa.txt) |

The JSONL also retains UTC start/end timestamps. Direct Git integration, source
reads, scaffold generation, initial manifest regeneration and visual inspection
are described in the handoff; they are not claimed to be part of this command
runner transcript. PDF inspection subcommands appear in `deck-pdf-qa.txt` where
applicable. The final git diff checks and repository-state verification are
retained in the handoff state evidence.

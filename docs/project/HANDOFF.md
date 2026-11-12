# Chen–Chen paper repository handoff

Prepared locally on 2026-11-13. No push, repository creation, PR, authenticated
request, `gh` or `nyxid` operation was performed. The user’s MongoDB process was
not touched. The repository is on `main` with no remotes. It has a fresh root
commit `f5f701fdea489d4123d50e385e83b806e65e8d5f`, made from the combined
template using `git archive` and `git init -b main`, followed by paper work.
Commits use the global Git identity AlyciaBHZ
`<50111876+AlyciaBHZ@users.noreply.github.com>`.

## Frozen paper and reading

Selected catalog work: `chen-chen-step-m-eulerian-parity-positivity`, version 2,
CC-BY-4.0, recorded authors Haobo Ma then Wenlin Zhang. The exact recorded
English title is unchanged. Chinese title:
“Chen 和 Chen 的奇偶正性猜想的证明：OEIS A392664–A392666 的 COMMENTS 及猜想 2（第 1 页）”.

`paper.py fill` imported all 16 generated files and the generated manifest
byte-for-byte from the supplied catalog projection. Complete checks continue
to verify every hash. No catalog receipt, node, manuscript, frozen PDF or
verification status was edited. The input projection, earlier pilot and Lean
checkout remained read-only. Nothing was installed globally.

The book has aligned Chinese and English opening pages, six explanatory
chapters, references and provenance. It introduces the recurrence and sign
mechanism for undergraduate readers, gives every exact formal statement and
all eight full written proofs, then separates the source's conclusions,
counterexamples and uncovered assertions. The first page of each edition says
that Mathesis prepared it from the manuscript, the authors did not review it,
and explanations are not verification. No nonexistent public Mathesis
explanation sidecar was fabricated: the owner's explicit manuscript-only
instruction governs this conversion while the CMA job is blocked.

The faithful pilot transcription was reused only after source checks. The
audit confirms eight English statement/prose/math matches to nodes, eight
Chinese statement math-multiset matches, and eight complete English proof
prose/math matches to the frozen TeX. Chinese proofs were translated and
manually reviewed; automated prose equivalence is not claimed. See
[STATEMENT-REVIEW.md](STATEMENT-REVIEW.md) and
[evidence/reading-audit.json](evidence/reading-audit.json).

## Every catalog node

All node identities have prefix
`collected:chen-chen-step-m-eulerian-parity-positivity:2:`.
Every row has a nonempty associated proof in both editions, `gids = []`, and
comparison commit `2a8e85703420116c8f07e1eebebd34fa221c8d55`.

| Node | Book id | Status | Verdict |
|---|---|---|---|
| s1 | paper-thm-main | written-proof | special case |
| s2 | paper-lem-second | written-proof | special case |
| s3 | paper-cor-classification | written-proof | variant |
| s4 | paper-cor-sums | written-proof | none |
| s5 | paper-cor-annulus | written-proof | none |
| s6 | paper-cor-odd | written-proof | none |
| s7 | paper-thm-growth | written-proof | none |
| s8 | paper-cor-boundaryroots | written-proof | none |

The source and frozen state were read at the actual pin with `git show` and
their inspected bytes are retained in `evidence/`. Twelve frozen theorems
include two public and ten private/generated entries. The nearby public
`D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive`
states integer-parameter even-row positivity. It does not state the complete
real-parameter main theorem, odd interior signs, full integer iff
classification, or the other five composite results. Thus it is comparison
context only for s1–s3. No complete result received a `lean=` citation; no
result was narrowed to obtain one. All eight nodes are mapped, none pending,
and `.mathesis/book.json` has stage complete.

No Lean compilation was run. The inspected module header records an unresolved
escape-audit annotation for issue #24785; this conversion does not resolve it.
The broader digest keyword search and its limits are documented in the review.

## Interactive visualization

`books/chen-chen-step-m-eulerian-parity-positivity/viz/step-triangle/` uses the
unmodified shared runtime. It shows ten triangle rows with sign colors, a step
slider, row timeline, selectable cells, sign counts and an evidence drawer.
Four independently referenced cards illustrate an even row at step -3, an
odd row at step -3, excluded step -1, and Pascal step 0. Both language editions
embed the corresponding cards. Each page identifies finite calculations as
illustrations, with NUM/ARGUED evidence, never formal verification.

The independent test oracle enumerates lattice paths, rather than copying
the page's row-array recurrence. Checks cover ten parameters through ten rows,
Pascal/binomial values, signs, excluded steps, controls, pointer and keyboard
interaction, speed and every bilingual card still. Results: **136/136** in
normal mode and **136/136** at 1000 ms/frame. Registry validation: 1 live page,
0 errors, 0 warnings. All seven desktop, embedded, phone and cover screenshots
were visually inspected, as were the eight bilingual stills. The retained
contact sheet is [evidence/viz-stills-reviewed.jpg](evidence/viz-stills-reviewed.jpg).
No separate static figure duplicates this same object; card stills and the
paper snapshot supply the static rendition.

## Seminar deck

English, original `TBookAcademic` Beamer theme, 4:3, approximately 25 minutes.
Nineteen main frames plus the generated eight-result ledger give **20 audience
pages**. All 19 speaker notes remain in the **39-page notes PDF**. Every result
is cited through `bookresult`; the source uses `BookViz`, `PinnedCommit` and
`FormalVerification`. Haobo's affiliation is Chrono AI, Singapore; Wenlin's are
Chrono AI and NUS, Singapore. The deck does not claim either author delivered it.
There is no Slidev deck.

Durable deliverables:

- [Audience PDF](artifacts/seminar-en.pdf), 247,562 bytes,
  SHA-256 `0679bbfb6fe955ae69b7f47c69145392d807b691bdcd550b9d3e6afb4c765bd2`.
- [Speaker-notes PDF](artifacts/seminar-en-notes.pdf), 264,252 bytes,
  SHA-256 `56b4e882360725fc268b08bb90fc17fca5cfda204569a5c5d0e5d250f3cc2cdd`.

Two uncached Tectonic 0.16.9 builds using the upstream versioned bundle and
deterministic mode produced byte-identical PDFs. The initial notes failure
(unescaped math underscores) was corrected. A first title-page render exposed
an overlap; its notice spacing and short section-navigation labels were fixed.

Final audience pages **1, 4, 5 and 20** were rendered with Poppler under
`/var/folders/jd/5x6vvk8d4yzcmtmp7mjw_9nw0000gn/T/mathesis-chen-chen.YqWUyy/deck-review/`
and looked at: readable title/affiliations/notice, theorem and purple badge,
the 3200×1800 triangle still with illustration caption, and all eight ledger
rows with the source pin. The outline (page 2) and a notes page were also
rendered and inspected. Audience text contains no timing notes; all 19 notes
were found in the notes PDF.

The logs still contain nullfont digit warnings and eight 0.82 pt ledger hbox
warnings per PDF. Inspected pages show no missing visible text or clipping;
this is not a claim that the TeX log is warning-free. Details and render paths
are in [evidence/deck-qa.json](evidence/deck-qa.json), with build logs retained.

The combined template's extra academic/written-proof compatibility commit
`690ec33` is required for this deck. Merging unmodified PR #48/#50/#51 heads
alone does not include it. Preserve it in upstream integration before a future
ordinary template update. This is also recorded in the layer-managed pin note.

## Commands and local build limits

[COMMANDS.md](COMMANDS.md) lists every recorded validation/build command with its
actual exit code and log, including failed attempts and retries. Exact argv and
timestamps are in [validation/commands.jsonl](validation/commands.jsonl).
Readable task logs have trailing whitespace and blank EOF normalized for Git;
`evidence/log-normalization.json` lists them. Catalog/frozen files are untouched.

| Final command/check | Actual result |
|---|---|
| `paper.py check --complete` | exit 0; 16 hashes OK, 8 mapped, 0 pending, complete |
| `./tbook check` | exit 0; 1 visible book, 0 errors, 0 warnings |
| Upstream / layer manifest checks | exit 0; 0.7.0 / 0.2.1 current |
| `audit-reading.py` | exit 0; fidelity checks and both Python-rendered intermediates/ledgers |
| Viz tests, normal and slow | exit 0 each; 136/136 each |
| Viz thumbnails, academic snapshots, screenshots, validation | exit 0 each |
| `python3 manuscript/verify.py` | exit 0; all assertions passed; JSON equals archived finite-check JSON |
| `./tbook doctor` | exit 1; missing mdBook, pypandoc/Pandoc and Typst; EPUB validation/Java also unavailable |
| `./tbook build html pdf epub viz --book …` | exit 1 overall; HTML needs mdBook, academic book PDF needs Pandoc, EPUB cover needs Typst; viz/site shell generated |
| Final `TBOOK_CACHE=0 ./tbook build slides --book …`, twice | exit 0 each; both PDFs identical |
| `review-deck.py` | exit 0; counts, geometry, notes, ledger, identity and PNG renders pass |
| `./tbook build site --book …` | exit 0; CSS cover fallback because Typst is absent |
| `audit-site.py` | exit 0; both PDF hashes/links, viz, pin and base URL agree |

The site uses the requested Pages base URL and has the future custom domain
commented in `site.toml`. The builder keeps the book under its normal nested
slug path beneath that base. `_site/manifest.json` records zero exact Lean
citations, one visualization and one academic deck, both downloadable PDFs,
and `html: null` for each unbuilt reading edition. The landing lists eight
written proofs in each language. `_site` is a partial local site, not a complete
reader build or a deployment.

The source finite checker replay matches its archived JSON exactly. Its finite
integer/rational/congruence/root checks are evidence of those calculations,
not an all-row Lean proof or an independent proof of every theorem.

## Still for CI and review

- Build both mdBook reading editions, academic book PDFs with Pandoc/Typst,
  EPUBs and covers, then run EPUB/Java validation and full bilingual reader
  review at desktop/phone widths and both themes. Only Python intermediates
  were available locally; no completed book PDF/EPUB is claimed.
- Confirm the combined upstream suite's three unresolved tests and skipped
  tool-dependent cases in the intended CI toolchain. Its final full run had
  1,032 tests, 934 passed, 95 skipped and three failures (film pixel identity;
  two macOS Bash `mapfile` failures). See the combined integration handoff.
- Mathematical comparison and transcription were reviewed against frozen
  sources; no Lean build, new receipt/status, author review, or comprehensive
  independent bibliography verification is claimed. All original bibliography
  entries were retained without inventing new citations.
- Dispatcher performs all GitHub writes and publication. No local task result
  changes the centrally managed formalization pool or its verification status.

## Local cleanup and regeneration

After all jobs exited, the task-only shared Node installation, paper dependency
symlink, npm cache and obsolete test temporary files were removed. Open-file
checks found no active users of those paths. Allocated space reclaimed:
886,688 KiB (865.9 MiB), measured with `du -sk`. All handoff sources, logs,
inspected frozen evidence, PDFs, stills, visualization screenshots and requested
temporary deck renders remain; the local Tectonic bundle cache is retained.
No shared cache or user service was touched. `evidence/cleanup.json` records
the exact paths and measurements. Rerun the recorded local `npm ci` before
browser-based checks; it does not download a browser.

`prepare-reading.py` and `prepare-viz.py` are historical one-time import helpers,
not safe regeneration commands: they would overwrite later editorial/media
changes and the former reads the external pilot. Normal validation is through
the self-contained audits, layer checker and upstream CLI.

# Sources and provenance

The publisher imported the catalog projection byte-for-byte. Its generated hashes are checked by the Mathesis adapter; those files remain authoritative for identity and source content.

- `paper.json` (Recorded paper metadata), `formalization/nodes.json` (catalog nodes), `CITATION.cff` (citation metadata).
- `paper.pdf` (Frozen paper PDF).
- Frozen TeX: `manuscript/note.tex` (main article), `manuscript/companion-results.tex` (companion results), `manuscript/coverage.tex` (coverage).
- `manuscript/source-guide.md` (Source guide), `manuscript/README.md` (companion README), `manuscript/metadata.json` (manuscript metadata).
- `manuscript/verify.py` (Exact finite checker) and its `manuscript/finite-check.json` (recorded output). Finite checks are separate from all-row proofs.
- `.mathesis/book.json` (Versioned claim-to-book mapping) and `docs/project/STATEMENT-REVIEW.md` (statement comparison). The closest public GIDs in that comparison are not book citations.

The original source archive and fetch receipt remain in the supplied read-only snapshot. The projection contains the unpacked source files: its archive hash is not a hash of a directory. The archived article DOI identifies the original article, not a newly rendered reading or seminar deck.

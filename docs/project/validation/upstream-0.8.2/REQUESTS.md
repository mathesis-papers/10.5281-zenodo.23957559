# Missing formalization-request registrations

The eight written results already have nonempty proofs in both editions.
Upstream 0.8.2 additionally requires a real shared-queue issue and registration.
An anonymous read of the public queue found only the unrelated issue #1.
No requests were created or registered during this local work package.

Source DOI: `10.5281/zenodo.23957560` (recorded version 2).
The source locations below were checked against the frozen TeX labels.

| Result | Source location | Required registration marker |
| --- | --- | --- |
| `paper-thm-main` | Theorem 1 (thm:main) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-thm-main -->` |
| `paper-lem-second` | Lemma 2 (lem:second) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-lem-second -->` |
| `paper-cor-classification` | Corollary 3 (cor:classification) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-cor-classification -->` |
| `paper-cor-sums` | Corollary 4 (cor:sums) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-cor-sums -->` |
| `paper-cor-annulus` | Corollary 5 (cor:annulus) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-cor-annulus -->` |
| `paper-cor-odd` | Corollary 6 (cor:odd) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-cor-odd -->` |
| `paper-thm-growth` | Theorem 7 (thm:growth) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-thm-growth -->` |
| `paper-cor-boundaryroots` | Corollary 8 (cor:boundaryroots) | `<!-- tbook:mathesis-papers/chen-chen-step-m-eulerian-parity-positivity:chen-chen-step-m-eulerian-parity-positivity:paper-cor-boundaryroots -->` |

`missing-requests.json` is the unmodified output of `./tbook requests --json`,
including suggested upstream-format titles. After a real issue exists, its body
or a comment must include the marker and `DOI:<bare DOI> | <source location>`.
Reuse one request for multiple uses only when it states the same mathematical
result. Add the verified URL as `request` in both editions, then rerun the layer
check, `./tbook check`, Tectonic deck build and site build.

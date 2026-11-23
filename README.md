# Proof of Chen and Chen's parity-positivity conjectures: OEIS A392664–A392666, COMMENTS, and Conjecture 2 (p. 1)

**Authors:** Haobo Ma, Wenlin Zhang

We prove Conjecture 2 on page 1 of Chen and Chen's January 2026 executive summary and the parity-positivity conjectures in OEIS A392664–A392666, COMMENTS: every positive even row is strictly positive for real m <= -3. We also prove the odd-row alternating-sum nonvanishing assertions at m = -4 and -5. The largest root modulus satisfies M_n(-3) ~ 5^(n/2)/sqrt(45), correcting the stated exponent log(2) to log(5)/2 and the proposed scaling constant 1/3. The constants 1/6 and 1/10 at steps -4 and -5 are proved. Companion identities, the integer-step sign classification and boundary cases have written proofs.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23957560](https://doi.org/10.5281/zenodo.23957560)
- Concept DOI: [https://doi.org/10.5281/zenodo.23957559](https://doi.org/10.5281/zenodo.23957559)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [chen-chen-step-m-eulerian-parity-positivity](https://mathesis-omega-research.apps.chrono-ai.fun/papers/chen-chen-step-m-eulerian-parity-positivity?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Proof of Chen and Chen's parity-positivity conjectures: OEIS A392664–A392666, COMMENTS, and Conjecture 2 (p. 1). Mathesis, version 2. https://doi.org/10.5281/zenodo.23957560

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Theorem (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23957559/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23957559/chen-chen-step-m-eulerian-parity-positivity/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23957559/chen-chen-step-m-eulerian-parity-positivity/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23957559/chen-chen-step-m-eulerian-parity-positivity/slides/) ([sources](books/chen-chen-step-m-eulerian-parity-positivity/slides/)) · [Visualizations](https://papers.trureturing.org/10.5281-zenodo.23957559/chen-chen-step-m-eulerian-parity-positivity/viz/) ([sources](books/chen-chen-step-m-eulerian-parity-positivity/viz/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23957559/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `paper-thm-main` | special case | `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive` |
| `paper-lem-second` | special case | `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive` |
| `paper-cor-classification` | variant | `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive` |
| `paper-cor-sums` | none | — |
| `paper-cor-annulus` | none | — |
| `paper-cor-odd` | none | — |
| `paper-thm-growth` | none | — |
| `paper-cor-boundaryroots` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/chen-chen-step-m-eulerian-parity-positivity/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.

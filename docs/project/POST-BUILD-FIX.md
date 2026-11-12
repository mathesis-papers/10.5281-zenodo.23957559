# Mathesis 0.3.1 post-build CI fix

Prepared locally on 2026-11-13 from paper `main` at
`fd35740b6583576939960be68ce4a74edb765a93`. The new consumer branch is
`fix/mathesis-post-build-fixtures-20261113`. No push, authenticated external
request, repository creation, PR or global installation was performed.

## Cause and change

The inherited template suite builds foreign books and empty repositories while
retaining the paper's `site.toml`. The old postprocessor selected the repository
from its script path and always enforced single-paper policy. Copies without the
layer script failed before entering Python (`exit 2`).

Layer 0.3.1 adds a standard-library bootstrap that first checks for the layer
script relative to the repository being built. `scripts/site.py` reads that
repository through the hook's working directory. Missing local script, missing
`.mathesis/book.json`, and an assembled manifest without the mapped book each
print one `Mathesis post-build skipped: ...` line and leave every output byte
unchanged. The `emit` function is unchanged from paper `main`, verified by AST
comparison. Once the mapped book is present, malformed data, extra books,
identity mismatches, unsafe paths and a missing book landing still fail.

`site-hook.json` is the canonical command shared by `fill`, the checker and the
idempotent `v0.3.1.py` migration. The migration replaces the legacy declaration
and preserves unrelated settings; it refuses to overwrite custom hook commands.
Both layers were applied with `./tbook template update`, without editing managed
consumer files directly.

One separate upstream fixture correction was unavoidable. The film sandbox's
cached `config.load_site()` could retain a `Site.root` from a removed temporary
directory. No command could start with that cwd, so a layer guard could not
handle it. Upstream `7eb37dae97c276c656400e4ddc32dc8feec6e9e3` sets
`root=self.root` in that fixture and refreshes its manifest. The production hook
and its error handling are unchanged. The combined template includes this
correction and layer 0.3.1 at `22894117c07f3ddd042739e6011254af84afa0f5`.
The layer source is `a75e7702ded7cfff56bb76abe3c4262f6afaaee7`.

## Validation

Logs are retained in [validation/post-build-fix/](validation/post-build-fix/).
Full suite commands unset `GITHUB_TOKEN`, `GH_TOKEN` and `TRURETURING_TOKEN`.
The final run also selects Python 3.12 for CLI/hook subprocesses:

```sh
env -u GITHUB_TOKEN -u GH_TOKEN -u TRURETURING_TOKEN \
  PATH="/opt/homebrew/opt/python@3.12/libexec/bin:$PATH" \
  TBOOK_PYTHON=python3.12 PYTHONPATH=tools \
  python3.12 -m unittest discover -s tools/tests
```

| Check | Result |
|---|---|
| Original full template suite, local default Python 3.15 | 1,027 tests: 15 errors, 3 failures, 186 skipped |
| Original site module, Python 3.12 | 49 tests: 14 hook errors, 8 skipped |
| Layer guards without upstream fixture correction, Python 3.12 | 1,027 tests: 1 stale-cwd error, 2 Bash failures, 186 skipped |
| Final full template suite, Python 3.12 | 1,027 tests: 839 passed, 186 skipped, 2 known Bash failures; zero errors |
| Layer suite, source and consumer, Python 3.12 | 21 passed in each |
| Upstream film suite | 93 passed |
| Upstream hook contract suite | 3 passed |
| Catalog publisher, including actual SDK/`fill` integration against loopback fixtures | 7 passed |
| Workflow YAML, pins, permissions and shell syntax fallback | passed |
| `paper.py check --complete` | 16 generated hashes OK; 8 mapped results; 0 pending; complete |
| `./tbook check` | 1 book; 0 errors; 0 warnings |
| Upstream / layer manifest checks | current: 0.7.0 / 0.3.1 |
| Site build and `audit-site.py` | passed: root redirect, nested landing, materials, visualization and both slide PDFs |

The two remaining failures are
`test_release_attaches_the_build_cache_and_publishes_a_complete_draft` and
`test_template_release_attaches_the_example_site_cache`: macOS Bash reports
`mapfile: command not found`. No publication workflow was changed for them.
Skip tests cover absent script/mapping/mapped book, execution of an external
script against cwd, byte-for-byte output preservation, strict real-paper
failures, new fills and migration behavior.

The local site still has no built HTML reading editions, uses the existing CSS
cover fallback because Typst is unavailable, and advertises one English slide
edition plus one visualization. No new reading build, browser visual review,
Linux/GitHub CI run or deployment is claimed. The root redirect and material
emission policy did not change. Frozen paper/manuscript bytes and mathematical
content were not edited.

The unpushed catalog publisher pins the fixed combined template. The dispatcher
must publish the upstream fixture correction, layer and combined template
dependencies before the paper and catalog branches. A squash or rebase requires
updating the catalog's `template_commit` to the actual reachable combined head.

After publisher validation, its task-only offline Cargo build directory was
checked for active file users and removed. This reclaimed 475,708 KiB
(464.6 MiB); source commits and logs remain. The named checkouts are retained
because these local changes have not been pushed. No user service was touched.

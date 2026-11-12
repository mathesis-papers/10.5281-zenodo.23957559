#!/usr/bin/env python3
"""Inspect real PDFs with Poppler, compare uncached builds, retain handoff PDFs."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess

root = Path(__file__).resolve().parents[2]
slug = 'chen-chen-step-m-eulerian-parity-positivity'
pdfs = root / 'build/slides' / slug
evidence = root / 'docs/project/evidence'
artifacts = root / 'docs/project/artifacts'
artifacts.mkdir(exist_ok=True)
render = Path(os.environ['TMPDIR']) / 'deck-review'
render.mkdir(exist_ok=True)

def run(*args):
    print('COMMAND:', ' '.join(map(str, args)), flush=True)
    return subprocess.check_output(list(map(str, args)), text=True)

baseline = json.loads((evidence / 'deck-first-build.json').read_text())
report = {'pdfs': {}, 'render_directory': str(render), 'renders': []}
texts = {}
for kind, filename, count in (
    ('audience', 'seminar-en.pdf', 20),
    ('notes', 'seminar-en-notes.pdf', 39),
):
    pdf = pdfs / filename
    info = run('pdfinfo', pdf)
    assert int(re.search(r'^Pages:\s+(\d+)', info, re.M)[1]) == count
    size = re.search(r'^Page size:\s+([\d.]+) x ([\d.]+)', info, re.M)
    width, height = map(float, size.groups())
    assert abs(width / height - 4 / 3) < .001
    text = run('pdftotext', '-layout', pdf, '-')
    texts[kind] = text
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert baseline[filename] == digest, f'{filename}: uncached builds differ'
    shutil.copy2(pdf, artifacts / filename)
    (evidence / f'deck-{kind}.txt').write_text(text)
    (evidence / f'deck-{kind}-pdfinfo.txt').write_text(info)
    report['pdfs'][kind] = dict(filename=filename, sha256=digest, bytes=pdf.stat().st_size,
        pages=count, width_pt=width, height_pt=height, uncached_builds_identical=True)

assert 'Timing:' not in texts['audience']
assert texts['notes'].count('Timing:') == 19
ledger = texts['audience'].split('\f')[-2]
assert ledger.count('WRITTEN PROOF') == 8
assert ledger.count('No GID (written proof)') == 8
assert '2a8e85703420' in ledger
report['audience_hides_notes'] = True
report['notes_retained'] = 19
report['ledger_written_proof_rows'] = 8

for kind, pages in [('audience', [1, 2, 4, 5, 20]), ('notes', [2])]:
    filename = report['pdfs'][kind]['filename']
    for page in pages:
        target = render / f'{kind}-{page}'
        run('pdftoppm', '-f', page, '-l', page, '-scale-to', 1600, '-png', '-singlefile',
            pdfs / filename, target)
        report['renders'].append(str(target.with_suffix('.png')))

stage = root / 'build/stage' / slug / 'beamer/seminar/en'
for kind in ('audience', 'notes'):
    shutil.copy2(stage / f'{kind}-build.log', evidence / f'deck-{kind}-build.log')
    warnings = [line for line in (stage / f'{kind}.log').read_text().splitlines()
                if 'Missing character:' in line or 'Overfull' in line]
    report['pdfs'][kind]['tex_warnings'] = warnings
(evidence / 'deck-qa.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k != 'pdfs'}, indent=2))
print('PDF counts, 4:3 geometry, notes, ledger and byte identity: PASS')

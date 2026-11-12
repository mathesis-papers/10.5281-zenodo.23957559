#!/usr/bin/env python3
"""Check the built local site manifest and media links without network access."""
from pathlib import Path
import hashlib
import json
import re

root = Path(__file__).resolve().parents[2]
site = root / '_site'
slug = 'chen-chen-step-m-eulerian-parity-positivity'
data = json.loads((site / 'manifest.json').read_text())
assert data['site']['base_url'] == f'https://papers.trureturing.org/{slug}/'
assert data['trureturing']['commit'] == '2a8e85703420116c8f07e1eebebd34fa221c8d55'
assert len(data['books']) == 1
book = data['books'][0]
assert book['slug'] == slug and book['verified'] == 0 and book['open'] == 0
assert book['media']['viz'] == ['step-triangle']
assert book['media']['slides'] == ['seminar']
assert len(book['files']) == 2
for item in book['files']:
    file = site / item['path']
    assert len(file.read_bytes()) == item['size']
    assert hashlib.sha256(file.read_bytes()).hexdigest() == item['sha256']
landing = site / slug / 'slides/seminar/en/index.html'
for href in re.findall(r'href="([^"]+\.pdf)"', landing.read_text()):
    assert (landing.parent / href).is_file(), href
assert (site / slug / 'viz/step-triangle/index.html').is_file()
book_html = (site / slug / 'index.html').read_text()
assert book_html.count('class="k written-proof"') == 16  # eight per language
assert all(edition['html'] is None for edition in book['editions'])
materials = json.loads((site / 'mathesis-materials.json').read_text())
assert materials['schema'] == 'mathesis.materials.v1'
assert materials['work'] == slug and materials['version'] == 2
assert materials['site_url'] == data['site']['base_url']
assert materials['doi'] == json.loads((root / 'paper.json').read_text())['work']['doi']
assert materials['reading'] == {}
assert len(materials['slides']) == 1 and len(materials['visualizations']) == 1
assert materials['slides'][0]['id'] == 'seminar'
assert materials['slides'][0]['language'] == 'en'
for url in [materials['slides'][0]['pdf_url'], materials['slides'][0]['notes_url'], materials['visualizations'][0]['url']]:
    assert url.startswith(materials['site_url'])
    path = site / url.removeprefix(materials['site_url'])
    assert (path / 'index.html' if url.endswith('/') else path).is_file()
assert f'0;url={slug}/' in (site / 'index.html').read_text()
report = dict(base_url=data['site']['base_url'], visible_books=1,
    exact_lean_citations=0, written_proof_results_per_language=8,
    media=book['media'], pdf_files=book['files'],
    reader_html_built=False, cover='CSS fallback; Typst unavailable',
    local_pdf_links_resolve=True, root_redirect=slug + '/', materials=materials)
evidence = root / 'docs/project/evidence'
(evidence / 'site-manifest.json').write_text(json.dumps(data, indent=2) + '\n')
(evidence / 'site-qa.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))

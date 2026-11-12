"""Audit manuscript-to-book statement and proof fidelity without modifying catalog data."""
from pathlib import Path
from collections import Counter
import json,re,hashlib,unicodedata,sys
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'tools'))
from tbook import mathrender,config,model,lean,ledger,pandoc,render
B=ROOT/'books/chen-chen-step-m-eulerian-parity-positivity'
def nm(s):
 s=re.sub(r'\\label\{[^}]+\}','',s)
 s=re.sub(r'\\hbox\{(?:is an odd integer|是奇整数)\}','ODD-INTEGER',s)
 return re.sub(r'\s+','',s).replace('&','')
def sm(s):
 out=[]
 pattern=r'\$(.*?)\$|\\\[(.*?)\\\]|\\begin\{equation\}(.*?)\\end\{equation\}|\\begin\{align\}(.*?)\\end\{align\}'
 for m in re.finditer(pattern,s,re.S):
  if m[4] is not None:out.extend(nm(row) for row in re.split(r'\\\\\s*',m[4]) if row.strip())
  else:out.append(nm(next(x for x in m.groups() if x is not None)))
 return out
def bm(s):
 spans,issues=mathrender.find_math(s);assert not issues,issues
 return [nm(x.tex) for x in spans]
def prose(s,tex=False):
 if tex:
  s=re.sub(r'\$.*?\$|\\\[.*?\\\]|\\begin\{(?:equation|align)\}.*?\\end\{(?:equation|align)\}',' ',s,flags=re.S)
  s=re.sub(r'\\(?:eqref|ref|label)\{[^}]+\}',' ',s)
  s=re.sub(r'\\cite(?:\[([^]]*)\])?\{[^}]+\}',lambda m:m[1] or ' ',s).replace(r'\S','§')
  s=re.sub(r'\\(?:begin|end)\{enumerate\}|\\item',' ',s).replace(r'\"o','ö').replace(r"\'e",'é')
 else:
  spans,_=mathrender.find_math(s)
  for x in reversed(spans):s=s[:x.start]+' '+s[x.end:]
  s=re.sub(r'<a id="[^"]+"></a>|\*\*Equation \(\d+\)\.\*\*',' ',s)
  s=re.sub(r'\[[^\[\]]*\]\([^\s()]+\)',' ',s);s=re.sub(r'^\d+\. ','',s,flags=re.M)
 s=''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c))
 return re.findall(r'[A-Za-z]+|\d+',s)
nodes=json.loads((ROOT/'formalization/nodes.json').read_text())['nodes'];mapping=json.loads((ROOT/'.mathesis/book.json').read_text())
all_text={lang:'\n'.join(p.read_text() for p in sorted((B/lang).glob('ch*.md'))) for lang in ('zh','en')}
rows=[]
for node in nodes:
 ident=next(k for k,v in mapping['results'].items() if v['claim']==node['identity'])
 item={'claim':node['claim'],'book_id':ident,'statement_sha256':hashlib.sha256(node['statement'].encode()).hexdigest()}
 for lang in ('zh','en'):
  statement=re.search(r'::: \{\.(?:theorem|lemma|corollary) #'+ident+r' [^\n]*\}\n(.*?)\n:::',all_text[lang],re.S)[1]
  assert Counter(sm(node['statement']))==Counter(bm(statement)),(ident,lang,Counter(sm(node['statement']))-Counter(bm(statement)),Counter(bm(statement))-Counter(sm(node['statement'])))
  if lang=='en':assert prose(node['statement'],True)==prose(statement),(ident,'English statement prose differs')
  assert f'#pf-{ident}' in all_text[lang]
  item[lang+'_statement_body_sha256']=hashlib.sha256(statement.encode()).hexdigest()
 rows.append(item)
source=(ROOT/'manuscript/note.tex').read_text().replace(r'\input{companion-results}',(ROOT/'manuscript/companion-results.tex').read_text())
proofs=re.findall(r'\\begin\{proof\}(?:\[[^]]*\])?(.*?)\\end\{proof\}',source,re.S)
written=re.findall(r'::: \{\.proof [^\n]*\}\n(.*?)\n:::',all_text['en'],re.S)
assert len(proofs)==len(written)==8
for i,(a,b) in enumerate(zip(proofs,written)):
 b=re.sub(r'^\s*\*Written proof reproduced from Ma and Zhang, frozen manuscript version 2\.\*\s*','',b)
 assert sm(a)==bm(b),(i,'proof math differs')
 assert prose(a,True)==prose(b),(i,'proof prose differs')
# Derive lines and visibility from the actual frozen source and keys, never hand-copy line numbers.
source_text=(ROOT/'docs/project/evidence/compared-source.txt').read_text();state=json.loads((ROOT/'docs/project/evidence/frozen-state.json').read_text())
starts={m[1]:i for i,line in enumerate(source_text.splitlines(),1) if (m:=re.match(r'(?:private )?(?:theorem|def) ([A-Za-z_][A-Za-z_0-9]*)',line))}
decs=[]
for d in state['declarations']:
 name=lean.parse_name_key(d['declaration_name_key']);generated='triangle' in name and name[-1]!='triangle'
 decs.append({'name':lean.name_to_str(name),'kind':d['kind'],'private':lean.is_private(name),'line':None if generated else starts.get(str(name[-1])),'generated_from_line':starts['triangle'] if generated else None})
(ROOT/'docs/project/evidence/frozen-declarations.json').write_text(json.dumps(decs,indent=2)+'\n')
book=config.named_book(B.name);lock=lean.Lock.load();site=config.load_site()
for lang in book.languages:
 mdl=model.load_edition(book.edition(lang))
 assert len([e for e in mdl.all_envs() if e.status==model.WRITTEN_PROOF])==8
 assert not [e for e in mdl.all_envs() if e.lean]
 (ROOT/f'docs/project/evidence/ledger-{lang}.md').write_text(ledger.ledger_markdown(mdl,lock))
 # Use the upstream Python-only render/stage functions. They are intermediates, not reader/PDF builds.
 ctx=render.RenderContext(site,book,book.edition(lang),mdl,lock,'mdbook',env_href=render.mdbook_env_href(mdl))
 target=ROOT/'build/reading-intermediates'/lang;target.mkdir(parents=True,exist_ok=True)
 for doc in mdl.chapters:(target/doc.chapter.path).write_text(render.chapter_markdown(doc,ctx))
 assert not ctx.issues,ctx.issues
 stage=pandoc.stage(site,book,book.edition(lang),mdl,lock)
 assert not stage.warnings,stage.warnings
report={'statement_nodes':len(rows),'en_statement_prose_and_math_equal_to_catalog':8,'zh_statement_math_multisets_equal_to_catalog':8,'en_complete_proof_prose_and_math_equal_to_manuscript':8,'zh_proofs':'translated and manually reviewed; not an automated prose equivalence proof','public_frozen_theorems':sum(d['kind']=='theorem' and not d['private'] for d in decs),'frozen_theorems':sum(d['kind']=='theorem' for d in decs),'exact_lean_matches':0,'statements':rows,'rendering':'Python intermediates and both ledgers generated; not completed reader/PDF output'}
(ROOT/'docs/project/evidence/reading-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='statements'},ensure_ascii=False,indent=2))

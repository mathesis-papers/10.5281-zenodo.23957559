"""Historical one-time scaffold transform; rerunning overwrites later edits."""
from pathlib import Path
import re,json
b=Path('books/chen-chen-step-m-eulerian-parity-positivity');v=b/'viz/step-triangle'
s=(v/'index.html').read_text()
s=re.sub(r'<link rel="preconnect"[^>]+>\n','',s)
s=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]+>\n','',s)
start=s.index('<!-- A working');end=s.index('<div class="app',start);s=s[:start]+s[end:]
s=re.sub(r'<div class="tagline">.*?</div>', '<div class="tagline"><span class="zh">负权重也能让偶数行全为正</span><span class="en">Negative weights can still give positive even rows</span></div>',s,flags=re.S)
s=s.replace('id="pillAngle">θ','id="pillAngle">m').replace('<span class="zh">平方和</span><span class="en">SUM</span>','<span class="zh">当前行</span><span class="en">ROW</span>')
start=s.index('      <!-- one card');end=s.index('      <p class="note" id="presetNote">',start)
s=s[:start]+'''      <div class="presets cards" id="presets">
        <button class="preset" data-preset="even" aria-pressed="false"><span class="code">EVEN</span><span class="cn zh">−3：第 6 行</span><span class="cn en">−3: row 6</span></button>
        <button class="preset" data-preset="odd" aria-pressed="false"><span class="code">ODD</span><span class="cn zh">−3：第 5 行</span><span class="cn en">−3: row 5</span></button>
        <button class="preset" data-preset="excluded" aria-pressed="false"><span class="code">EXCLUDED</span><span class="cn zh">−1：第 4 行</span><span class="cn en">−1: row 4</span></button>
        <button class="preset" data-preset="pascal" aria-pressed="false"><span class="code">PASCAL</span><span class="cn zh">0：第 6 行</span><span class="cn en">0: row 6</span></button>
      </div>
''' + s[end:]
start=s.index('    <section class="panel sec">',s.index('id="presetNote"'));end=s.index('  </aside>',start)
s=s[:start]+'''    <section class="panel sec">
      <h2><span class="zh">步长</span><span class="en">Step</span><span class="aside">m</span></h2>
      <div class="field"><label for="step"><span class="zh">步长 m</span><span class="en">Step m</span><small class="zh">点击格子读取精确位置</small><small class="en">click a cell to read its position</small></label><output id="oStep" for="step">−3</output>
      <input type="range" id="step" min="-8" max="3" step="0.25" value="-3"></div>
    </section>
''' + s[end:]
s=s.replace('单位圆上的一点，它在横轴上的影子与它的高度','步长三角形，颜色区分正、负、零；点击格子查看数值').replace('A point on the unit circle, its shadow on the horizontal axis and its height','A step triangle: colours distinguish positive, negative and zero; click cells for values')
start=s.index('      <div class="hud-bl">');end=s.index('      <div class="toast"',start)
s=s[:start]+'''      <div class="hud-bl">
        <span><i class="sw cy"></i><span class="zh">正</span><span class="en">positive</span></span>
        <span><i class="sw mg"></i><span class="zh">负</span><span class="en">negative</span></span>
        <span><i class="sw" style="background:var(--dim)"></i><span class="zh">零</span><span class="en">zero</span></span>
        <span><i class="sw am"></i><span class="zh">当前项</span><span class="en">current cell</span></span>
      </div>
''' + s[end:]
s=s.replace('两个平方此消彼长','每行正负项数').replace('One square grows as the other shrinks','Positive and negative counts by row').replace('cos²θ 与 sin²θ 随角度的变化','各行正项与负项的个数').replace('cos²θ and sin²θ against the angle','Counts of positive and negative entries by row')
s=s.replace('cos² + sin²','T(n,k)').replace('影子² + 高度²','当前项').replace('shadow² + height²','Current cell').replace('影子 cos θ','当前行正项数').replace('shadow cos θ','Positive in row').replace('高度 sin θ','当前行负项数').replace('height sin θ','Negative in row')
start=s.index('      <!-- To cite');end=s.index('      <button class="chip" id="infoBtn">',start)
s=s[:start]+'''      <div class="lean argued"><span class="ok">ARGUED</span><span><span class="zh">手稿定理 1 与推论 3 的书面论证；本书未为这些完整陈述引用 Lean 定理。</span><span class="en">Written arguments of manuscript Theorem 1 and Corollary 3; no Lean theorem is cited for these complete statements.</span></span></div>
      <div class="lean num"><span class="ok">NUM</span><span><span class="zh">图示仅计算前 10 行，使用双精度；这是例示，不是证明。零值按实际计算结果判断。</span><span class="en">Only the first 10 rows are computed, in double precision: an illustration, not a proof. Zero means a computed zero.</span></span></div>
''' + s[end:]
s=s.replace('max="360" step="any" value="60" aria-label="角度" data-aria-en="Angle"','max="10" min="1" step="any" value="6" aria-label="当前行" data-aria-en="Current row"').replace('min="0" max="10" min="1"','min="1" max="10"')
s=s.replace('每次 15°','每次一行').replace('15° at a time','one row at a time')
start=s.index('    <div class="zh">',s.index('id="drawer"'));end=s.index('\n  </div>\n</div>',start)
s=s[:start]+'''    <div class="zh"><p class="lede">每个圆是三角形的一项。改变步长，或沿时间轴换行；点击圆读取该项。图中前 10 行是按原递推算出的例示，不是证明。</p><ol><li>依据：本书<a href="../../zh/ch01-recurrence.html#paper-thm-main" target="_top">定理 1</a>及<a href="../../zh/ch02-signs.html#paper-cor-classification" target="_top">推论 3</a>，均有手稿书面证明。</li><li>青色为正，品红为负，灰色为零。琥珀色只圈出当前项。圆大小不表示数值大小。</li><li>范围为 −8 ≤ m ≤ 3，按 0.25 步进；行号 1 到 10。有限图示不证明无限多行，也不覆盖复参数或根渐近。</li></ol></div>
    <div class="en"><p class="lede">Each circle is one triangle entry. Vary the step, scrub the row rail, or click a cell to read its value. These first 10 computed rows are an illustration, not a proof.</p><ol><li>Sources: <a href="../../en/ch01-recurrence.html#paper-thm-main" target="_top">Theorem 1</a> and <a href="../../en/ch02-signs.html#paper-cor-classification" target="_top">Corollary 3</a>, both with manuscript written proofs.</li><li>Cyan is positive, magenta negative, grey zero. Amber rings only the current cell. Circle size does not encode magnitude.</li><li>Steps range from −8 to 3 in increments of 0.25; rows from 1 to 10. A finite picture establishes neither infinitely many rows nor complex-parameter or root asymptotics.</li></ol></div>''' + s[end:]
(v/'index.html').write_text(s)
(v/'style.css').write_text('#cv { cursor: crosshair; touch-action: none; }\n')
p=b/'viz/visualizations.json';data=json.loads(p.read_text());d=data['visualizations'][0];d.update(status='live',summary='改变步长与行号，观察两行一步的符号传播及被排除的参数；有限图示不是证明。',summary_en='Vary step and row to inspect two-row sign propagation and excluded parameters; finite illustrations are not proofs.',tags=['递推','符号','三角形'],tags_en=['recurrence','signs','triangle'],theory=[{'label':'第 1–2 章：符号与整数分类','label_en':'Chapters 1–2: signs and integer classification','href':'../zh/ch02-signs.html','href_en':'../en/ch02-signs.html'}],lean=[]);p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

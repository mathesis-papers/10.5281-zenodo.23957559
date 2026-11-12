(() => {
  'use strict';
  const {kit, L}=TRV, P=TRV.palette, $=id=>document.getElementById(id);
  let m=-3, k=3, view;
  function triangle(step) {
    const rows=[[],[1]];
    for(let n=2;n<=10;n++) {
      const row=Array(n).fill(1);
      for(let j=2;j<n;j++) row[j-1]=(step*(n-j)+1)*rows[n-1][j-2]+(step*(j-1)+1)*rows[n-1][j-1];
      rows[n]=row;
    }
    return rows;
  }
  const position=(n,j)=>[j-(n+1)/2,11-n];
  const valueText=x=>Number.isInteger(x)?String(x):Number(x.toPrecision(10)).toString();
  function read() {
    const n=Math.max(1,Math.min(10,Math.round(clock.t))), rows=triangle(m);
    k=Math.min(n,Math.max(1,k));
    return {m,n,k,t:clock.t,value:rows[n][k-1],rows:rows.slice(1),positive:rows[n].filter(x=>x>0).length,negative:rows[n].filter(x=>x<0).length,playing:clock.playing,preset:cards.current};
  }
  function drawStage(s) {
    const g=kit.plot($('cv'),{x:[-5.4,5.4],y:[0,11.8],pad:[26,18,62,66]});view=g;
    // Cells carry signs; an amber ring marks only the selected entry.
    for(let n=1;n<=10;n++) for(let j=1;j<=n;j++) {
      const [x,y]=position(n,j), v=s.rows[n-1][j-1], role=v>0?P.cyan:v<0?P.magenta:P.dim;
      if(n===s.n&&j===s.k) g.dot(x,y,P.amber,TRV.thumbMode?16:12);
      g.dot(x,y,role,TRV.thumbMode?12:8.5);
      if(!TRV.thumbMode&&n===s.n) {
        g.line([[x-.08,y],[x+.08,y]],P.bg,{width:1.5});
        if(v>0)g.line([[x,y-.08],[x,y+.08]],P.bg,{width:1.5});
        if(v===0)g.dot(x,y,P.bg,2);
      }
    }
    if(!TRV.thumbMode)g.text(-5,11-s.n,`n=${s.n}`,P.amber,{size:12,align:'left'});
    $('hudBig').textContent=`m = ${kit.fix(m,2)} · n = ${s.n}`;
    $('hudSub').textContent=L('有限行的符号例示 · 点击格子','Signs in finitely many rows · click a cell');
  }
  function drawPlot(s) {
    const g=kit.plot($('plot'),{x:[1,10],y:[0,10.5],pad:[28,10,12,24]});
    g.axes({xTicks:[2,4,6,8,10],yTicks:[0,5,10]});
    g.line(s.rows.map((r,i)=>[i+1,r.filter(x=>x>0).length]),P.cyan,{width:2});
    g.line(s.rows.map((r,i)=>[i+1,r.filter(x=>x<0).length]),P.magenta,{width:2});
    g.vline(s.n,P.amber,{dash:[3,3]});
    $('plotMeta').textContent=L('项数，不是数值大小','Counts, not magnitudes');
  }
  function draw() {
    const s=read(); drawStage(s); drawPlot(s);
    $('roSum').textContent=`T(${s.n},${s.k}) = ${valueText(s.value)}`;
    $('roSumSub').textContent=L('点击其他格子查看','Click another cell to inspect');
    $('roCos').textContent=String(s.positive);$('roSin').textContent=String(s.negative);
    $('roNote').textContent=L('青色为正，品红为负；所有数值由递推计算。','Cyan is positive, magenta negative; values are computed from the recurrence.');
    $('pillAngle').querySelector('strong').textContent=kit.fix(m,2);$('pillSum').querySelector('strong').textContent=String(s.n);
  }
  const paint=kit.painter(draw,[$('stage'),$('plot')]);
  const clock=kit.clock({range:$('now'),play:$('play'),label:$('tau'),speeds:$('speedChips'),min:1,max:10,t:6,rate:1,step:1,format:t=>`n ${Math.max(1,Math.round(t))} <small>/ 10</small>`,onChange:()=>paint()});
  const fStep=kit.field($('step'),{fmt:v=>kit.fix(v,2),onInput:v=>{m=v;clock.pause();cards.mark(null);paint();}});
  const PRESETS={even:{m:-3,n:6,k:3},odd:{m:-3,n:5,k:3},excluded:{m:-1,n:4,k:2},pascal:{m:0,n:6,k:3}};
  const NOTES={
    even:['m = −3：第 6 行全部为正，内部是青色。','m = −3: every entry of row 6 is positive; its interior is cyan.'],
    odd:['m = −3：第 5 行内部为负，两端仍为 1。','m = −3: row 5 has a negative interior while both boundary entries remain 1.'],
    excluded:['m = −1：第 4 行中间两项为 −1，偶数行正性在这里失败。','m = −1: the two middle entries of row 4 are −1, so even-row positivity fails here.'],
    pascal:['m = 0：两个递推权重都是 1，得到杨辉三角。','m = 0: both recurrence weights are 1, giving Pascal’s triangle.']};
  const cards=kit.cards($('presets'),{presets:PRESETS,notes:NOTES,noteEl:$('presetNote'),tour:$('tour'),idle:['自由探索：换步长、换行或点击格子。','Explore: vary the step, change row or click a cell.'],onPick:id=>{const p=PRESETS[id];m=p.m;k=p.k;clock.pause();clock.set(p.n);fStep.set(m);paint();}});
  $('rew').addEventListener('click',()=>{clock.pause();clock.set(1);paint();});
  $('cv').addEventListener('pointerdown',ev=>{
    const b=$('cv').getBoundingClientRect(),x=view.invX(ev.clientX-b.left),y=view.invY(ev.clientY-b.top);
    let n=Math.max(1,Math.min(10,Math.round(11-y)));k=Math.max(1,Math.min(n,Math.round(x+(n+1)/2)));
    cards.mark(null);clock.pause();clock.set(n);paint();
  });
  TRV.drawer({drawer:$('drawer'),open:$('infoBtn'),close:$('drawerClose')});
  window.TRIANGLE_DEBUG={get state(){return read();},cell:(n,j)=>{const b=$('cv').getBoundingClientRect(),[x,y]=position(n,j);return[b.left+view.X(x),b.top+view.Y(y)];}};
  window.TRV_THUMB=()=>{m=-3;clock.pause();clock.set(6);paint.now();};
  cards.pick(cards.initial('even'));paint();
})();

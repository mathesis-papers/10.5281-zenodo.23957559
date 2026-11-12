#!/usr/bin/env node
import {session,stageFirstChecks,settle,until,openStill} from '../../../../tools/node/viz-testkit.mjs';
const BOOK='chen-chen-step-m-eulerian-parity-positivity',ID='step-triangle';
const T=await session(),{check}=T;
await stageFirstChecks(T,BOOK,ID);
const page=await T.goto(BOOK,ID,'?lang=en');
const state=async()=>{await settle(page);return page.evaluate(()=>window.TRIANGLE_DEBUG.state);};
// Independent representation: enumerate all left/right lattice paths, multiply their edge weights,
// then sum path weights by endpoint. The page instead updates an array by its recurrence.
function paths(m) {
 let walk=[{k:1,w:1}],rows=[[1]];
 for(let n=1;n<10;n++) {
  walk=walk.flatMap(({k,w})=>[{k,w:w*(m*(k-1)+1)},{k:k+1,w:w*(m*(n-k)+1)}]);
  rows.push(Array.from({length:n+1},(_,j)=>walk.filter(p=>p.k===j+1).reduce((a,p)=>a+p.w,0)));
 }
 return rows;
}
function binomial(n,k){let a=1;for(let j=1;j<=k;j++)a=a*(n-j+1)/j;return a;}
async function input(id,value){await page.locator(id).evaluate((el,v)=>{el.value=String(v);el.dispatchEvent(new Event('input',{bubbles:true}));},value);return state();}
let s=await state();check('default is the sixth row at step -3',s.m===-3&&s.n===6&&s.preset==='even'&&!s.playing);
for(const [card,m,n] of [['even',-3,6],['odd',-3,5],['excluded',-1,4],['pascal',0,6]]) {
 await page.click(`[data-preset="${card}"]`);s=await state();
 check(`card ${card} selects its advertised step and row`,s.m===m&&s.n===n&&s.preset===card);
 check(`card ${card} values equal independent path sums`,s.rows.every((row,i)=>row.every((v,j)=>v===paths(m)[i][j])));
 for(const lang of ['zh','en']){
  const p=await openStill(T,BOOK,ID,card,lang);await settle(p);
  const d=await p.evaluate(()=>window.TRIANGLE_DEBUG.state);
  check(`${card} ${lang} still matches caption`,d.m===m&&d.n===n&&!d.playing);
  await p.context().close();
 }
}
for(const m of [-8,-5,-4,-3.5,-3,-2,-1,0,.25,3]) {
 s=await input('#step',m);const expected=paths(m);
 let error=0;for(let i=0;i<10;i++)for(let j=0;j<=i;j++)error=Math.max(error,Math.abs(s.rows[i][j]-expected[i][j])/Math.max(1,Math.abs(expected[i][j])));
 check(`all first ten rows at m=${m} match path enumeration`,error<1e-12,`relative error ${error}`);
 check(`slider m=${m} leaves card state`,s.preset===null&&s.m===m&&!s.playing);
 if(m<=-3) check(`sampled m=${m} has positive even rows and negative odd interiors`,s.rows.every((r,i)=>(i+1)%2===0?r.every(x=>x>0):(i<2||r.slice(1,-1).every(x=>x<0))));
 if(m===-1||m===-2)check(`m=${m} fails at the two middle entries in row four`,s.rows[3][1]===-1&&s.rows[3][2]===-1);
 if(m===0)check('m=0 is the binomial triangle',s.rows.every((r,i)=>r.every((x,j)=>x===binomial(i,j))));
}
s=await input('#now',8);check('row rail selects row 8',s.n===8);
check('counts describe the selected row',s.positive===s.rows[7].filter(x=>x>0).length&&s.negative===s.rows[7].filter(x=>x<0).length);
const target=await page.evaluate(()=>window.TRIANGLE_DEBUG.cell(4,2));await page.mouse.click(...target);s=await state();
check('directly clicking a cell selects its row and column',s.n===4&&s.k===2&&s.preset===null);
await page.click('#rew');s=await state();check('rewind returns to the first row',s.n===1&&!s.playing);
await page.click('[data-speed="2.5"]');check('speed chip changes playback speed',await page.locator('[data-speed="2.5"]').getAttribute('aria-pressed')==='true');
await page.click('[data-preset="even"]');await page.keyboard.press('ArrowRight');check('right arrow advances one row',(await state()).n===7);
await page.keyboard.press('Space');check('Space starts playback',await until(page,()=>{const s=window.TRIANGLE_DEBUG.state;return s.playing&&s.t>7;}));
await page.keyboard.press('Space');check('Space pauses playback',!(await state()).playing);
check('no page-specific errors',T.errors.length===0,T.errors.slice(0,4).join(' | '));
await T.finish();

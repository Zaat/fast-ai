#!/usr/bin/env python3
"""Compute statistics over c/history/ and draw logs/progress.svg."""
import glob,os,re,subprocess,csv
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
H=sorted(glob.glob('c/history/*.c'))
L=[len(open(f).read().replace('\n','')) for f in H]
# golf steps start at the verified no-limits version (index 3, 1134 chars)
g=L[3:]; steps=[a-b for a,b in zip(g,g[1:])]
log=subprocess.run(['git','log','--format=%s'],capture_output=True,text=True).stdout.splitlines()
albert=sum(1 for s in log if s.startswith('C (') and 'Albert' in s)
rows=list(csv.DictReader(open('logs/history_results.csv')))
rej=len(glob.glob('c/rejected/*.c'))
big=sorted(zip(steps,range(len(steps))),reverse=True)[:6]
md=['# Statistics','',
f'- C versions preserved: **{len(H)}** (plus {rej} rejected attempts in `c/rejected/`)',
f'- Golf steps from the first no-limits version: **{len(steps)}**, {g[0]} → {g[-1]} chars (**{100*(g[0]-g[-1])/g[0]:.1f}%** shorter)',
f'- From the original C ({L[0]} chars) to now: **{100*(L[0]-L[-1])/L[0]:.1f}%** shorter',
f'- Average saving per step: {sum(steps)/len(steps):.1f} chars; median: {sorted(steps)[len(steps)//2]}',
f'- Steps that came from Albert\'s ideas (commit titles): **{albert}**',
f'- Versions passing re-verification today: **{sum(r["result"]=="PASS" for r in rows)}/{len(rows)}** (see `logs/history_results.md`)',
f'- Commits on this branch: {len(log)+1}','',
'## Largest single steps','','| From → To | Saved |','|---|---:|']
md+=[f'| {g[i]} → {g[i+1]} | {s} |' for s,i in big]
md+=['','## Size of each step','','```']+[f'{g[i]:>5} → {g[i+1]:>4}  -{s:<3} '+'#'*s for i,s in enumerate(steps)]+['```','','![progress](progress.svg)']
open('logs/STATS.md','w').write('\n'.join(md)+'\n')
# SVG chart
W,Hh,P=760,360,50; xs=range(len(g)); mx,mn=max(g),min(g)
X=lambda i:P+i*(W-2*P)/(len(g)-1); Y=lambda v:Hh-P-(v-500)*(Hh-2*P)/(mx-500)
pts=' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(g))
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" font-family="sans-serif" font-size="11">',
'<rect width="100%" height="100%" fill="white"/>',
f'<text x="{W/2}" y="20" text-anchor="middle" font-size="14">TREE(3) C program length per verified step</text>']
for t in range(500,mx+1,100):
    svg.append(f'<line x1="{P}" x2="{W-P}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="#ddd"/><text x="{P-6}" y="{Y(t)+4:.1f}" text-anchor="end">{t}</text>')
svg.append(f'<polyline points="{pts}" fill="none" stroke="#2a6fdb" stroke-width="2"/>')
for i,v in enumerate(g):
    if i in (0,len(g)-1) or v in (736,681,595,566):
        svg.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="#2a6fdb"/><text x="{X(i):.1f}" y="{Y(v)-8:.1f}" text-anchor="middle">{v}</text>')
svg.append(f'<text x="{W/2}" y="{Hh-12}" text-anchor="middle">verified step</text></svg>')
open('logs/progress.svg','w').write('\n'.join(svg))
print('\n'.join(md[:10]))

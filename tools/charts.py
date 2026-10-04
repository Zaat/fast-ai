#!/usr/bin/env python3
"""Draw logs/forecasts.svg (forecast vs outcome) and logs/step_savings.svg (saving per step)."""
import glob,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
def svg(w,h,title): return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" font-family="sans-serif" font-size="11">','<rect width="100%" height="100%" fill="white"/>',f'<text x="{w/2}" y="20" text-anchor="middle" font-size="14">{title}</text>']
# 1. forecasts: at each point, the "best guess" end length vs what was actually reached next milestone
F=[(790,775,736),(736,729,681),(681,640,606),(606,575,545),(595,532,545),(566,537,545),(561,545,545)]
W,H,P=760,380,60; lo,hi=520,800
X=lambda i:P+i*(W-2*P)/(len(F)-1); Y=lambda v:H-P-(v-lo)*(H-2*P)/(hi-lo)
s=svg(W,H,'Forecast best guess vs. length actually reached')
for t in range(550,hi+1,50): s.append(f'<line x1="{P}" x2="{W-P}" y1="{Y(t):.0f}" y2="{Y(t):.0f}" stroke="#eee"/><text x="{P-6}" y="{Y(t)+4:.0f}" text-anchor="end">{t}</text>')
for k,c,lab in ((0,'#999','length when forecast was made'),(1,'#e8833a','forecast best guess'),(2,'#2a6fdb','length eventually reached')):
    s.append(f'<polyline fill="none" stroke="{c}" stroke-width="2" points="{" ".join(f"{X(i):.0f},{Y(f[k]):.0f}" for i,f in enumerate(F))}"/>')
    s.append(f'<rect x="{P+10+k*220}" y="{H-25}" width="12" height="3" fill="{c}"/><text x="{P+26+k*220}" y="{H-21}">{lab}</text>')
for i,f in enumerate(F): s.append(f'<text x="{X(i):.0f}" y="{H-P+16}" text-anchor="middle">at {f[0]}</text>')
s.append('</svg>'); open('logs/forecasts.svg','w').write('\n'.join(s))
# 2. savings per step
L=[len(open(f).read().replace('\n','')) for f in sorted(glob.glob('c/history/*.c'))][3:]
d=[a-b for a,b in zip(L,L[1:])]
W,H,P=760,320,50; bw=(W-2*P)/len(d); m=max(d)
s=svg(W,H,'Characters saved per verified step (1134 → 545)')
for t in range(0,m+1,50): y=H-P-t*(H-2*P)/m; s.append(f'<line x1="{P}" x2="{W-P}" y1="{y:.0f}" y2="{y:.0f}" stroke="#eee"/><text x="{P-6}" y="{y+4:.0f}" text-anchor="end">{t}</text>')
for i,v in enumerate(d):
    hgt=v*(H-2*P)/m; s.append(f'<rect x="{P+i*bw+1:.1f}" y="{H-P-hgt:.1f}" width="{bw-2:.1f}" height="{hgt:.1f}" fill="{"#2a6fdb" if v>=10 else "#9bbcf0"}"><title>{L[i]} → {L[i+1]}: {v}</title></rect>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle">step (dark = 10+ chars, mostly structural ideas)</text></svg>')
open('logs/step_savings.svg','w').write('\n'.join(s)); print('ok')

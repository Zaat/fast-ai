#!/usr/bin/env python3
"""Run every rejected attempt in c/rejected/ and record what goes wrong.
Each is compiled with gcc and run for TREE(2) (10 s limit) without and with sanitizers."""
import os,re,subprocess,glob,time,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
sys.path.insert(0,'tools')
os.environ['ASAN_OPTIONS']='detect_leaks=0'
def run(cmd,t=None):
    s=time.time()
    try:
        p=subprocess.run(cmd,capture_output=True,text=True,timeout=t); return p.returncode,p.stdout,p.stderr,time.time()-s
    except subprocess.TimeoutExpired: return 'timeout','','',time.time()-s
def var(src,n):
    if 'atoi' in src: return None
    if '3*v' in src: return src.replace('3*v',f'{n}*v').replace('c/3',f'c/{n}').replace('c%3',f'c%{n}')
    return src.replace('c=3;',f'c={n};').replace('p<3;',f'p<{n};').replace('p<3)',f'p<{n})')
desc={l.split('|')[0]:l.split('|')[1].strip() for l in open('c/rejected/WHY.txt') if '|' in l}
out=['# Rejected attempts','','Every attempt below was proposed during the sessions and rejected. Re-run with `tools/run_rejected.py`.','TREE(2) should print 3.','',
     '| File | Chars | Why it was tried / what is wrong | gcc warnings | TREE(2) plain | TREE(2) with ASan/UBSan |','|---|---:|---|---:|---|---|']
for f in sorted(glob.glob('c/rejected/*.c')):
    n=os.path.basename(f); src=open(f).read(); ch=len(src.replace('\n',''))
    rc,_,err,_=run(['gcc','-Wall','-o','/tmp/rj',f]); w=err.count('warning:')
    v=var(src,2); sf=f; a=['2']
    if v is not None: open('/tmp/rj2.c','w').write(v); sf='/tmp/rj2.c'; a=[]
    run(['gcc','-w','-o','/tmp/rjp',sf]); r,o,e,dt=run(['/tmp/rjp']+a,10)
    plain=f"{o.strip() or '(no output)'} (rc={r}, {dt:.1f}s)" if r!='timeout' else 'no result in 10 s'
    if r==-11 or r==139: plain=f'segmentation fault ({dt:.1f}s)'
    if r==-9 or r==137: plain='killed (out of memory)'
    run(['gcc','-w','-g','-fsanitize=address,undefined','-o','/tmp/rja',sf]); r2,o2,e2,dt2=run(['/tmp/rja']+a,10)
    m=re.search(r'ERROR: AddressSanitizer: ([\w-]+)|runtime error: ([^\n]+)',e2)
    san=(m.group(1) or m.group(2))[:60] if m else (f"{o2.strip() or '(no output)'} (rc={r2})" if r2!='timeout' else 'no result in 10 s')
    open(f'logs/rejected_{n}.log','w').write(f'gcc -Wall:\n{err}\n\nplain run: rc={r}\n{o}\n\nsanitizer run: rc={r2}\nstdout: {o2}\nstderr:\n{e2[:6000]}\n')
    out.append(f'| {n} | {ch} | {desc.get(n,"")} | {w} | {plain} | {san} |'); print(n,plain,'|',san,flush=True)
open('logs/rejected_results.md','w').write('\n'.join(out)+'\n')

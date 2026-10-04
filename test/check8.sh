#!/bin/bash
# usage: check.sh file.c   (file must use layout: int* tree = [sizes..., labels...]; globals P,p,N,v; functions e(x,i,y,j), g())
F=$1
python3 -c "import sys;print('chars:',len(open('$F').read().rstrip(chr(10))))"
gcc -w -O1 -fsanitize=address,undefined -fno-sanitize-recover=all -o /tmp/tm "$F" 2>&1 | grep -i error
r1=$(/tmp/tm 1); r2=$(/tmp/tm 2); echo "TREE(1)=$r1 TREE(2)=$r2 (asan+ubsan)"
sed '/^main(/d' "$F" > /tmp/lib.c
cat >> /tmp/lib.c <<'XX'
int*rd(){int n;scanf("%d",&n);int*t=realloc(0,8*n);for(int i=0;i<2*n;i++)scanf("%d",t+i);return t;}
main(){int k;scanf("%d",&k);while(k--){x=rd(),y=rd();printf("%d\n",!!F(0,*x,0,*y));}}
XX
gcc -w -O2 -o /tmp/et /tmp/lib.c && /tmp/et < pairs_end.txt > /tmp/got.txt && echo "embedding mismatches: $(diff <(cat /tmp/got.txt) expected.txt | grep -c '^<')"
sed '/^main(/d' "$F" > /tmp/gen.c
cat >> /tmp/gen.c <<'XX'
main(){N=2;*(P=realloc(0,8))=&M;for(int v=1;v<6;)g(v++);for(int k=1;k<p;k++){int*t=P[k];printf("%d",*t);for(int i=0;i<2**t;i++)printf(" %d",t[i]);puts("");}}
XX
gcc -w -o /tmp/gen /tmp/gen.c && /tmp/gen | python3 -c "
import sys
def canon(Z,L,i=0):
    ch=[];c=i+1
    while c<i+Z[i]: ch.append(canon(Z,L,c)); c+=Z[c]
    return (L[i],)+tuple(sorted(ch))
got=set()
for line in sys.stdin:
    a=list(map(int,line.split()));n=a[0];got.add(canon([a[1+j]-j for j in range(n)],a[1+n:]))
def trees(n):
    if n==1: return {(c,) for c in (0,1)}
    res=set()
    def forests(m):
        if m==0: yield (); return
        for s in range(1,m+1):
            for t in trees(s):
                for rest in forests(m-s): yield tuple(sorted((t,)+rest))
    for c in (0,1):
        for f in forests(n-1): res.add((c,)+f)
    return res
ref=set().union(*(trees(k) for k in range(1,6)))
print('generator: distinct',len(got),'reference',len(ref),'match' if got==ref else 'MISMATCH')"

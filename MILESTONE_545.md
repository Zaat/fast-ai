# Milestone: C TREE(3) at 545 characters

This document freezes the current C milestone in one place for archival and independent-verification purposes.

## Canonical artifact

- Canonical source: `c/tree3.c`
- Historical copy: `c/history/049_545.c`
- Source length: **545 characters/bytes**
- Git blob: `8e210e0bfebd20a367fa16cc5352dbd6e4886749`
- Milestone commit: `a61616401f4c1d844a6365128ffc4cb2049ba857`
- Licence: **MIT**

The two source files above are byte-identical.

## Source

```c
void*realloc();int**P,**S,p=1,q,k,i,c,j,M,*x,*y;F(i,I,j,J){int c=j,n=j,r=i/I;for(;n<J>r;n++)n<abs(y[c])||(c=n),n<y[c]&&x[*x+i]==y[*y+n]&F(i+1,x[i],n+1,y[n])&&(y[c]*=-1,r=F(x[i],I,j,J),y[c]*=-1);return r;}g(v){for(S=realloc(S,8*p),k=p;k&&*(x=P[--k])+1==v;)for(c=3*v;c--;)for(i=c/3,P=realloc(P,8*p+8),P[p++]=y=realloc(0,8*v),j=v;j--;)q=j-(j>i),y[j]=j-i?x[q]+(x[q]>=i):i?i+1:v,y[j+v]=j-i?x[*x+q]:c%3;}f(d,k){for(g(d+2),M+=d>M;*P[k]<d+2;~q?:f(d+1,1),k++)for(S[d]=y=P[k],q=d;q--&&(x=S[q])-y&&!F(0,*x,0,*y););}main(){*(P=realloc(0,8))=&M;g(1);f(0,1);printf("%d",M);}
```

> Historical note: the canonical stored 545 version in the branch is the one preserved by the Git blob above. If this text is ever edited, the blob IDs and canonical files take precedence.

## Target environment

Archived verification environment:

```
gcc 13.3.0
x86-64 Linux
glibc 2.39
```

The program intentionally relies on permissive gcc behavior and is not portable ISO C.

## Verification

The project harness checks:

- source count;
- 3,000 embedding reference pairs;
- 286-tree generator reference set;
- TREE(1)=1;
- TREE(2)=3;
- AddressSanitizer/UBSan on tractable cases;
- bounded TREE(3) execution to catch immediate runtime failures.

Run:

```sh
cd test
bash T8.sh ../c/tree3.c
```

## Historical significance inside this project

The late sequence was:

```
595 → 566 → 561 → 545
```

The 561 → 545 step removed another **16 characters (~2.85%)** after the code had already been treated as near a practical floor.

## Claim status

This is the **shortest verified C version preserved in this project**.

No formal world-record claim is made without independent comparison under equivalent rules.

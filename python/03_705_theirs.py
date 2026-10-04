from functools import lru_cache
from itertools import product,combinations
def P(n,k):
 if k==1:return [(a,()) for a in range(n)]
 r=[]
 for a in range(n):
  for m in range(k):
   for q in product(sum((P(n,j) for j in range(1,k)),[]),repeat=m):
    if 1+sum(S(x) for x in q)==k:r+=[(a,tuple(sorted(q,key=repr)))]
 return list(dict.fromkeys(r))
def S(t):return 1+sum(map(S,t[1]))
def E(a,b):
 if a[0]!=b[0]:return any(E(a,x) for x in b[1])
 A,B=a[1],b[1]
 return any(all(E(x,y) for x,y in zip(A,c)) for c in combinations(B,len(A)))
def T(n,s=()):
 c=[x for x in sum((P(n,j) for j in range(1,len(s)+2)),[]) if all(not E(y,x) for y in s)]
 return len(s) if not c else max(T(n,s+(x,)) for x in c)
print(T(3))

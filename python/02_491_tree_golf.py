o=lambda x:tuple(sorted(x))
def a(t,c):
 r,k=t;yield r,o(k+((c,()),))
 for i,s in enumerate(k):
  for u in a(s,c):yield r,o(k[:i]+(u,)+k[i+1:])
e=lambda T,S:any(e(T,c)for c in S[1])or T[0]==S[0]and m(T[1],S[1])
m=lambda A,B:not A or any(e(A[0],b)and m(A[1:],B[:i]+B[i+1:])for i,b in enumerate(B))
def T(n,q=[]):
 S={(c,())for c in range(n)}
 for _ in q:S|={u for t in S for c in range(n)for u in a(t,c)}
 return max([T(n,q+[t])for t in S if not any(e(p,t)for p in q)]or[len(q)])
print(T(3))

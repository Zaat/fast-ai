from itertools import*
r=range(3)
a=lambda t,c:[t+((c,),)]+[t[:k]+(u,)+t[k+1:]for k in range(1,len(t))for u in a(t[k],c)]
e=lambda x,y:any(e(x,z)for z in y[1:])or x[0]==y[0]and any(all(map(e,x[1:],p))for p in permutations(y[1:],len(x)-1))
def T(q=()):
 S={(c,)for c in r}
 for _ in q:S|={u for t in S for c in r for u in a(t,c)}
 return max([T(q+(t,))for t in S if not any(e(p,t)for p in q)]+[len(q)])
print(T())

from itertools import*
r=range(3)
a=lambda t:[t+((c,),)for c in r]+[t[:k]+(u,)+t[k+1:]for k in range(1,len(t))for u in a(t[k])]
e=lambda x,y:any(e(x,z)for z in y[1:])or x[0]==y[0]and any(all(map(e,x[1:],p))for p in permutations(y[1:],len(x)-1))
T=lambda q=(),S={(c,)for c in r}:max([T(q+(t,),S|{u for t in S for u in a(t)})for t in S if all(1-e(p,t)for p in q)]+[len(q)])
print(T())

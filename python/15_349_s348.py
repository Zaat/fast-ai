from itertools import*
r=0,1,2
a=lambda t:[t+((c,),)for c in r]+[t[:k]+(u,)+t[k+1:]for k in range(1,len(t))for u in a(t[k])]
e=lambda x,y:any(e(x,z)for z in y[1:])or(x[0]==y[0])*any(all(map(e,x[1:],p))for p in permutations(y[1:],len(x)-1))
T=lambda S=[*zip(r)],*q:max([1+T(sum(map(a,S),S),*q,t)for t in S if all(1-e(p,t)for p in q)]+[0])
print(T())

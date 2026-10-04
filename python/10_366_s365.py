from itertools import*
l=len
r=range(3)
a=lambda t:[t+((c,),)for c in r]+[t[:k]+(u,)+t[k+1:]for k in range(1,l(t))for u in a(t[k])]
e=lambda x,y:any(e(x,z)for z in y[1:])or x[0]==y[0]and any(all(map(e,x[1:],p))for p in permutations(y[1:],l(x)-1))
T=lambda q=[],S={*zip(r)}:max([T(q+[t],S|{*sum(map(a,S),[])})for t in S if all(1-e(p,t)for p in q)]+[l(q)])
print(T())

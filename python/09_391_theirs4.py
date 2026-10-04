from itertools import*
R=range(3)
a=lambda t,c:[t+((c,),)]+[t[:i]+(u,)+t[i+1:]for i in range(1,len(t))for u in a(t[i],c)]
e=lambda T,S:any(e(T,c)for c in S[1:])or(T[0]==S[0])*any(all(map(e,T[1:],p))for p in permutations(S[1:],~-len(T)))
def T(q=[]):
 S=[*zip(R)]
 for _ in q:S+=sum((a(t,c)for t in S for c in R),[])
 return max([len(q),*(T(q+[t])for t in S if all(1>e(p,t)for p in q))])
T()

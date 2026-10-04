import random,itertools,json
random.seed(1)
def rand_tree(n,c):
    t=[random.randrange(c)];nodes=[t]
    for _ in range(n-1):
        p=random.choice(nodes);ch=[random.randrange(c)];p.append(ch);nodes.append(ch)
    def tup(x):return (x[0],)+tuple(tup(y) for y in x[1:])
    return tup(t)
def e(x,y):
    return any(e(x,z) for z in y[1:]) or (x[0]==y[0] and any(all(map(e,x[1:],p)) for p in itertools.permutations(y[1:],len(x)-1)))
def flat(t):
    L=[];Z=[]
    def go(u):
        i=len(L);L.append(u[0]);Z.append(0)
        for ch in u[1:]:go(ch)
        Z[i]=len(L)-i
    go(t);return Z,L   # sizes first, then labels (new layout)
pairs=[(rand_tree(random.randint(1,6),random.randint(1,3)),rand_tree(random.randint(1,9),random.randint(1,3))) for _ in range(3000)]
with open('pairs.txt','w') as f:
    f.write(str(len(pairs))+"\n")
    for x,y in pairs:
        for t in (x,y):
            Z,L=flat(t);f.write(f"{len(Z)} "+" ".join(map(str,Z+L))+"\n")
with open('expected.txt','w') as f:
    f.write("\n".join(str(int(e(x,y))) for x,y in pairs)+"\n")

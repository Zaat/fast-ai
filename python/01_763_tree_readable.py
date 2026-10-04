import sys
sys.setrecursionlimit(10000)
def add_leaf(t,c):
    yield (t[0],tuple(sorted(t[1]+((c,()),))))
    for i,s in enumerate(t[1]):
        for u in add_leaf(s,c):
            yield (t[0],tuple(sorted(t[1][:i]+(u,)+t[1][i+1:])))
def emb(T,S):
    return any(emb(T,c) for c in S[1]) or (T[0]==S[0] and match(T[1],S[1]))
def match(A,B):
    return not A or any(emb(A[0],b) and match(A[1:],B[:i]+B[i+1:]) for i,b in enumerate(B))
def TREE(n):
    def trees(k):
        S={(c,()) for c in range(n)}
        for _ in range(k-1): S|={u for t in S for c in range(n) for u in add_leaf(t,c)}
        return S
    def L(q):
        return max([L(q+[t]) for t in trees(len(q)+1) if not any(emb(p,t) for p in q)],default=len(q))
    return L([])
print(TREE(1),TREE(2))

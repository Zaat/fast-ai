# Milestone: Python TREE(3) at 348 source characters

This document freezes the current Python milestone in one place for archival and independent-verification purposes.

## Canonical artifact

- Canonical source: `python/tree3.py`
- Historical copy: `python/15_349_s348.py`
- Stored file size: **349 bytes**
- Golf count used during the project: **348 source characters + final newline**
- Git blob: `78b7242f7642c4b5edef53cfe4bc8b45aecc4723`
- Milestone commit: `dbdd9767e66e8d02cfdd507c11e835146639e470`
- Licence: **MIT**

The canonical and historical files are byte-identical.

## Source

```python
from itertools import*
r=0,1,2
a=lambda t:[t+((c,),)for c in r]+[t[:k]+(u,)+t[k+1:]for k in range(1,len(t))for u in a(t[k])]
e=lambda x,y:any(e(x,z)for z in y[1:])or(x[0]==y[0])*any(all(map(e,x[1:],p))for p in permutations(y[1:],len(x)-1))
T=lambda S=[*zip(r)],*q:max([1+T(sum(map(a,S),S),*q,t)for t in S if all(1-e(p,t)for p in q)]+[0])
print(T())
```

## Archived environment

```
Python 3.13.15
x86-64 Linux
```

TREE(3) itself is not expected to finish in practice.

## Preserved progression

```
763 → 491 → 413 → 401 → 392 → 383 → 376
    → 366 → 363 → 360 → 354 → 352 → 349 bytes
```

This is a **54.3% reduction** from the readable 763-byte reference to the canonical stored file.

## Verification status

The final five preserved Python variants can be automatically reduced to two colours by the current verifier and all produce:

```
TREE(2) = 3
```

in about 0.01 seconds in the archived environment.

Earlier Python variants are preserved but require representation-specific verification logic rather than the generic current rewrite.

## Important final idea

The milestone commit specifically records Albert's contribution:

```python
any(all(map(e,x[1:],p))for p in permutations(y[1:],len(x)-1))
```

Two shorter-looking variants were rejected because they changed semantics or failed on the empty case.

## Claim status

This is the **shortest Python version preserved in this project** under the project's counting convention.

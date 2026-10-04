# Python golf statistics

The Python track preceded much of the C work and is a substantial part of the project in its own right.

## Current result

- Canonical source: `python/tree3.py`
- Historical copy: `python/15_349_s348.py`
- Stored size: **349 bytes**
- Golf count used during the session: **348 characters plus the final newline**
- The two files are the same Git blob: `78b7242f7642c4b5edef53cfe4bc8b45aecc4723`
- Final milestone commit: `dbdd9767e66e8d02cfdd507c11e835146639e470`

## Preserved progression

| Step | File | Bytes | Best-so-far | Note |
|---:|---|---:|---:|---|
| 1 | `01_763_tree_readable.py` | 763 | 763 | readable reference |
| 2 | `02_491_tree_golf.py` | 491 | 491 | first major golf |
| 3 | `03_705_theirs.py` | 705 | 491 | comparison / alternate version |
| 4 | `04_413_short.py` | 413 | 413 | new best |
| 5 | `05_401_short2.py` | 401 | 401 | new best |
| 6 | `06_392_short3.py` | 392 | 392 | new best |
| 7 | `07_383_s390.py` | 383 | 383 | new best |
| 8 | `08_376_s375.py` | 376 | 376 | new best |
| 9 | `09_391_theirs4.py` | 391 | 376 | comparison / alternate version |
| 10 | `10_366_s365.py` | 366 | 366 | new best |
| 11 | `11_363_s362.py` | 363 | 363 | new best |
| 12 | `12_360_s360.py` | 360 | 360 | new best |
| 13 | `13_354_s353.py` | 354 | 354 | new best |
| 14 | `14_352_s351.py` | 352 | 352 | new best |
| 15 | `15_349_s348.py` | 349 | 349 | current Python best |

From the 763-byte readable reference to the 349-byte current file, stored source size fell by **54.3%**.

![Python progress](progress.svg)

## Verification currently preserved

The historical re-verifier records every numbered Python source and directly runs TREE(2) for versions whose colour set can be safely reduced by the scripted transformation. The last five preserved golf versions all produce:

```
TREE(2) = 3
```

in about **0.01 s** in the archived environment.

Earlier Python versions are preserved but the current generic re-verifier marks them "not tested" when their colour representation does not match the later `r=0,1,2` form. That is a limitation of the *verification script*, not evidence those versions are wrong.

The readable starting implementation explicitly prints `TREE(1)` and `TREE(2)`, and it served as the conceptual/reference implementation for later work.

## Important Python-specific findings

The Python golf explored a very different compression space from C:

- tuples encode rooted coloured trees directly;
- recursion and comprehensions replace explicit allocation/state machinery;
- `itertools.permutations` provides compact injective child matching;
- default arguments and variadic state compress the TREE search;
- Python's high-level operations make the source much shorter than C, but the language/runtime carries far more implicit machinery.

A key final idea attributed in the commit history to Albert was:

```python
any(all(map(e,x[1:],p))for p in permutations(y[1:],len(x)-1))
```

Two tempting reductions were explicitly rejected during the session:

- dropping the permutation length changed the semantics / results;
- `max(len(q),*[...])` can fail on the empty-list case.

## Why preserve Python separately?

The C track should not eclipse the Python work. The Python sequence was where several concepts were first made compact and testable, and it provided an independent high-level reference for reasoning about the C implementation.

The meaningful comparison is therefore not "349 vs 545, Python wins." They operate under radically different language/runtime assumptions. Both tracks demonstrate a different kind of description-length compression.

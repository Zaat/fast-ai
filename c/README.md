# C implementation

This directory contains the current TREE(3) C golf, a readable explanation, generated assembly from an earlier exploration, and the full preserved optimization history.

## Files

- `tree3.c` — current **545-character** verified entry.
- `tree3_explained.c` — commented explanation of the same current algorithm.
- `history/` — preserved verified milestones.
- `tree.s` — assembly output saved during the exploration.

## Build

```sh
gcc -w tree3.c -o tree3
```

Target: permissive gcc on x86-64. This is deliberately not portable ISO C.

## Representation

The current version stores each rooted coloured tree as a flat array. The first half stores subtree end positions; the second half stores colours. This makes subtree traversal and insertion compact enough to encode directly in arithmetic.

The embedding/matching routine `F` uses temporary sign changes in the target tree to mark already-used subtrees. The sign is restored before returning.

## Why TREE(3) never finishes here

The program implements the finite search defining TREE(3), but TREE(3) is far beyond feasible computation. Validation therefore focuses on the embedding relation, generator, TREE(1), TREE(2), sanitizer behavior, and consistency with independent reference data.

See `../test/README.md` for the verification standard.

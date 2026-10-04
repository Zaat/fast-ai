# Reproducibility

This file records the assumptions needed to reproduce the current 545-character C result.

## Target

- Architecture: **x86-64**
- Compiler family: **gcc**
- Dialect: permissive GNU C / legacy C behavior accepted by gcc
- Portability: **not a goal**

The golf intentionally relies on constructs that strict ISO C, clang, other ABIs, or `-fno-builtin` may reject or interpret differently.

## Build

From the repository root:

```sh
gcc -w c/tree3.c -o tree3
```

Warnings are suppressed because warnings are expected in deliberately golfed legacy-style C. The acceptance criterion is successful compilation in the stated target environment plus verification behavior, not warning-free source.

## Count

The current source is a one-line file.

```sh
wc -c c/tree3.c
```

should report **545** bytes for the stored current version.

The project’s historical convention is to compare source characters with line breaks excluded. Where a history file has a trailing newline, its filesystem byte count may therefore exceed the number encoded in its filename.

## Verification

```sh
cd test
bash T8.sh ../c/tree3.c
```

See `test/README.md` for the checks and expected behavior.

## Expected tractable results

```
TREE(1) = 1
TREE(2) = 3
```

TREE(3) itself is not expected to terminate on real hardware.

## What “correct” means here

The project does not claim correctness merely because the source compiles. A current-record candidate must preserve:

- the intended rooted coloured-tree generation;
- the intended homeomorphic embedding relation;
- injective matching of child subtrees;
- the sequence-size restriction defining TREE;
- the search over bad sequences;
- the verified small-case behavior.

The test harness cross-checks these components against independent/reference data on tractable cases.

## Record wording

The 545-character program is the **shortest verified C version preserved in this project**.

A claim such as “world record” should only be made after independent comparison with other submissions under matching rules.

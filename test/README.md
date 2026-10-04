# Verification harness

The C golf is intentionally non-portable and highly compressed, so **verification is part of the artifact**.

## Quick check

Run from this folder:

```sh
bash T8.sh ../c/tree3.c
```

The harness reports:

1. **character count** (line breaks excluded by the project convention);
2. **embedding mismatches** against 3,000 independently generated/reference-labelled tree pairs;
3. **generator verification** against an independently computed reference set (286 distinct trees in the current small-case check);
4. **TREE(1)** and **TREE(2)** under AddressSanitizer/UBSan (expected `1` and `3`);
5. a bounded **TREE(3)** run under sanitizers to catch immediate runtime failures.

TREE(3) is not expected to finish. A timeout on TREE(3) is therefore normal; the purpose of the bounded run is to detect crashes, sanitizer faults, or obvious control-flow failures.

## Files

- `T8.sh` — top-level driver for the current verification flow.
- `check8.sh` — checks matching the current code shape (`F`, global `x/y`, `g(v)`).
- `mkdata.py` — generates random tree pairs/reference results.
- `pairs.txt` — reference pairs in the earlier layout.
- `pairs_end.txt` — equivalent pairs in the end-position layout used by current C versions.
- `expected.txt` — expected embedding results.
- `w.c` — current 545-character source copy used by parts of the harness.
- `W.c` — related harness/test variant used during development.
- `s`, `w` — generated binaries/artifacts preserved from the verification workflow.

## What counts as a valid improvement

A shorter candidate should not replace `c/tree3.c` merely because it compiles.

It should also:

- preserve TREE(1)=1 and TREE(2)=3;
- match the embedding reference corpus;
- preserve generator output on the independently checked small cases;
- avoid sanitizer/runtime failures on tractable checks;
- avoid accidental nontermination on cases that should terminate;
- preserve the same intended TREE(3) search semantics.

Historically, several apparently obvious 1–10 character savings failed one of these tests.

## Environment

The golf targets permissive **gcc on x86-64** and deliberately relies on behavior/extensions that are not portable ISO C.

Warnings are acceptable. The question is whether the agreed target compiler builds the program and the resulting executable passes the verification standard above.

## Historical versions

Older entries in `c/history/` used slightly different tree layouts, function signatures, or initialization strategies, so the harness evolved during the project. The current `T8.sh` / `check8.sh` pair is for the current 545-character architecture.

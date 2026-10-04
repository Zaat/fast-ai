# Verification harness

Run from this folder:

    bash T8.sh ../c/tree3.c

It prints:
1. the character count (line breaks not counted);
2. `embedding mismatches`: the embedding function is compared with reference results
   from the Python version on 3,000 random tree pairs (`pairs_end.txt`, `expected.txt`);
3. `generator`: all trees with up to 5 nodes and 2 colours are generated and compared
   with an independently computed reference set (286 distinct trees);
4. TREE(1) and TREE(2) computed with AddressSanitizer and UBSan (expected 1 and 3);
5. TREE(3) run for 10 seconds under the sanitizers (exit code 124 = still running, no errors).

Files:
- `mkdata.py`: generates random tree pairs and reference results (sizes-first format, `pairs.txt`).
- `pairs_end.txt`: the same pairs converted to the end-position format used from the 608-char version on.
- `check8.sh`: the checks above for the current code shape (function `F`, globals `x`,`y`, `g(v)`).

The harness changed as the code changed shape (argument order, tree format, how the
first trees are built). `check8.sh` matches the current version; older history
versions were checked with the earlier variants of the same tests.

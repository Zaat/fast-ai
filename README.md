# TREE(3) code golf

The shortest verified programs we could write that compute **TREE(3)**, by Albert with Claude.

## What TREE(3) is
TREE(n) is the length of the longest sequence of rooted trees, each node coloured with one of
n colours, where the k-th tree has at most k nodes and no earlier tree embeds into a later one
(Kruskal's tree theorem says such sequences are always finite). TREE(1)=1, TREE(2)=3, and
TREE(3) is so large that no physical computer could ever finish computing it, so the program is
correct in principle but runs forever in practice. Smaller cases are used to test it.

## Files
- `c/tree3.c`: current best C, **545 characters**
- `c/tree3_explained.c`: the same code with line breaks and comments explaining how it works
- `c/history/`: every verified step as `step_chars.c`; each commit message explains the change
- `c/tree.s`: gcc -Os assembly of the readable C version (an early request for a short assembly version)
- `python/`: Python versions from the readable reference down to 348 characters, plus `shortest_code.py` (a character-count helper)
- `test/`: verification harness (see `test/README.md`)
- `NOTES.md`: rules, biggest wins, rejected ideas, checked claims
- `PROBABILITIES.md`: probability estimates over time, the method used, and outcomes

## Build and run
    gcc -w c/tree3.c -o tree3 && ./tree3

Requirements and caveats:
- **gcc on 64-bit x86 Linux.** It relies on implicit `int`, K&R-style parameters, the GNU `a?:b`
  operator, and gcc recognising `realloc`/`bzero`/`abs`/`printf` as built-ins without declarations.
  `-fno-builtin`, clang, or strict C99/C23 modes will not work.
- **TREE(3) only**: the colour count is fixed at 3 (versions from 816 chars on).
  To test smaller cases, change `3*v`, `c/3` and `c%3` to 1 or 2: TREE(1)=1, TREE(2)=3.
- **No fixed limits**: all storage grows with `realloc`; memory use grows without bound.
- Readability is close to zero by design; see `c/tree3_explained.c`.

## How it works (short version)
Trees are flat arrays: for each node, where its subtree ends, then each node's colour.
`g` builds all trees of the next size by inserting one node into each smaller tree.
`f` does a depth-first search over sequences, using `F` to check that no earlier tree
embeds into the candidate. `F` matches child subtrees injectively, marking a used child by
negating its end value and restoring it afterwards.

## C progression (chars, line breaks not counted)

1513 → 1778 → 824 → 1134 → 860 → 856 → 852 → 849 → 810 → 807 → 806 → 806 → 798 → 795 → 793 → 792 → 789 → 781 → 780 → 779 → 761 → 760 → 759 → 755 → 754 → 753 → 749 → 748 → 736 → 728 → 715 → 707 → 681 → 679 → 675 → 668 → 660 → 656 → 633 → 629 → 624 → 620 → 608 → 606 → 599 → 595 → 566 → 561 → 545

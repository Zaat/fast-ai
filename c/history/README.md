# C history

This directory preserves the verified C milestones from the TREE(3) golfing sessions.

The filenames encode the order and recorded source length, for example:

```
046_595.c
047_566.c
048_561.c
049_545.c
```

The history is intentionally kept rather than squashed because the major reductions often came from **different representations**, not just shorter syntax. Comparing adjacent files shows where a local minimum was escaped by changing how the algorithm itself was encoded.

## Selected late-stage milestones

| File | Length | Main significance |
|---|---:|---|
| `029_736.c` | 736 | first major late-stage compact flat representation |
| `033_681.c` | 681 | global tree context / tighter embedding machinery |
| `040_629.c` | 629 | `k` passed into `f`; global `r` removed |
| `043_608.c` | 608 | subtree end positions instead of sizes |
| `046_595.c` | 595 | highly compressed generator/search architecture |
| `047_566.c` | 566 | matching and embedding merged into one function `F` |
| `048_561.c` | 561 | apparent near-floor version |
| `049_545.c` | 545 | current best: `realloc` declaration dropped (15) plus `n<J>r` (1) |

For the full source-length progression, see the repository root `README.md`.

## Verification

These files were preserved as verified milestones under the project’s evolving harness. Older versions do not all share the current tree layout or function signatures, so the present `test/check8.sh` is specifically for the current architecture.

The goal of the history is archival and explanatory: it records how the program changed, including the dead ends and structural jumps that made later versions possible.

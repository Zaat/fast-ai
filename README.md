# TREE(3) code golf

Shortest verified programs that compute TREE(3). The search is correct but never finishes in practice.

- `c/tree3.c`: current best C, 545 chars (gcc, x86-64: `gcc -w tree3.c`)
- `c/history/`: every verified step as `step_chars.c`; each commit message explains the change
- `python/`: Python versions (final 348 chars plus newline)
- `test/`: verification harness
- `NOTES.md`: rejected ideas, checked claims and estimates

## C progression (chars, line breaks not counted)

1513 → 1778 → 824 → 1134 → 860 → 856 → 852 → 849 → 810 → 807 → 806 → 806 → 798 → 795 → 793 → 792 → 789 → 781 → 780 → 779 → 761 → 760 → 759 → 755 → 754 → 753 → 749 → 748 → 736 → 728 → 715 → 707 → 681 → 679 → 675 → 668 → 660 → 656 → 633 → 629 → 624 → 620 → 608 → 606 → 599 → 595 → 566 → 561 → 545

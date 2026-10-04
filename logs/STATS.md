# Statistics

- C versions preserved: **49** (plus 12 rejected attempts in `c/rejected/`)
- Golf steps from the first no-limits version: **45**, 1134 → 545 chars (**51.9%** shorter)
- From the original C (1513 chars) to now: **64.0%** shorter
- Average saving per step: 13.1 chars; median: 4
- Steps that came from Albert's ideas (commit titles): **13**
- Versions passing re-verification today: **47/49** (see `logs/history_results.md`)
- Commit history: **95+ commits** at archival-audit time; continues to grow with curation and CI

## Largest single steps

| From → To | Saved |
|---|---:|
| 1134 → 860 | 274 |
| 849 → 810 | 39 |
| 595 → 566 | 29 |
| 707 → 681 | 26 |
| 656 → 633 | 23 |
| 779 → 761 | 18 |

## Size of each step

```
 1134 →  860  -274 ##################################################################################################################################################################################################################################################################################
  860 →  856  -4   ####
  856 →  852  -4   ####
  852 →  849  -3   ###
  849 →  810  -39  #######################################
  810 →  807  -3   ###
  807 →  806  -1   #
  806 →  806  -0   
  806 →  798  -8   ########
  798 →  795  -3   ###
  795 →  793  -2   ##
  793 →  792  -1   #
  792 →  789  -3   ###
  789 →  781  -8   ########
  781 →  780  -1   #
  780 →  779  -1   #
  779 →  761  -18  ##################
  761 →  760  -1   #
  760 →  759  -1   #
  759 →  755  -4   ####
  755 →  754  -1   #
  754 →  753  -1   #
  753 →  749  -4   ####
  749 →  748  -1   #
  748 →  736  -12  ############
  736 →  728  -8   ########
  728 →  715  -13  #############
  715 →  707  -8   ########
  707 →  681  -26  ##########################
  681 →  679  -2   ##
  679 →  675  -4   ####
  675 →  668  -7   #######
  668 →  660  -8   ########
  660 →  656  -4   ####
  656 →  633  -23  #######################
  633 →  629  -4   ####
  629 →  624  -5   #####
  624 →  620  -4   ####
  620 →  608  -12  ############
  608 →  606  -2   ##
  606 →  599  -7   #######
  599 →  595  -4   ####
  595 →  566  -29  #############################
  566 →  561  -5   #####
  561 →  545  -16  ################
```

![progress](progress.svg)


## Verification and build statistics

Across the 49 preserved C files in `logs/history_results.csv`:

- **47 pass** current re-verification; **2 fail** for historically documented reasons.
- Compile time range in the archived environment: **0.03–0.06 s** per version.
- Mean compile time: **~0.043 s**.
- Compiled binary-size range: **16,360–16,552 bytes**.
- Original 1,513-char C binary: **16,408 bytes**.
- Current 545-char C binary: **16,416 bytes**.
- Current source emits **22 warnings** under the historical diagnostic run; the maximum
  observed among preserved versions is 29.

The contrast between a ~64% source reduction and essentially unchanged executable size is
shown in `source_vs_binary.svg`.

## Rejected-attempt statistics

The 12 preserved rejected attempts cover several distinct failure classes:

- memory safety / crash / out-of-memory failures;
- wrong TREE results;
- embedding nontermination on a small reference pair;
- a correct but longer rewrite;
- a confidently misreported "598-char" claim whose code was actually 795 chars.

See `rejected_failure_modes.svg` and `rejected_results.md`.

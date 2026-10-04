# Probability estimates during the golf

Every few steps Albert asked how likely further trimming was. These are the
estimates as they were given at the time (subjective judgement, not measurements),
followed by what actually happened.

## Method
1. **Inventory of remaining ideas.** List concrete untried changes, estimate how many
   characters each could save and how likely it is to work (small tricks: high
   probability, 1-5 chars; structural ideas: low probability, 10-30 chars).
2. **Per-component floor.** Split the program into its parts (globals, matcher,
   embedding check, generator, search, main), estimate each part's plausible minimum,
   and add them up to get a "practical floor".
3. **Diminishing returns.** Look at how much each recent idea saved (e.g. 26 -> 11 -> 5)
   and assume the trend continues.
4. **Cumulative curves.** Express the result as P(final length <= X) for several X.
5. **Calibration against the track record** (added later). Every estimate turned out
   too pessimistic, so from 561 on the curves were deliberately shifted toward more
   savings instead of defending them.

## Estimates over time
| When (current length) | Estimate given | Outcome |
|---|---|---|
| 790 | <=789 97%, <=785 85%, <=780 65%, <=770 40%, <=750 15%, <=710 3% | 736 reached in the next few rounds, 681 soon after |
| 790 | "best guess: a careful effort ends around 770-780" | beaten by 100+ chars |
| 736 | 729: ~75%; low 720s: ~40% | 681 |
| 736 | readability rated ~5% | - |
| 681 | 630-650 "realistic"; <600 ~20%; floor ~450-500 | 633, then 606 |
| 606 | <=600 95%, <=590 75%, <=575 50%, <=550 25%, <=500 8%, <=450 2% | 595, 566, 561, 545 |
| 595 | floor 510-555; 480 ~15% (needs a new algorithm) | merge of matcher+embedding check gave 566 |
| 566 | 480 ~5%; 530-545 ~50% | 561, then 545 |
| 561 | 555 85%, 545 60%, 530 35%, 500 10%, 480 3% | 545 |
| 561 (recalibrated) | 555 90%, 545 65%, 530 40%, 500 12%, 480 4% | 545 |

## Retrospective probabilities
| Target | Implied by the first estimate (at 790) | Later estimate |
|---|---|---|
| 681 | <1% | - |
| 606 | ~0.1% | ~10% at 681 |
| 595 | well under 0.1% | ~15% at 681, ~85% at 606 |

## An outside estimate that failed
A pasted analysis argued that at 595 the search was nearly exhausted and gave
P(<=561) of about 0.25% (1 in 400). 561 was reached about 20 minutes later. Its main
errors: it treated "obvious tricks used up" as "nothing left", missed that each big
change opened new ones, and ignored the pessimistic track record.

## Lesson
Big savings came from structural ideas that were not foreseeable when the estimate
was made (global x/y, merging functions, end positions, empty-tree seed, built-in
realloc). Forecasts based only on visible remaining tricks systematically
underestimated how far the code could shrink.

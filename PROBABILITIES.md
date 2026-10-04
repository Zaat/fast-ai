# Probability history of the TREE(3) golf

These are **subjective forecasts made during the golfing sessions**, preserved because
the forecasting failures became part of the story. They are not empirical frequencies,
not proofs about the shortest possible program, and not literal odds that can be
multiplied as if the events were independent lottery draws.

The striking lesson is that we repeatedly confused **"I cannot currently see another
compression"** with **"another compression is extremely unlikely to exist."** Large
representation-level changes kept invalidating that assumption.

## What was being estimated

Let

```
L = the shortest valid source length under the agreed rules
```

The clean question is therefore `P(L <= X)`, not "what is the chance of another
miracle?" A new record tells us that the previous distribution over `L` was too high;
a long unsuccessful search is evidence in the other direction.

The time-bounded questions ("within 20 minutes", "today") add a second uncertainty:
even if a shorter program exists, will we discover, implement, compile, test and verify
it inside that time window?

## Forecasts actually made during the descent

The table below records representative estimates from the conversation. Ranges are
kept where the estimate moved during discussion.

| Current best | Target / forecast | Estimate at the time | What happened |
|---:|---|---:|---|
| ~991 | <950 / <900 / <860 / <820 / <800 / <750 | 85% / 60% / 40% / 20% / 10% / **3%** | All were eventually beaten; 748 was reached |
| 857 | <850 / <825 / <800 / <775 / <750 | 85% / 60% / 40% / 20% / 10% | 748, then far lower |
| 772 | <=768 / <=765 / <=762 / <=760 / <=750 / <=740 / <=725 | 90% / 80% / 65% / 55% / 25% / 10% / 3% | 729, 681 and lower followed |
| 729 | <=681 | about 15–25% from that point; retrospectively <0.1% from the ~991 stage | 681 reached |
| 669 | <=663 | ~30% overall (~40% conditional on 669 being valid) | 663 was surpassed |
| 669 | <=629 | ~3–5% | 629 reached |
| 629 | <=620 / <=610 / <=600 / <=590 / <=580 / <=560 / <=550 | 80% / 55% / 33% / 19% / 11% / 3% / 1% | 595, 561 and 545 followed |
| 595 | <=561 | initially ~20–25%; later pushed down as "search exhaustion" arguments accumulated | 561 reached soon afterward |
| 595 | <=561 eventually | **~0.25% (~1 in 400)** in the harshest local-floor model | 561 reached |
| 595 | <=561 within ~20 min | a crude uniform-time model produced **~1 in 35 million** | 561 was reached in roughly 15–20 minutes |
| 561 | <=555 / <=551 / <=549 / <=546 | estimates wandered from ~25/12/7/3% down to tiny values as more constraints were considered | 545 ultimately beat all four |
| 561 | <=546 today | estimates were repeatedly revised downward: ~0.6%, ~0.1%, ~0.005%, then "multi-million-to-one" and still lower | 545 was reached in the same session |

## The "1 in 35 million" and later extreme odds

The most dramatic miss was the estimate that reaching <=561 within about 20 minutes
was roughly **1 in 35 million**. That number came from a bad model:

1. estimate the probability that <=561 existed at all;
2. estimate the chance of finding it within six months;
3. spread that chance roughly uniformly over minutes;
4. multiply.

Code-golf breakthroughs are not uniformly distributed in time. They are lumpy:
nothing happens, then one representation change deletes dozens of characters. The
uniform-time assumption therefore manufactured absurdly tiny numbers.

After 561 was reached, the discussion repeated the same mistake for 546. As more
constraints were named (already-obfuscated C, no whitespace, short variable names,
headers removed, compile/run/correctness requirements, limited time and attention),
the estimate was pushed into the millions-, billions-, and even lower-to-one range.
Those figures should be archived as **forecasting artifacts, not calibrated facts**.

They were also highly correlated. "No whitespace", "one-letter names", "no includes",
"very obfuscated", and "loose GNU C" are mostly different symptoms of the same fact:
ordinary syntactic slack was already exhausted. Multiplying each as an independent
rarity factor would double-count the evidence.

## What actually happened

The source-length history contains repeated late-stage collapses:

```
... 729 -> 681 -> 629 -> 595 -> 561 -> 545
```

The important part is not merely that new records appeared, but **how**:

- a different tree representation made previously explicit metadata implicit;
- sign marking replaced a separate "used child" structure;
- global tree context removed repeated pointer arguments;
- matcher and embedding logic were merged;
- tree generation reused the empty-tree seed;
- subtree end positions replaced subtree sizes;
- C expression semantics (including chained comparisons and GNU extensions) folded
  multiple logical conditions into fewer source characters.

The 595 -> 561 step was a ~5.7% reduction from an already extreme program.
The 561 -> 545 step removed another 16 characters (~2.85%) after 561 had already
been treated as near-irreducible.

## Why the probability model kept failing

### 1. Local minima were mistaken for global floors
At each stage the current code looked saturated because all **visible** improvements
had been tried. The next large saving usually came from changing what was visible.

### 2. Structural discoveries have fat tails
A normal local edit saves 1–3 characters. A new invariant or representation can make
an entire mechanism disappear and save 10–40 characters at once.

### 3. Search changes the search space
A breakthrough does not merely shorten the program; it creates new expressions,
new shared state and new algebraic identities that did not exist in the previous
representation.

### 4. "No idea left" is weak evidence
It is evidence about the present search state, not a theorem about minimum description
length.

### 5. Correctness constraints matter
Many seductive trims were rejected because they returned TREE(2)=2, corrupted
recursive state, truncated pointers, reintroduced self-embedding loops, or otherwise
failed the test harness. A short candidate counts only after verification.

## How to interpret rarity now

The achievement is genuinely unusual: a complete TREE(3) search was compressed to
545 characters of extremely loose C after many rounds of verified optimization.

What we **cannot** honestly claim is that 545 was literally a "1 in 35 million",
"1 in a billion", or "1 in quintillions" event. Those numbers came from subjective
models that were immediately falsified.

The reproducible facts are stronger than the speculative odds:

- the exact source is preserved;
- the byte/character count is measurable;
- the compiler assumptions are stated;
- the verification harness is preserved;
- the sequence of progressively shorter verified programs is preserved;
- the structural ideas behind the big jumps can be inspected.

That is the right basis for calling the result noteworthy.

## Forecasting lesson

The best summary from the session is:

> **Apparent semantic density is not the same thing as proximity to minimum
> description length.**

Repeatedly, the code looked irreducible because every known optimization had already
been applied. Repeatedly, a new representation made part of the "irreducible" logic
disappear.

For future estimates, maintain a distribution over the unknown minimum `L`, update it
with both successful and failed searches, and avoid multiplying correlated constraints
or assuming discoveries arrive uniformly in time.

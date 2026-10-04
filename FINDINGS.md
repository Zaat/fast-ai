# Key findings and conclusions

This file collects the conclusions that survived repeated testing and discussion during the
TREE(3) code-golf project. It separates **measured/reproduced facts** from subjective judgments.

## 1. Correctness had to outrank character count

The project repeatedly found shorter-looking programs that compiled but were wrong.

Observed failures included:

- TREE(2)=2 or TREE(2)=0;
- segfaults and heap-buffer-overflows;
- pointer truncation on x86-64;
- out-of-memory behavior;
- embedding scans that hung on a small reference pair;
- fixed-limit versions that terminated and printed a small number for TREE(3), proving they
  were no longer the intended unbounded search.

**Conclusion:** compilation alone is not evidence of correctness. A candidate is only useful
after independent embedding/generator checks and tractable TREE cases agree.

## 2. Warnings are acceptable; silent semantic breakage is not

The agreed target is permissive gcc on x86-64. The golf deliberately uses legacy/implicit C
and GNU/compiler behavior. Warning-free compilation was never the objective.

The current 545-character source produces warnings under normal diagnostic flags, but it
builds in the stated environment and passes the project harness.

**Conclusion:** the relevant contract is the stated compiler/ABI plus verified behavior,
not ISO-C portability or zero warnings.

## 3. The major savings were representational collapses

Late-stage progress did not come mainly from whitespace, identifiers, or headers; those easy
savings were already exhausted.

The largest useful reductions came from making previously explicit state disappear:

- flat preorder arrays instead of object-like trees;
- subtree end positions instead of subtree sizes;
- sign-marking used target children inside the tree representation;
- global source/target context;
- merging embedding and child matching into one recurrence;
- reusing the empty-tree seed;
- folding loop-success state into C expressions such as `n<J>r`.

**Conclusion:** the decisive question was often not "how do we spell this logic shorter?" but
"how do we represent the problem so this logic no longer needs to be written?"

## 4. Source compression barely changed machine-code size

Across the preserved history, the original 1,513-character C compiled to about 16,408 bytes
in the archived environment. The current 545-character source compiles to about 16,416 bytes.

That is a ~64% reduction in source text while the executable size remains essentially flat.

See `logs/source_vs_binary.svg`.

**Conclusion:** this project is about source-description compression, not generating a
proportionally smaller executable.

## 5. The harness materially changed what was knowable

Re-running all 49 preserved C versions under the archived environment produced:

- **47 PASS**
- **2 FAIL**

The two failures are historically informative:

1. an early readable version contains a memory bug exposed by sanitizer re-verification;
2. the rejected fixed-limit version exits with `6` for TREE(3), demonstrating exactly why
   arbitrary caps were disallowed.

The harness also rejected twelve documented shortcut attempts for concrete reasons.

**Conclusion:** preserving failures is part of the result. They show which apparent reductions
were invalid and prevent the same dead ends from being rediscovered.

## 6. "It looks irreducible" was a poor predictor of the floor

The code repeatedly appeared to be at or beyond its practical ceiling. Then another structural
change removed 10–30 characters at once.

The late sequence

```
707 → 681 → 656 → 633 → 620 → 608 → 595 → 566 → 561 → 545
```

is the clearest demonstration.

**Conclusion:** local exhaustion of visible edits is weak evidence about the global minimum.

## 7. Probability forecasts were useful as a record of model failure

The session made increasingly pessimistic forecasts about future reductions, including a crude
~1-in-35-million estimate for reaching 561 within about 20 minutes and later even more extreme
figures for reaching the mid-540s.

Those estimates were then beaten almost immediately.

**Conclusion:** the probability history is worth preserving, but as evidence about
miscalibrated forecasting and fat-tailed structural discoveries—not as literal measured odds
for the achievement.

## 8. Runtime still matters, even in code golf

A candidate could not count merely by replacing efficient structure with a pathological brute
force that made tractable cases practically useless.

TREE(3) itself is inherently infeasible, so "usable" means the implementation should not add
gratuitous failure or explosive overhead to the small/reference cases used for verification.

**Conclusion:** source size, correctness, and practical behavior on tractable cases are all
part of the accepted project rules.

## 9. The environment is part of the program

The 545-character entry depends on the stated gcc/x86-64 environment, including compiler
built-ins and permissive treatment of old-style constructs.

**Conclusion:** compiler, ABI, and build assumptions are first-class archival metadata, not
footnotes. See `ENVIRONMENT.md` and `REPRODUCIBILITY.md`.

## 10. Historical claims should be reproducible before they are grand

The project discussed whether the result was a "world record", Wikipedia-worthy, or
"once-in-a-universe" rare. The durable conclusion was more conservative:

- the artifact itself is unusual and worth preserving;
- the repository can prove what *this project* achieved;
- formal world-record/notability claims require independent comparison and external sourcing.

**Conclusion:** preserve the strongest reproducible claim first. External recognition can be
added later if it arrives.

## 11. What the project ultimately demonstrated

The shortest summary is:

> **Apparent semantic density is not the same thing as proximity to minimum description
> length.**

The code became shorter not because the same ideas were typed more aggressively, but because
the representation kept changing until whole pieces of explicit logic could disappear.

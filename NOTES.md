# Notes from the TREE(3) golfing sessions

Work by Albert with AI assistance. Every preserved C milestone in `c/history/` was kept only after the relevant verification checks passed.

Current verified C best in this project: **545 characters**.

## Ground rules

- No fixed-capacity shortcuts: versions that imposed arbitrary node/sequence limits were rejected.
- Target environment: gcc on x86-64, permissive GNU C.
- Warnings are allowed; portability and strict standards compliance are not goals.
- TREE(3) only from the point where the colour count was fixed at 3.
- A shorter version counts only if it still compiles in the target environment and preserves the intended TREE semantics on the verification harness.
- TREE(3) itself is not expected to finish in practice; tractable cases and structural checks are used for verification.

## Current representation

Each tree is a flat `int` array representing preorder nodes:

- `t[i]` is the exclusive end position of node `i`'s subtree.
- `t[n+i]` is the node colour, where `n=t[0]`.
- Children of node `i` are found by starting at `i+1` and jumping to successive subtree ends.
- A target child already used by the embedding matcher is marked by negating its end position, then restored.

This representation was a major late-stage simplification because subtree traversal becomes direct index arithmetic rather than explicit tree objects or stored child lists.

## Biggest structural wins

| Change | Approx. saving / effect |
|---|---:|
| Globals `x`, `y` for the two trees being compared | ~26 chars |
| Merge embedding and child matching into recursive `F` | ~26 chars |
| Seed with the empty tree and let `g` generate the first real trees | ~23 chars |
| Store subtree end positions instead of subtree sizes | ~12 chars |
| Drop explicit `realloc` declaration and rely on gcc built-in behavior | ~15 chars |
| Sign-mark used target subtrees instead of a separate used-array | ~10 chars net |
| Fold matcher stop state into chained comparison `n<J>r` | 1 char (part of 561 → 545) |

The last two major verified collapses were:

```
595 → 561   merged/reframed matcher + embedding logic
561 → 545   15 chars from dropping the realloc declaration + 1 from n<J>r
```

These were structural changes, not whitespace/name cleanup.

## Why the 545-byte program is difficult to read

Nearly every remaining token has multiple jobs:

- globals are reused across functions;
- recursion state is encoded into arithmetic and side effects;
- target-matching state is stored inside the tree itself;
- loop conditions also carry success/failure state;
- generation and traversal exploit the exact flat-array layout;
- ordinary abstractions were deliberately removed.

The readable companion `c/tree3_explained.c` should be used to understand the current program.

## Rejected or broken ideas

- Fixed-size tree or sequence arrays: invalid because they impose arbitrary limits.
- Globalising recursion-sensitive loop variables: corrupted caller state.
- `return!i<I`: parses as `(!i)<I`, not `!(i<I)`.
- Removing `abs` from marked-child traversal: marked subtree ends become negative and traversal moves backward.
- Removing the self-comparison guard: source and target alias; temporary marking corrupts both and can run out of memory.
- Storing pointers in `int*S`: truncates pointers on x86-64 and segfaults.
- Reusing recursion state across `f` frames: produced wrong TREE(2) values.
- Loop fusions that appended trees before construction completed: inserted partial trees.
- Argument-address tricks such as `(&x)[1]`: invalid with register-passed arguments on x86-64.
- Strictly shorter-looking rewrites were repeatedly rejected when TREE(2), embedding pairs, generator output, or sanitizer checks failed.

## Verified claims and corrections from the sessions

Several plausible analyses turned out to be wrong and were corrected through testing:

- `*P[p++]=1` was accused of unsequenced access; in that form `p` is evaluated once and the claim was incorrect.
- Some early matcher rewrites appeared equivalent but returned TREE(2)=2.
- Removing the target-child state array only became safe after sign-marking plus corresponding traversal changes.
- A shorter version with `int*S` looked plausible but crashed because tree pointers were truncated.
- The self-comparison shortcut was not redundant in the relevant architecture.
- A pasted analysis claimed global `k`/`c` in `g` and the undeclared `bzero` were bugs and offered a "corrected 598-char" version; the code it gave was actually 795 chars and the bugs did not exist (782-char version passed all checks).
- A pasted analysis pointed out that `f` falls off its end while its value was tested by `&&`; this was **correct**, and the 761 version fixed it with `?:` (saving 1 char instead of the proposed +2).
- `P[p][1]=p++` (an early attempt) really was unsequenced: it segfaulted.
- Unparenthesised `#define A(n)n<0?-n:n` misparses inside `i+A(x[i])` and runs out of memory; a macro also cost more than it saved (+17 net).

## Verification standard

The current harness checks:

- source count;
- thousands of embedding comparisons against reference data;
- generator output against an independent reference set;
- TREE(1)=1 and TREE(2)=3;
- sanitizer runs on tractable cases;
- bounded TREE(3) execution for immediate runtime failures.

See `test/README.md`.

## Probability-forecast history

The search repeatedly beat forecasts that assumed the current code was near a practical floor. The most extreme examples include a crude ~1-in-35-million estimate for reaching 561 quickly, followed by 561 appearing within roughly 15–20 minutes, and later ultra-small forecasts for reaching 546 before the 545 version appeared in the same session.

Those numbers are preserved in `PROBABILITIES.md` as **forecasting artifacts**, not literal calibrated odds.

The main lesson:

> Apparent semantic density is not the same as proximity to minimum description length.

## Record status

The branch documents the shortest **verified version in this project**. It should not be described as a formal world record unless independent comparison and external verification establish that claim.

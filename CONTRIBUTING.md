# Contributing and shorter-candidate rules

Contributions are welcome, especially shorter correct programs, independent verification,
new regression cases, and documentation corrections.

## Shorter C candidate

A candidate intended to replace `c/tree3.c` should include:

1. the complete source;
2. the claimed character count using this project's counting convention;
3. the compiler, version, architecture, and any new assumptions;
4. a short explanation of the saving;
5. output from the current verification harness;
6. disclosure of any change in semantics, limits, or performance characteristics.

Before proposing a new record, run:

```sh
cd test
bash T8.sh ../path/to/candidate.c
```

A candidate does **not** count merely because it compiles or passes TREE(1)/TREE(2). It
must preserve the intended TREE search and pass the embedding and generator checks as well.

## Things that do not count

- fixed tree/sequence limits;
- hard-coded results;
- a source that crashes, segfaults, accidentally loops on tractable cases, or silently
  changes the embedding relation;
- relying on a different compiler/ABI without stating that as a new ruleset;
- shaving characters by removing correctness checks that are semantically required.

## Evidence

For a shorter candidate, attach or link:

- exact compiler command;
- `gcc --version`;
- `uname -a` (or equivalent platform information);
- harness output;
- character count;
- sanitizer output if relevant.

The issue template in `.github/ISSUE_TEMPLATE/shorter-candidate.yml` can be used for this.

## Historical integrity

Do not rewrite or delete old milestones simply because a shorter version appears. Add the
new version to the history so the path of discovery remains reproducible.

## Record wording

Until independently established against external submissions under equivalent rules, use
phrasing such as **"shortest verified C version in this project"** or **"candidate record"**,
not "world record".

# Archive integrity audit

This audit checks whether the repository curation work accidentally overwrote or dropped useful
material from the TREE(3) project.

## Scope

The audit sampled the branch history around the major documentation/logging commits and compared
the current versions of the project's core files with earlier committed versions.

Checked areas:

- `README.md`
- `NOTES.md`
- `PROBABILITIES.md`
- `JOURNAL.md`
- `c/tree3.c`
- `c/history/`
- `c/rejected/`
- `test/`
- `logs/`
- `tools/`
- GitHub Actions configuration

## Result

**No destructive loss of the canonical 545-character source or its verification data was found.**

The current `c/tree3.c` and `c/history/049_545.c` are the same Git blob:

```
8e210e0bfebd20a367fa16cc5352dbd6e4886749
```

That is important: later documentation work did not alter the canonical 545-byte artifact.

The core reference corpus and harness are also still present and are content-addressed in
`MANIFEST.md`.

## Documentation overwrite check

### README
Earlier README material was not lost in the curation sequence sampled. The current README keeps
the project definition, build assumptions, verification description, milestone sequence,
representation breakthroughs and status wording while adding charts, logs, milestone commit
links and project metadata.

### NOTES
The technical notes survived the documentation updates. The current file retains the ground
rules, representation, structural wins, rejected ideas, C-semantics corrections, verification
standard and probability lesson.

### PROBABILITIES
The probability history was expanded rather than replaced. The original forecast table and
model-failure explanation remain, with later forecast-history and cosmic-odds discussion added.

### JOURNAL
The journal was introduced later in the archive work, so there is no earlier journal body that
was overwritten. It consolidates conversation topics that previously existed only in chat,
commit messages or scattered notes.

## What cannot be recovered exactly

The original interactive sessions did **not** save every raw stdout/stderr stream, shell command,
compiler invocation or failed scratch candidate as a file at the instant it occurred.

Those exact ephemeral terminal transcripts therefore cannot be reconstructed perfectly after the
fact.

What *was* recoverable has been preserved in three ways:

1. preserved historical source files and commit messages;
2. regenerated logs produced by re-running those sources in the stated environment;
3. explicit rejected-attempt files for candidates whose failures were discussed and could be
   reconstructed.

The regenerated material is deliberately labelled as such in `logs/README.md`; it should not be
presented as an original in-session transcript.

## Historical anomalies preserved rather than erased

Re-verification found two historical files that do not pass today's verification:

- the early readable C contains a sanitizer-detected memory bug;
- the fixed-limit experiment exits with a small TREE(3) result because its caps change the
  problem.

These files were **not deleted or silently repaired**. Keeping them is valuable because they
document why the verification rules hardened.

## Recovery principle

Git history is part of the archive. Future cleanup should follow these rules:

- never rewrite `c/history/` to make old attempts look cleaner;
- never replace a failed historical version with a repaired one under the same filename;
- append corrections and explanations instead of erasing mistakes;
- keep generated re-verification logs distinguishable from original session evidence;
- preserve the canonical 545 source byte-for-byte unless a new verified record supersedes it,
  in which case keep 545 as a milestone.

## Conclusion

The current branch is a **superset archive**, not a cleaned-up rewrite of the project. The
important source history, failures, probability discussions, verification evidence and major
technical conclusions remain recoverable.

The only material known to be permanently unavailable is ephemeral session output that was never
saved in the first place.

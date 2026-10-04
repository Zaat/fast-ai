# Logs

All produced by the scripts in `tools/` (environment: `ENVIRONMENT.md`).

| File | What it is | Produced by |
|---|---|---|
| `current_harness.log` | Full harness run on the current `c/tree3.c` | `test/T8.sh` |
| `history_results.md` / `.csv` | Every version in `c/history/` re-verified: warnings, compile time, binary size, TREE(1), TREE(2), TREE(3) | `tools/verify_all.py` |
| `c/*.md` | Per-version detail: full gcc warning output, sanitizer reports | `tools/verify_all.py` |
| `python/*.log` | Python versions run with 2 colours (TREE(2)) | `tools/verify_all.py` |
| `rejected_results.md`, `rejected_*.log` | What goes wrong with each rejected attempt | `tools/run_rejected.py` |
| `STATS.md`, `progress.svg` | Statistics and a chart of the progression | `tools/stats.py` |
| `forecasts.svg`, `step_savings.svg` | Forecast best guesses vs outcomes; characters saved per step | `tools/charts.py` |
| `source_vs_binary.svg` | Source length vs compiled binary size, normalized to the original C | archival analysis of `history_results.csv` |
| `verification_outcomes.svg` | 47/49 historical versions passing current re-verification | archival analysis of `history_results.csv` |
| `rejected_failure_modes.svg` | Failure-mode summary for the 12 preserved rejected attempts | archival analysis of `rejected_results.md` |

These logs were regenerated after the sessions by re-running the preserved sources, so they
reflect what each version does today with the stated compiler. The original in-session test
runs were not saved as files; their results are summarised in the commit messages.

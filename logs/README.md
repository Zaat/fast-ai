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

These logs were regenerated after the sessions by re-running the preserved sources, so they
reflect what each version does today with the stated compiler. The original in-session test
runs were not saved as files; their results are summarised in the commit messages.

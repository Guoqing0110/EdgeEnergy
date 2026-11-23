# Reproduce a thesis result

[Set up the environment](README.md#run-an-example), then run `python -B reproduce.py --only STUDY --output ../run` from the clone or extracted package. Replace `STUDY` with an entry below and use a fresh output directory. Output paths in the table are relative to `../run/`.

| Thesis experiment | STUDY | First output to open |
|---|---|---|
| Ch. 4 · Dynamic-K: five schedulers with fixed or adaptive donor limits | `dynamic-k` | `experiments/dynamic-k/nominal_results.csv` — eleven simulated configurations, including no transfer |
| Ch. 5 · DA-IES-S: value of reports and reserve protection | `da-ies-s` | `experiments/da-ies-s/results.json` — two new example trajectories; `experiments/da-ies-s/matched-policy-tables.txt` — policy means from the 735 and 1,176 stored trajectory summaries |
| Ch. 6, Stage I · Local anomaly sensing | `adaptive-sampling-monitoring` | `experiments/adaptive-sampling-monitoring/task10/table_6_3.csv` — four simulated policies on one measured temperature window; `experiments/adaptive-sampling-monitoring/hardware_replay.json` — one recorded session |
| Ch. 6, Stage II · Revisits along a moving front | `stage-ii` | `stage-ii/runs.csv` — one new simulation; `stage-ii-tables/table_comparison.csv` — comparisons with thesis table values |
| Chs. 4–5 · Ten-node hardware records | `hil` | `hil/dynamic-k.json` and `hil/da-ies-s.json` — wireless traffic, host energy accounts and controller replay |

**Full experiments and figures.** In the extracted package, `experiments/adaptive-sampling-monitoring/stage-ii/README.md` gives the commands for all 220 moving-front runs and Figure 6.8. For the additional Ch. 5 comparisons and Ch. 6 session tables, run `python -B experiments/thesis-tables/verify.py` from the extracted package; it prints the values calculated from the supplied records. See `experiments/thesis-tables/README.md` for the table mapping. The per-study guides describe each experiment’s inputs and the results available for comparison.

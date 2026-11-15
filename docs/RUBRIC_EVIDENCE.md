# Rubric evidence map

No grade is promised. Paths refer to executed evidence where available.

| Requirement | Evidence | Limit |
|---|---|---|
| Problem and requirements | report/main.tex section 1 | operational availability assumptions need confirmation |
| Design and ML workflow | section 2; src/data.py, pipeline.py | random order split, not temporal |
| Implementation | section 3; src/run.py; tests/test_pipeline.py | local Python environment |
| Experiments and results | section 4; results/tables/comparison.csv; figures | bounded subset, historical holdout |
| Discussion | section 5; report/analysis.tex; DEFENSE_GUIDE.md | descriptive, not causal |
| Conclusion | section 6 | no deployment effectiveness claim |
| Leakage and reproducibility | group-subset-v1; group/CV/imputation tests; manifest hashes | raw CSV supplied privately |
| Representativeness | sampling_categories.csv, sampling_numeric.csv, sampling_groups.json | marginal checks only |
| Order vs item evaluation | *_order_metrics.json and *_confusion.csv | fixed aggregation/threshold |
| Time-feature ablation | time_ablation_cv.csv | A-selected settings, reused training CV |
| Error analysis | errors_by_Shipping_Mode.csv; tree rules; status cross-tabs | no holdout-driven tuning |
| Historical evidence | results/historical/2680607 | preserved, superseded EDA population |
| Submission | LaTeX sources, AI_USAGE.md | PDF/compiler/template and actual team details pending |

Execution results and clean-export checks: REPAIR_VERIFICATION.md.

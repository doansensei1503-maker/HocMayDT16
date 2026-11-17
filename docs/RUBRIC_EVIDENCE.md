# FIT4013 report requirements and evidence

The official six-section sequence is from `docs/fit4013_extracted.txt`,
section 2.2. Results below are preserved project evidence, not new training or
independent validation. Source locations are cited for review.

| Required section | Evidence | Findings and limits |
|---|---|---|
| 1. Đặt vấn đề và phân tích yêu cầu | `report/main.tex`, section 1; `report/analysis.tex` | DataCo source, target/timing, row/order distinction, dimensions, label counts, missing values and canceled-order caveat. |
| 2. Thiết kế giải pháp và quy trình học máy | `report/main.tex`, section 2; `configs/default.json`; `src/pipeline.py` | Group split and CV, leakage controls, allowlist, A/B pipelines, baseline and search ranges. Does not test temporal or unseen-customer generalization. |
| 3. Phân tích mã nguồn và chức năng | `report/main.tex`, section 3; `src/`; `notebooks/`; `docs/REPAIR_VERIFICATION.md` | Responsibilities of modules/notebooks and previously recorded tests (14 passed in the main workspace; clean export: 13 passed, 1 expected private-data skip). Not rerun for this update. |
| 4. Thử nghiệm và kết quả | `report/generated.tex`; `results/tables/comparison.csv`; `results/figures/` | Six pre-existing model/flow rows, CV and historical holdout row metrics, confusion matrices for all six configurations, model comparison and all eight existing EDA figures. 5999 rows (3.32% of data); the holdout is already observed. |
| 5. Thảo luận và so sánh | `report/analysis.tex`; `report/repair_analysis.tex`; `results/tables/*_order_metrics.json`; `results/tables/time_ablation_cv.csv` | Explains group-level averaging, Dummy's slightly higher equal-order F1 despite predicting all positive, the fixed-parameter CV ablation and Standard Class false negatives. Descriptive only; no causal, operational or future-generalization claim. |
| 6. Tổng kết và hướng phát triển | `report/main.tex`, section 6 | Summarizes historical results, highlights the severe Standard Class recall limitation and lists further validation. No deployment-readiness claim. |

## Current artifact status — 2026-11-17 completion

- Report: `report/final_report.pdf`, 40 pages A4, three-pass XeLaTeX; full visual
  review and artifact checks recorded in `docs/REPORT_VERIFICATION.md`.
- Final content lives in `report/sections/01_problem.tex` through
  `06_conclusion.tex`; main no longer inputs the older generated/analysis files.
  Six sections include equations, all 15 existing result images, pipeline diagram,
  13 tables, order evaluation, ablation and limitations. No retraining was done.
- Two covers use the unchanged logo extracted from the supplied Word file;
  identities are supplied and matched. Lecturer matches the course requirements.
- Actual contributions remain unconfirmed; the assignment table is explicitly
  proposed. See `TEAM_ASSIGNMENT_PROPOSED.md`.
- Official LaTeX template is unavailable. Do not claim template compliance.
- Slides remain a previously built, partially inspected nine-page deck; this
  report update does not certify the entire deck or update its team identity.
- Instructor approval of the repository and human final review remain necessary.

See `STATUS.md`, `FINAL_SUBMISSION_CHECKLIST.md`, and `report/README.md`.

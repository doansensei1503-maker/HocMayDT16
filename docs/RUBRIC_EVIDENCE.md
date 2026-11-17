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

## Current artifact status

- **PDF: PENDING.** MiKTeX 25.12 and XeLaTeX are installed in the user profile,
  but the first report build stopped at missing `infwarerr.sty`. No PDF was
  generated or visually inspected. No further installation or compilation is
  being attempted per the user's instruction.
- **Official template: BLOCKED.** The official course template is not available
  in the repository or provided materials. `report/main.tex` is provisional,
  not template-compliant by claim.
- **Team information: PENDING.** Verified member names, student IDs and actual
  contributions are absent. Do not fabricate them or infer roles from Git
  authorship.
- **Slides: SOURCE UPDATED; PDF PENDING.** `slides/presentation.tex` now includes
  historical equal-order metrics and sample coverage. It has not been compiled
  or visually reviewed.
- **Repository: CONFIRM.** The configured remote is
  `doansensei1503-maker/HocMayDT16`; confirm instructor approval.

Build instructions and preflight checks are in `README.md` and
`scripts/build_report.ps1`. The script does not invoke MiKTeX package
installation. Complete `docs/FINAL_SUBMISSION_CHECKLIST.md` before submission.
No grade is promised.

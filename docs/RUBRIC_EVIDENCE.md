# FIT4013 report requirements and evidence

Source of required report structure: the course instructions extracted to
`docs/fit4013_extracted.txt`, section 2.2. The report must use these six
sections in this exact order. The evidence below is from existing project
artifacts; it is not a new experiment or independent validation.

| Required section | Evidence in report | Supported findings / limits |
|---|---|---|
| 1. Đặt vấn đề và phân tích yêu cầu | `report/main.tex`, section 1 | DataCo source, prediction timing, target definition, row/order unit, dataset dimensions, class counts and missingness. Missing fields are excluded; label 0 includes canceled orders. |
| 2. Thiết kế giải pháp và quy trình học máy | `report/main.tex`, section 2; `configs/default.json`; `src/pipeline.py` | Group split and CV, leakage controls, allowlist, A/B features, algorithms and search ranges. Results apply to a bounded random group split, not future or unseen-customer generalization. |
| 3. Phân tích mã nguồn và chức năng | `report/main.tex`, section 3; `src/`; `notebooks/`; `docs/REPAIR_VERIFICATION.md` | Module/notebook responsibilities and historical test evidence (14 passed in the workspace; 13 passed and 1 expected private-data skip in a clean export). Tests were not rerun for this update. |
| 4. Thử nghiệm và kết quả | `report/main.tex`, section 4; `report/generated.tex`; `results/tables/comparison.csv`; `results/figures/` | Real-data baseline and A/B results, CV/test metrics and confusion matrices. 5999-row subset; the holdout is already observed and is not fresh independent evidence. |
| 5. Thảo luận và so sánh | `report/analysis.tex`; `report/repair_analysis.tex`; `report/main.tex`, section 5 | Error denominators and model tradeoffs, order-level metrics, sampling differences and fixed-parameter calendar ablation. Descriptive only; selection optimism, one known split, no causal or future-generalization claim. |
| 6. Tổng kết và hướng phát triển | `report/main.tex`, section 6 | Summarizes historical row- and order-level outcomes, highlights Standard Class false negatives and lists further validation. No deployment-readiness claim. |

## Submission blockers

- **Template/PDF: BLOCKED.** The official course template was not supplied or
  found in the repository. XeLaTeX, pdfLaTeX, latexmk and Tectonic were not
  available on PATH or the checked standard Windows install paths. No PDF was
  compiled or visually inspected. `report/main.tex` is prepared source, not a
  claim of template compliance or successful compilation.
- **Team details: BLOCKED.** Verified member names and actual contributions
  have not been supplied. Add them only after confirmation; do not fabricate
  names, contributions or commit history.
- **Repository approval: CONFIRM.** The current remote is
  `doansensei1503-maker/HocMayDT16`; the team must ensure it is approved by the
  instructor.
- **Historical test status.** Test outcomes in
  `docs/REPAIR_VERIFICATION.md` and this map are prior evidence. No fresh
  independent validation is claimed.

No grade is promised. Passing a rubric evidence map does not replace checking
the compiled PDF, official template, team contribution evidence or oral defense.

# Submission status — 2026-11-17

## Current decision: NOT READY TO SUBMIT

- The six required report sections appear in the official order in
  `report/main.tex`. Each has source-backed analysis or experiment results; see
  `docs/RUBRIC_EVIDENCE.md`.
- The report is still a working article source, not the official FIT4013
  template. No official template file was supplied or found in this repository.
- XeLaTeX, pdfLaTeX, latexmk and Tectonic are unavailable on PATH; checked
  standard Windows install paths also had no compiler. No report PDF has been
  compiled or visually inspected. Do not claim PDF/template completion.
- Actual member names and contributions are missing. The team must provide and
  verify them; none are to be inferred or fabricated.

## Existing evidence (historical; not fresh independent validation)

- Repair and clean-export test outcomes are recorded in
  `docs/REPAIR_VERIFICATION.md`: 14 passed in the main workspace; a clean source
  export had 13 passed and 1 expected private-data skip. The report was not
  rerun for this readiness update.
- The real-data experiment used 5999 of 180519 rows, grouped into 4823 train
  rows/1690 orders and 1176 test rows/423 orders. The selected tree_B's
  historical row-level test F1 was 0.7098; equal-order F1 was 0.7100. These
  reuse the already observed holdout and are not new independent evidence.
- The Standard Class row-level recall was 0.0236 (248 false negatives among 254
  positive rows). This limits any operational conclusion.
- Historical artifacts remain preserved under `results/historical/2680607`.
  Sampling, order-level and fixed-parameter calendar-ablation caveats are
  documented in `docs/REPAIR_VERIFICATION.md` and the report.

## Remaining submission work

1. Obtain the official course LaTeX template and required compiler/package/font
   setup; transfer the prepared report content without claiming an unverified
   build.
2. Compile the PDF, resolve build/layout issues, and inspect figures, tables,
   fonts, and references.
3. Add verified member names and real contribution details; confirm the target
   GitHub repository is the one approved by the instructor.

No training, notebook execution, EDA, or prior test suite was repeated for this
status update.

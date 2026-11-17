# Submission status — 2026-11-17

## Current decision: NOT READY TO SUBMIT

**PDF = PENDING; Official Template = BLOCKED; Team Information = PENDING.**

- **PDF: PENDING.** No final PDF was generated or inspected. The first XeLaTeX
  run stopped because `infwarerr.sty` is missing. Per the user's latest
  instruction, no further MiKTeX package installation, Console interaction or
  PDF compilation is being attempted.
- **Official template: BLOCKED.** The course instructions require its official
  LaTeX template, but no template file was supplied or found in this repository.
  `report/main.tex` is a provisional article source and does not claim template
  compliance.
- **Team information: PENDING.** Verified member names, student IDs and actual
  individual contributions have not been supplied. The author field is an
  explicit placeholder; repository Git authorship is not proof of team roles.
- **Six report sections: COMPLETE AS SOURCE.** All six required sections are in
  the required order, supported by existing results and constraints. The report
  still needs official-template integration and team details.

## Toolchain state

MiKTeX 25.12 was installed in the current user's profile using WinGet, and
XeLaTeX starts successfully. The report compile then encountered missing
`infwarerr.sty`. MiKTeX displayed a package-install prompt whose only available
scope was Admin; that install was canceled to avoid modifying the system-level
TeX installation. No MiKTeX Console interaction, further package installation
or retry is being performed. `scripts/build_report.ps1` now preflights required
TeX files and will stop with a clear message instead of opening the Console.
Times New Roman and Arial are present on this machine.

## Existing empirical and test evidence

- The experiment used 5999 of 180519 rows (3.32%) and 2113 of 65752 orders
  (3.21%). Historical test metrics reuse the already observed holdout; they are
  not new independent validation.
- tree_B historical row F1 is 0.7098; equal-order F1 is 0.7100. Dummy's
  equal-order F1 is 0.7123 because it predicts every order positive; its
  equal-order Accuracy and Precision are both 0.5532. These scores do not
  establish operational utility.
- Standard Class has 248 false negatives among 254 positive rows
  (FNR=0.9764), a material limitation.
- Historical tests and clean-export checks remain recorded in
  `docs/REPAIR_VERIFICATION.md`. No ML tests, training, EDA or notebooks were
  rerun for this report update. Targeted source/build-script static checks and
  the failed first LaTeX attempt are recorded there separately.
- Historical outputs remain under `results/historical/2680607`.

## Remaining submission work

1. Obtain the actual course template and a working user-level LaTeX setup that
   contains the required packages; build and visually inspect the PDF and slides.
2. Obtain verified names, student IDs and actual contribution statements from
   the team, then check the approved GitHub destination.
3. Complete `docs/FINAL_SUBMISSION_CHECKLIST.md` before submission.

No retraining, notebook execution, EDA or historical test rerun was performed.

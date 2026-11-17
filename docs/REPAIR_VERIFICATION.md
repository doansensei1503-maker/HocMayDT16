# Repair verification ? 2026-11-16

- Correct repository: https://github.com/doansensei1503-maker/HocMayDT16, main.
  Original origin was DT16HocMay; intended remote had no branches.
- Backup checkpoint e66ff6b5801b2ea04aabb873b4de0ffcdcf3e357 pushed and matched
  refs/heads/main. Initial one-commit history: 2680607; working tree was clean.
- Reviewed all 112 initial tracked files and the one-commit history. No credential
  pattern/email matches; largest tracked file 70624 bytes. Raw data/ZIP, models,
  private split rows, environments and caches remain excluded.
- Python AST checks: 14 source/script/test files passed. Six report sections present.
- Main workspace: 14 pytest tests passed, 6 warnings, 57.41 seconds.
- Clean source export, run from its own directory with no data or prior outputs:
  13 passed, 1 expected private-data skip, 6 warnings, 67.46 seconds.
  Used installed dependencies; a fresh isolated dependency install was not tested.
- The smoke runner creates missing report outputs; finalization now creates
  data/processed. A no-run clean export exits clearly with NOT RUN.
- Initial sandbox attempts failed at Windows temp/Jupyter ACL access; verification
  succeeded with approved execution outside the sandbox. Warnings include seaborn
  deprecation and undefined Dummy fixture precision, plus Jupyter platform warnings.
- All four notebooks executed with real kernel outputs. Notebook 03 ran the bounded
  six-model real-data experiment with full-data sampling comparisons, order metrics,
  and the fixed-parameter A/B training-CV ablation. No full-data model training.
- Selected tree B order F1=0.7100; order confusion [[165,24],[92,142]].
  Historical row F1=0.709797. The test is already observed, not fresh validation.
- Fixed-parameter CV F1: K-NN A=0.666848, B=0.671415;
  tree A=0.674115, B=0.690374. Fold validation uses test_* column names in the CSV.
  Training-CV reuse has selection optimism; no causal/time-generalization claim.
- Largest marginal category fraction difference: 0.022724,
  feature Customer Segment, category Consumer. Mean items/order:
  full 2.74545 vs subset 2.83909. Sampling representativeness remains limited.
- LaTeX compiler unavailable (xelatex/pdflatex/latexmk/tectonic absent from PATH).
  Official template absent. PDF compilation/layout validation NOT RUN.
- Real team membership and contributions remain for the team to supply.

Persisted evidence verification and final Git verification are recorded below.

- Persisted real-data CV/test metrics matched the prior run within 1e-12.
- All notebooks executed without cell errors; six models; real group overlap zero.
- Data SHA and exact protocol split checked; notebook/train EDA tables identical.
- Final candidate-file scan: no credential-pattern or email matches; no files >=10 MB.
- Final Git commit and remote SHA are reported in the delivery response (a commit
  cannot contain its own SHA). No forced push or history rewrite used.

- Actual clean local Git clone at f048570: 13 passed, 1 expected raw-data skip,
  6 warnings in 61.11 seconds. Includes synthetic end-to-end training/publication.
  Full private-data retraining in the clean clone was not repeated; real-data
  reproduction and SHA/split checks were performed in the main workspace.

## 2026-11-17 report completion update

- Readiness changes preserve all experiment artifacts and historical outcomes;
  no training, EDA, notebook execution or test suite was rerun.
- Confirmed the six required section headings and order against the FIT4013
  instructions. Report source now includes all 15 existing report figures
  (eight train-only EDA figures, six model confusion matrices and one model
  comparison), plus the existing comparison table and documented order/ablation
  tables. Figure/table paths, labels, citation keys and cross-references passed
  static checks.
- Rechecked `comparison.csv`, `tree_B_order_metrics.json` and
  `dummy_A_order_metrics.json` against report metrics. Stored results remain:
  tree_B row F1=0.7098 and equal-order F1=0.7100; Dummy equal-order F1=0.7123
  because it predicts every order positive. The 5999-row (3.32%) sample,
  historical holdout reuse, canceled-label caveat and Standard Class false
  negatives are explicitly described.
- Verified the Mendeley Data DOI metadata via DataCite: Fabian Constante is the
  creator; Fernando Silva and António Pereira appear as contributors. Corrected
  the bibliography to avoid listing contributors as co-creators. Confirmed the
  Kaggle page title and uploader metadata via its public API.
- Installed MiKTeX 25.12 in the current user's profile; XeLaTeX starts. The
  first report compile stopped at missing `infwarerr.sty`. MiKTeX offered only
  Admin scope in its package prompt; that install was canceled. Per the user's
  subsequent instruction, no further Console interaction, installation or PDF
  compilation was attempted. PDF remains PENDING; no output PDF is claimed.
- Added `scripts/build_report.ps1` with syntax validation, input/package
  preflight, two-pass XeLaTeX, logs and output checks. It stops before invoking
  XeLaTeX if the known missing package is unresolved; it does not install
  packages or open MiKTeX Console.
- Static checks passed for the report-generator Python syntax, PowerShell build
  script syntax, six-section order, citations, labels/cross-references, all 15
  image paths, table/figure environments and stored metric consistency. No
  fresh ML tests were run.

## XeLaTeX build update

- Located MiKTeX 25.12 / MiKTeX-XeTeX 4.16 in the current user's
  `MiKTeX-New\miktex\bin\x64` directory; `xelatex` was not on PATH. `ltxcmds`
  was already installed. Installed missing `infwarerr`, `babel-vietnamese`,
  `geometry`, `booktabs`, `kvsetkeys`, `kvdefinekeys`, `pdfescape`, `hycolor`,
  `refcount`, `gettitlestring`, `kvoptions`, `stringenc`, `intcalc`, `bitset`,
  `bigintcalc`, `rerunfilecheck`, `uniquecounter`, `beamer`, `translator` and
  `amscls` with the official `miktex packages install` CLI only; no interactive
  MiKTeX Console or installer was used.
- Built directly with XeLaTeX twice per source, passing
  `--disable-installer -interaction=nonstopmode -halt-on-error -file-line-error`
  and outputting to `build/`. Report: `report/build/final_report.pdf`, 12 pages,
  608152 bytes. Slides: `slides/build/presentation.pdf`, 9 pages, 68476 bytes.
- The final report was visually checked across all 12 pages, including page 12
  after a bibliography alignment adjustment. Tables, figures, page breaks and
  Vietnamese glyphs are visible; Times New Roman fonts are embedded. The slide
  deck was visually spot-checked, including its opening content and CV-results
  table, but not every page.
- PDF text extraction confirmed the expected Vietnamese section headings and
  bibliography. Both final logs have no unresolved citations/references and no
  overfull/underfull box warnings. They retain a nonfatal Babel warning that
  Vietnamese hyphenation patterns were not preloaded; do not claim that
  hyphenation is configured. The report log confirms 12 pages and the slide log
  confirms 9 pages.
- A `kpsewhich` lookup in the existing helper triggered a hidden
  `miktex-console.exe --hide --check-updates` process. It was stopped by its
  specific PID; no user-facing Console interaction or package installation was
  performed through it. Updated `scripts/build_report.ps1` to avoid `kpsewhich`,
  search the user's MiKTeX program folders, and pass `--disable-installer`.
- The updated PowerShell helper passed the PowerShell parser syntax check; it
  was not rerun to avoid duplicating the already verified direct builds.
- No model training, notebook execution, EDA, ML tests or experiment artifacts
  were changed or rerun. The PDFs are provisional outputs; the official course
  template and verified team information remain unavailable.

## Hoàn thiện báo cáo 35–40 trang — 17/11/2026

Các trạng thái PDF 12 trang/tên nhóm chưa có phía trên là lịch sử của bản trước.
Bản hiện tại có PDF 36 trang và danh tính do người dùng cung cấp; sáu phần được
mở rộng theo artifact thực. Xem `REPORT_VERIFICATION.md` cho kiểm tra số liệu,
font, bố cục từng trang và tài liệu tham khảo. Template chính thức vẫn chưa có;
phân công vẫn là đề xuất chưa xác nhận. Không huấn luyện lại hoặc tạo metric mới.

## Cập nhật hai bìa theo quy chuẩn mới — 17/11/2026

Bản hiện tại 37 trang, tiêu đề bìa 15 pt đậm, chữ còn lại/bảng nhóm 14 pt;
phần thân Times New Roman 13 pt, H1/H2/H3 14/13/13. Đối chiếu Word trang 1–2,
kiểm tra font PDF và hình ảnh ghi ở `COVER_UPDATE_VERIFICATION.md` cùng
`COVER_TYPOGRAPHY_AUDIT.json`. Không đổi nội dung sáu phần hoặc kết quả thực nghiệm.

## Đối chiếu video — bản 40 trang

Kiểm chứng hiện hành nằm ở `VIDEO_REVIEW.md` và bốn JSON audit của PDF cuối.
Đã đọc các trang quy định từ trình phát, áp dụng phần phù hợp với FIT4013 và
quy chuẩn người dùng; không khẳng định đã có transcript/lời nói đầy đủ.
Không thay code ML hay số liệu, không huấn luyện lại. Các mốc PDF trước là lịch sử.

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

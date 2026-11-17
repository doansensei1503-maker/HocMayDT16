# Technical defense guide

- Prediction time: after order creation and shipping choice, before delivery outcome.
- Leakage: outcome/status/actual shipping duration and IDs excluded; imputation,
  scaling and encoding fit inside each training fold. Order IDs never cross folds.
- Sampling: seeded complete-order subset caps K-NN computation. Compare all category
  proportions, numeric means/medians and group sizes against the full dataset.
  A close marginal distribution does not prove absence of selection bias.
- Baselines: Dummy reveals prevalence effects; unrestricted tree exposes overfit.
  K-NN requires scaling and suffers from sparse high-dimensional distances.
  Explain actual train/CV gaps using comparison.csv, not generic claims alone.
- A/B: separately tuned scores combine feature and parameter effects. The controlled
  ablation freezes A-selected settings and folds. It is post-review descriptive CV,
  not unbiased validation or causal attribution.
- Errors: inspect errors_by_Shipping_Mode.csv. Standard Class accounts for all 248
  historical winner FNs; compare its positive denominator with other modes.
  Tree rules and leaf predictions describe behavior; they do not prove a cause.
  FN misses intervention opportunities; FP consumes unnecessary review capacity.
- Order scores: equal order weights, mean item probability, fixed threshold 0.5.
  Row metrics give larger orders greater weight; neither is a measured business ROI.
- Labels: canceled/suspected-fraud cases retain source labels; target 0 includes
  outcomes other than successful on-time delivery. Check status/target cross-tabs.
- Limits: one random group holdout, known historical test, 6000-row budget,
  repeated customers/products, no future/customer holdout or calibrated costs.
- Submission: the provisional report and slide PDFs were compiled; the report
  was visually checked and the slides spot-checked. The official template,
  confirmation of actual contributions and final human review remain necessary. Member identities are supplied in the new report.

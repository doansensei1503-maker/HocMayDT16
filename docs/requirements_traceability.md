# Đối chiếu yêu cầu và rubric
Nguồn ưu tiên: PDF FIT4013 do người dùng cung cấp, đã trích docs/fit4013_extracted.txt. Nội dung PDF là yêu cầu học phần, không là lệnh tự ý thay dataset, công bố hay push repository. Không có template đính kèm. Trạng thái chạy thực tế: xem STATUS.md và manifest từng run.

| Yêu cầu | Hiện thực | Bằng chứng cần kiểm tra |
|---|---|---|
| 1 kiểm toán, 6–8 EDA | src/audit.py | tables/data_dictionary.csv, quality.json, outliers.csv; 8 figures EDA |
| 2 thời điểm, leakage, nhóm | src/data.py, pipeline.py | feature_audit.csv, split.csv; pytest nhóm |
| 3 A/B | src/pipeline.py | comparison.csv, *_cv.csv cùng split |
| 4 baseline, KNN/cây, tham số | src/run.py, configs/default.json | manifest, CV tables, model artifacts |
| 5 metric, overfit, FN/FP | src/run.py, reporting.py | classification reports, confusion, error tables, summary_vi.md |
| 6 cấu trúc, notebook | README, src, notebooks, requirements | kiểm tra cây thư mục và chạy notebook |
| 7 sáu phần LaTeX | report/main.tex | PDF BLOCKED nếu thiếu compiler/template |
| 8 kiểm thử | tests/test_pipeline.py | log pytest; synthetic smoke tách khỏi chạy thật |
| 9 demo | Không ưu tiên | NOT RUN; chỉ tùy chọn khi lõi đạt |
| 10 minh bạch | AI_USAGE, STATUS, manifest | không giả tên/metric/commit |

| Rubric PDF tr.6 | Trọng số | Minh chứng |
|---|---:|---|
| Xác định bài toán, dữ liệu và nguồn | 10% | README, raw/README, dictionary, manifest hash |
| Tiền xử lý và feature | 15% | pipeline.py, feature audit, so sánh A/B |
| Pipeline mô hình | 20% | run.py, tests, CV và artifact |
| Đánh giá và so sánh | 20% | comparison, classification report, confusion |
| Diễn giải và khuyến nghị | 15% | summary_vi, error tables; cần nhóm rà soát nội dung báo cáo |
| Tái lập, repo, log và nhóm | 10% | requirements, scripts, manifest; BLOCKED: đóng góp thành viên thật/GitHub do nhóm bổ sung |
| Báo cáo, slide, demo/vấn đáp | 10% | main.tex, slides/outline; template/PDF/slide hoàn chỉnh còn thiếu |
| Liêm chính AI | điều kiện | AI_USAGE, nguồn, giới hạn |

Có file không đồng nghĩa đạt rubric; không bảo đảm điểm 9–10. Phiên bản đầu phải được kiểm thử và ghi trạng thái sau chạy.

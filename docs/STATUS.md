# Kiểm toán và trạng thái cuối phiên

## COMPLETED — đã xác minh bằng thực thi
- Đã đọc PDF FIT4013 năm 2026–2027; văn bản trích ở fit4013_extracted.txt, yêu cầu/rubric ở requirements_traceability.md.
- Dữ liệu thật tải từ link Kaggle trong PDF (slug có -analysis), không dùng dataset thay thế. Đã đọc hai CSV, schema và nhãn, lưu SHA256 trong results/tables/experiment_manifest.json.
- Kiểm toán toàn bộ 180519×53: 65752 đơn, 45902 đơn nhiều dòng, 0 dòng trùng hoàn toàn, 0 đơn nhãn mâu thuẫn; missing/cardinality/outlier/dictionary/feature audit và cross-tab nhãn đã xuất.
- Thí nghiệm tập con 5999 dòng thuộc 2113 đơn; train 4823 dòng/1690 đơn, test 1176 dòng/423 đơn. CV 3 fold trên train theo nhóm, seed42. Không cùng đơn ở train và test.
- Baseline cây A, Dummy A, K-NN A/B, cây A/B; bảng toàn bộ grid, metric, confusion, classification report, thời gian tìm kiếm+fit lại và dự đoán, sáu model save/load.
- Chọn tree_B bằng CV F1=0.705753 trước khi đánh giá test. Test Accuracy=0.732993, Precision=0.853333, Recall=0.607595, F1=0.709797; TN478/FP66/FN248/TP384. Toàn bộ FN thuộc Standard Class. Không tuyên bố model đã sẵn sàng vận hành.
- 12 tests pass (43.22 giây); docs/pytest_output.txt. Có 6 warning: seaborn deprecation và precision undefined của Dummy trong một số fold fixture; không phải lỗi test, không phải metric dữ liệu thật bị bịa.
- Cả 4 notebook đã thực thi có output thật, không lỗi cell; notebook 03 thực hiện lần chạy thứ hai. Đối chiếu tái lập và kiểm tra artifact ở docs/evidence_verification.txt.
- Kết quả review được công bố an toàn vào results/tables, results/figures; model chọn ở results/models/selected.joblib (gitignore); split cục bộ ở data/processed/split.csv (gitignore).
- Báo cáo LaTeX tiếng Việt đủ 6 phần, nội dung phân tích thực tế, bảng/hình được sinh; có nguồn Beamer slide. Git cục bộ đã khởi tạo, không commit/push.

## BLOCKED — đầu vào/công cụ chưa có
- Không có template LaTeX chính thức kèm tài liệu; không tìm thấy xelatex/pdflatex/latexmk/tectonic trên PATH. Chưa có PDF báo cáo/slide được biên dịch và kiểm tra bố cục.
- Chưa có danh sách thành viên, đóng góp thật hoặc remote GitHub được giảng viên thống nhất. Nhóm phải tự bổ sung và bảo vệ; không tạo lịch sử đóng góp giả.

## NOT RUN / ngoài phạm vi thực nghiệm hiện tại
- Chưa huấn luyện toàn bộ 180519 dòng. Tập con là giới hạn tài nguyên công khai, mọi mô hình so sánh cùng subset/split. max_rows=null cho phép chạy toàn bộ nhưng K-NN có thể rất chậm.
- Chưa có temporal holdout, đánh giá khách hàng mới, calibration, tối ưu threshold theo chi phí, CI bootstrap theo nhóm hoặc thử nghiệm hiệu quả vận hành. Không suy rộng kết quả random group split sang tương lai.
- Streamlit tùy chọn chưa triển khai; ưu tiên lõi học thuật.
- scripts/reproduce.ps1 đã được tạo; chưa chạy nguyên khối script này. Các thành phần pytest, src.run và finalize_evidence đã chạy riêng thành công; pipeline còn được chạy qua notebook.

## Các lệnh đã chạy
- py -m pip install pypdf (7.0.1); đọc PDF bằng pypdf, xác minh annotation dataset.
- Tải ZIP từ Kaggle public API, kiểm tra ZIP và giải nén đúng hai CSV.
- py -m pytest -q --tb=short (lần cuối 12 passed).
- py -X utf8 -m src.run --config configs/default.json.
- py -X utf8 scripts/execute_notebooks.py (cả 4 notebook).
- py -X utf8 -m scripts.finalize_evidence.
- py -X utf8 -m scripts.verify_evidence.
- git init; git status --short. Không commit/push.

## Chạy tiếp
Tại thư mục gốc: powershell -ExecutionPolicy Bypass -File scripts/reproduce.ps1. Hoặc py -m src.run --config configs/default.json để chỉ thực nghiệm. Cài requirements-notebooks.txt trước khi chạy notebook ở máy khác. Khi có compiler/template, chuyển nội dung rồi biên dịch theo README; cần cập nhật các đoạn số liệu tĩnh nếu đổi config.

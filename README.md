# FIT4013 – Đề tài 16: Dự đoán nguy cơ giao trễ

Thời điểm dự đoán: sau khi tạo đơn và chọn phương thức vận chuyển, trước kết quả giao thực tế. Đơn vị mô hình là order-item; đánh giá theo dòng nhưng chia train/test và CV theo Order Id. Không diễn giải metric theo dòng thành hiệu quả theo đơn hàng.

## Chạy lại (PowerShell, tại thư mục gốc)
```
py -m pip install -r requirements.txt
py -m pytest -q
py -m src.run --config configs/default.json
```
Chỉ chạy lệnh cuối khi có đủ CSV và mô tả trong data/raw. Đọc docs/STATUS.md để biết trạng thái kiểm chứng. Kết quả lưu ở thư mục run riêng, không ghi đè kết quả cũ. Mỗi run lưu SHA256 dữ liệu, phiên bản, config, split, tham số, metric và thời gian. Model joblib chỉ nạp từ nguồn tin cậy.

## Quyết định phương pháp
- Allowlist bảo thủ; cột lạ tự động bị loại, không tự suy đoán là an toàn. Mô tả gốc được đưa vào data dictionary để người học kiểm tra trước khi bảo vệ.
- Luồng A: median/mode, one-hot, StandardScaler. Luồng B: thêm lịch đặt hàng (tháng, thứ, giờ) từ thời điểm tạo đơn; giả thuyết lịch đặt hàng phản ánh lịch vận hành. Không dùng ngày giao hàng. Không khẳng định B tốt hơn trước khi chạy.
- GroupShuffleSplit 80/20, StratifiedGroupKFold 3 folds trên train; không cùng Order Id ở hai tập. Khách hàng/sản phẩm có thể lặp: chỉ đo khái quát sang đơn hàng mới trong cùng quần thể, không sang khách hàng mới hoặc tương lai. Chưa phải temporal validation.
- Giới hạn mặc định 6000 dòng bằng lấy mẫu nhóm trước chia tập để K-NN chạy được trên máy cá nhân. Đây là thí nghiệm tập con, không phải toàn bộ dữ liệu. Có thể đặt max_rows=null để dùng toàn bộ; K-NN có chi phí dự đoán cao. Tất cả mô hình dùng cùng split và subset.
- Tối ưu F1 lớp 1 bằng CV, báo Recall và Precision để cân đối bỏ sót/cảnh báo nhầm. Test chỉ dùng sau khi khóa toàn bộ cấu hình; không xếp hạng để chọn mô hình bằng test. Không chọn threshold từ test.
- Baseline Decision Tree mặc định + A và Dummy most_frequent. Grid nhỏ cho K-NN (k, weights, metric) và cây (depth, leaf, criterion), không thay bằng mô hình nâng cao.

Các notebook gọi code trong src. Báo cáo hoàn chỉnh ở `report/final_report.pdf`
(40 trang A4), nguồn tại `report/main.tex` và `report/sections/`. Hai bìa có logo
trích nguyên từ Word và thông tin nhóm do người dùng cung cấp. Chưa có template
LaTeX chính thức để đối chiếu; phân công là đề xuất chưa xác nhận đóng góp thực tế.
Không huấn luyện lại khi biên tập báo cáo. Dữ liệu thô/model/split riêng được gitignore.

## Notebook và báo cáo
```
py -m pip install -r requirements-notebooks.txt
py -X utf8 scripts/execute_notebooks.py
py -X utf8 -m scripts.finalize_evidence
```
Lệnh execute_notebooks chạy cả bốn notebook; notebook 03 tạo một run thực nghiệm mới. scripts/create_notebooks.py là công cụ tạo lại bản notebook chưa chạy, sẽ thay output notebook; không cần chạy khi tái lập. scripts/finalize_evidence xuất bổ sung cross-tab nhãn, thống kê nhóm, luật cây và bảng giải thích; scripts/reproduce.ps1 gọi bước này sau tests và training.

## Build báo cáo và slide

Cần XeLaTeX (MiKTeX hoặc TeX Live) và font Times New Roman; slide dùng thêm
Arial. Tại thư mục gốc, chạy:

```powershell
.\scripts\build_report.ps1
.\scripts\build_report.ps1 -BuildSlides
```

Lệnh thứ nhất tạo `report/final_report.pdf`; lệnh có `-BuildSlides` còn tạo
`slides/presentation.pdf`. Auxiliary files và log nằm trong `report/build/` và
`slides/build/`. Helper tìm XeLaTeX trên PATH hoặc trong thư mục cài MiKTeX của
người dùng, truyền `--disable-installer` và không gọi `kpsewhich`; package còn
thiếu được báo trong log thay vì cài tự động. Nếu cần, cài package bằng CLI
chính thức của MiKTeX. Việc build không xác nhận template chính thức hay thay
thế việc kiểm tra trực quan.

Các tệp `report/generated.tex`, `analysis.tex`, `repair_analysis.tex` là nguồn cũ,
được giữ để truy vết và không còn input vào main. Bảng mới được tạo từ artifact
sẵn có bằng `py scripts/report_tables.py`, kèm kiểm tra metric; không training.
Helper chạy XeLaTeX ba lượt. Xem [hướng dẫn báo cáo](report/README.md).

Video hướng dẫn đã được đối chiếu tại các trang quy định đọc rõ, xem
[đối chiếu video](docs/VIDEO_REVIEW.md). Bản 40 trang giữ sáu phần FIT4013,
áp dụng lề/giãn dòng/chú thích phù hợp và APA-style, không đổi thuật toán/số liệu.

## Submission readiness

**PDF = BUILT, 40 pages; Team identity = SUPPLIED; Contributions = PROPOSED;
Official Template = UNVERIFIED.**

Sáu phần đã hoàn thiện từ kết quả lịch sử. Phải xác nhận phân công/đóng góp thực
tế, template chính thức, repository được giảng viên chấp thuận và rà soát của
nhóm trước nộp. Slide 9 trang là bản cũ, chưa cập nhật thông tin nhóm trong
lần hoàn thiện báo cáo này. Xem `docs/STATUS.md` và checklist.

Kết quả nộp/review an toàn nằm ở results/tables và results/figures. Run riêng trong results/runs chứa split và model để kiểm toán cục bộ, được gitignore. Model không được commit. Khi làm lại với phiên bản code khác, giữ run cũ, hash dữ liệu và commit thật của nhóm; không tạo commit thay đóng góp thành viên.


## Repair verification (2026-11-16)
Protocol `group-subset-v1` is shared by training and EDA notebooks. It retains
historical subset/split semantics; reproduce with identical CSV hashes, row order,
config and dependency versions. Original artifacts and notebooks are preserved in
`results/historical/2680607`. Historical test observations are already known;
reruns verify reproducibility and are not independent unseen-test evidence.

New aggregate evidence: `sampling_categories.csv`, `sampling_numeric.csv`,
`sampling_groups.json`, `*_order_metrics.json`, and `time_ablation_cv.csv`.
Order evaluation averages item probabilities and applies the fixed 0.5 threshold,
with equal weight per order; inconsistent order targets block that diagnostic.
The controlled ablation fixes each algorithm's A-selected parameters for A/B on
the same training CV folds. Its scores are descriptive, with selection optimism;
they do not establish causal calendar benefits or generalization to future orders.
See `docs/RUBRIC_EVIDENCE.md` and `docs/DEFENSE_GUIDE.md`.

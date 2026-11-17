> Bản hiện hành dùng bảng trắng–đen: xem `MONOCHROME_TABLE_VERIFICATION.md`. Nội dung dưới đây ghi nhận lần chỉnh trước.

> Hồ sơ lần chuẩn hóa heading. PDF hiện hành sau chỉnh bảng: `TABLE_STYLE_VERIFICATION.md`; các JSON audit đã cập nhật theo PDF mới.

# Kiểm chứng heading và hoàn thiện báo cáo — 17/11/2026

PDF hiện hành: `report/final_report.pdf`, 40 trang A4.
SHA-256: `99cf01aa7350de63afe5901a47f2b91488d8523c5c75457fa4c4a7d20640f61d`.

## Thay đổi và kết quả

| Yêu cầu | Kết quả kiểm tra |
|---|---|
| H1 Times New Roman 14 pt, đậm, giữa, viết hoa | Đạt: đo 12 tiêu đề thực trong PDF; không nghiêng |
| Sáu chương tự động CHƯƠNG 1–6 | Đạt: tiêu đề đúng yêu cầu, mỗi chương bắt đầu trang mới |
| Mục lục và hyperlink | Đạt: sáu tiêu đề chương có tiền tố, link đúng trang; 128 liên kết nội bộ có đích hợp lệ |
| H2 13 pt đậm, H3 13 pt đậm nghiêng | Đạt: 49 H2; H3 cấu hình tập trung, nội dung hiện tại không có H3 |
| Lời mở đầu, phân công | Đạt: giới thiệu DataCo/K-NN/Decision Tree; hai cột, hai thành viên, ghi chờ xác nhận |
| Hai bìa riêng 15/14 pt, không số trang | Đạt: giống từng pixel bản trước; logo, khung, thông tin không đổi |
| Bảng và chú thích 13 pt | Đạt: 13 bảng, 14 hình; 27 chú thích, bảng trên/hình dưới |
| URL GitHub tại Chương 3 | Đạt: đầy đủ, nhấp được, trong lề |
| Đúng năm nguồn tham khảo | Đạt: fit, kaggle, dataco, knn, tree; tập cite đúng tập bibitem |
| Toàn bộ trang, font và tràn | Đạt: render và xem 40 trang; font nhúng, không ký tự thay thế, không chữ tràn trang |
| Bảo toàn thực nghiệm | Đạt: src/results/configs/notebooks/tests không đổi, không chạy lại ML |

Nguồn LaTeX giữ sáu tệp nội dung. `titlesec` quản lý H1/H2/H3 tập trung trong
`typography.tex`; macro `partstart` tạo section và nhãn chương tự động. Kiểu bìa
được giữ độc lập. Mục lục được giảm khoảng trắng giữa các mục chương từ 0,6em
xuống 0,2em để tránh trang thứ ba chỉ chứa một mục; không cắt nội dung khoa học
hoặc giảm font để đạt 40 trang.

Ba nguồn ngoài danh sách yêu cầu (pitfalls, cross-validation, metrics) đã bỏ.
Các câu tương ứng dẫn đến `src/data.py`, `src/pipeline.py`, hàm `metrics` của
`src/run.py`; không gán nhầm cho tài liệu K-NN hoặc cây. Năm mục còn lại giữ tên
nguồn, tác giả, DOI/URL; mô tả bằng tiếng Việt, trình bày tác giả–năm APA-style.
Danh mục được sắp theo tác giả, không phải số thứ tự.

## Kiểm chứng thực hiện

- `scripts/build_report.ps1`: XeLaTeX ba lượt, tạo 40 trang, không lỗi LaTeX,
  overfull/underfull box hoặc citation/reference chưa giải quyết.
- `scripts/verify_report_typography.py`, `verify_report_navigation.py`,
  `verify_video_layout.py`: đạt; JSON audit gắn đúng hash PDF trên.
- Xem đủ mười contact sheet gồm 40 trang; so hai bìa với raster đã duyệt trước.
- Các trang chương nằm tại trang PDF 7, 11, 17, 22, 33, 38; tài liệu tham khảo
  trang 40. Hai bìa không đánh số, tiếp theo i–iv, phần chính 1–34.

Còn cảnh báo Babel thiếu mẫu ngắt từ tiếng Việt và nhắc kiểm tra cập nhật MiKTeX;
không ngăn biên dịch. Cỡ nhỏ tự nhiên của chỉ số toán học và chữ có sẵn trong ảnh
biểu đồ được giữ nguyên; chữ thường/bảng/chú thích soạn bằng LaTeX đúng 13 pt.
Template FIT4013 chính thức chưa được cung cấp; phân công thực tế cần nhóm xác nhận.
Hồ sơ video trước đây vẫn chỉ xác minh phần hình hướng dẫn đã đọc, không khai báo
đã nghe toàn bộ video. Xem `VIDEO_REVIEW.md` cho phạm vi đó.

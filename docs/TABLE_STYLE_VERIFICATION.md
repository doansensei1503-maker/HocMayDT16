# Kiểm chứng hệ thống bảng biểu — 17/11/2026

PDF: `report/final_report.pdf`, 40 trang A4.
SHA-256: `7471bfb7c1d6f324688a8a262b6d69928906b3424733b205a1b510e665cce191`.

## Phạm vi và thiết kế

Đã chỉnh cả 13 bảng active trong frontmatter, sections và năm tệp tables;
nguồn cũ không được input vào báo cáo không được chỉnh lại. Hai bìa và bảng
bìa giữ nguyên quy chuẩn riêng 14/15 pt đã chốt.

Style tập trung tại `report/typography.tex`: Times New Roman 13 bp (đúng 13 pt
trong PDF), arraystretch 1,22, tabcolsep 6 pt, extrarowheight 1,2 pt. Dùng
`tabularx`, `array`, `booktabs` và `xcolor/colortbl`; header đậm nền RGB
230/236/241, quy tắc ngang xám xanh; không viền dọc hoặc màu hàng rối mắt.
Bảng dùng đúng chiều rộng vùng chữ; cột Y xuống dòng cho văn bản, cột r căn phải
cho số cùng số chữ số thập phân. Không scale bảng hoặc giảm font.

- Bảng 1: cột họ tên 3,6 cm, nhiệm vụ rộng hơn, hai thành viên; bỏ dòng chú thích
  lặp dưới bảng, giữ trạng thái dự kiến trong caption.
- Bảng 2: nhóm thông tin, biến minh họa, kiểu dữ liệu, vai trò, ghi chú; giữ các
  nhóm và ý nghĩa cũ, bổ sung tên biến từ hợp đồng `src/data.py` và metadata.
- Bảng 3: thuộc tính, kiểu lưu, số thiếu, tỷ lệ thiếu, hướng xử lý. Dtype/số thiếu
  đối chiếu `results/tables/data_dictionary.csv`; quyết định loại khỏi đầu vào
  theo `feature_audit.csv`. Cột mô tả hoàn toàn thiếu mang dtype float64 được
  giải thích, không diễn giải thành đặc trưng số hữu dụng.
- Bảng 4–7, 13: giữ nguyên các dòng và nội dung, nâng cấp header, đệm và căn cột.
- Bảng 8–12: sửa cả `scripts/report_tables.py` để đầu ra nhất quán; mô hình và
  luồng A/B tách riêng. Bảng 8 nhóm header CV/Test; bảng 8 và 10 in đậm cực đại
  từng thước đo, có giải thích. Dummy vẫn được in đậm Recall/F1 đơn khi đúng số.
  Bảng mức khớp train không đánh dấu cực đại là tốt nhất. Không đổi số hoặc thứ tự.

## Kiểm chứng

| Kiểm tra | Kết quả |
|---|---|
| XeLaTeX qua helper ba lượt | Thành công, 40 trang; không overfull/underfull hoặc cite/ref chưa giải quyết |
| Font ô bảng trong PDF | 13/13 bảng: Times New Roman 13 pt; header đậm, nền nhẹ |
| Vị trí bảng | 13/13 nằm trong vùng chữ, nguyên bảng trên trang, không tràn ô sau sửa xuống dòng |
| Caption / đánh số | 13 caption bảng 13 pt, phía trên; nhãn và tham chiếu giữ nguyên |
| Bảng sinh tự động | Kiểm tra sáu ma trận nhầm lẫn, metric, winner CV, F1 đơn, FN/FP nhóm đều đạt |
| Bảo toàn số | Đối chiếu mọi số thập phân và số lần xuất hiện trong năm bảng sinh với commit 9eba3fa: trùng |
| Tính lặp script | Chạy lại cho đầu ra giống từng byte; không thực thi huấn luyện |
| Điều hướng / heading | Audit đạt: sáu chương, 49 H2, mục lục và URL GitHub hoạt động |
| Trực quan | Đã xem đủ 40 trang trên 10 contact sheet và riêng 13 crop bảng ở mức 1,8x |
| Bìa / font nhúng | Hai bìa giống pixel bản trước; font nhúng, không ký tự thay thế hoặc chữ tràn trang |
| Mở PDF | Đã đóng tab cũ và mở đúng final_report.pdf trong VS Code |

Bảng 1–13 tại các trang PDF: 3, 8, 10, 12, 17, 21, 22, 23, 27, 31, 32, 32, 35.
Bằng chứng máy đọc: `TABLE_LAYOUT_AUDIT.json`, `COVER_TYPOGRAPHY_AUDIT.json`,
`REPORT_NAVIGATION_AUDIT.json`, `VIDEO_LAYOUT_AUDIT.json`, `PDF_REVIEW_AUDIT.json`.
Lệnh kiểm tra: `py scripts/verify_report_tables.py`, `verify_report_typography.py`,
`verify_report_navigation.py`, `verify_video_layout.py`.

Không thay src/results/configs/notebooks/tests, không huấn luyện lại, không thay
nội dung chuyên môn ngoài cách tổ chức và diễn giải metadata sẵn có trong bảng.
Cảnh báo Babel thiếu mẫu ngắt từ tiếng Việt và nhắc cập nhật MiKTeX còn tồn tại,
không cản trở biên dịch. Template chính thức và đóng góp thực tế vẫn chờ xác nhận
như hồ sơ trước; không tự khai báo đã được duyệt.

# Trạng thái báo cáo FIT4013 — 17/11/2026

**PDF: 37 trang A4, đã biên dịch và kiểm tra trực quan.**
**Template chính thức: chưa có để xác minh. Đóng góp thực tế: cần nhóm xác nhận.**

- Đầu ra: `report/final_report.pdf`; nguồn chính `report/main.tex` và sáu tệp
  `report/sections/`. Hai trang bìa không đánh số; bốn trang đầu dùng số La Mã,
  nội dung và tài liệu tham khảo dùng số Ả Rập. Có mục lục tự động, danh mục hình/bảng.
- Bìa: logo trích nguyên từ Word; trường/khoa Đại học Đại Nam; FIT4013, đề tài 16;
  tên đề tài đầy đủ; Hà Nội 2026. Không đưa nội dung chuyên môn của Word vào báo cáo.
- Giảng viên: ThS. Lê Thị Thùy Trang, khớp `fit4013_extracted.txt`.
- Sinh viên: Vũ Quốc Đoàn — 1871020143; Trần Đại Hiệp — 1871020223. Khớp
  yêu cầu người dùng và bìa Word. Lớp CNTT18-10, khóa K18, năm học 2026–2027.
- Sáu phần: hoàn thiện nội dung học thuật, công thức, phân tích mã và thực nghiệm;
  dựa trên artifact đã lưu, không tạo số liệu hoặc huấn luyện lại.
- Hình: toàn bộ 15 ảnh kết quả cũ (8 EDA train, 6 confusion matrices, 1 comparison),
  cộng sơ đồ pipeline LaTeX, trong 14 mục hình. Có phân tích văn bản đi kèm.
- Bảng: 13 bảng, gồm phân công, dữ liệu, leakage, repository, kiểm thử, split,
  metric, gap CV, cấp đơn, ablation, lỗi nhóm và importance. Năm bảng số liệu
  được sinh từ CSV/JSON bằng `scripts/report_tables.py`, không nhập metric bằng tay.
- Phân công: **đề xuất, chưa xác nhận** cả ở PDF lẫn `TEAM_ASSIGNMENT_PROPOSED.md`.
- Trình bày: A4, Times New Roman; thân bài, bảng và chú thích 13 pt; H1 14 pt đậm,
  H2 13 pt đậm, H3 13 pt đậm nghiêng. Bìa dùng riêng tiêu đề 15 pt đậm,
  chữ khác 14 pt, bảng nhóm 14 pt.
  PDF có font nhúng, tiếng Việt hiển thị; các trang đã được render để kiểm tra.
- Build: XeLaTeX ba lượt; không còn lỗi LaTeX, overfull/underfull box hoặc
  citation/reference chưa giải quyết. Còn cảnh báo Babel chưa nạp mẫu ngắt từ
  tiếng Việt và nhắc MiKTeX chưa kiểm tra cập nhật; không cản trở tạo PDF.
- Template: yêu cầu mục 2.3 nói nộp theo template học phần nhưng workspace chỉ có
  hướng dẫn trích xuất, không có template LaTeX chính thức. Bìa được dựng theo
  thông tin người dùng, chưa tự nhận đạt template chưa được cung cấp.

## Bằng chứng thực nghiệm được giữ nguyên

Mẫu 5.999/180.519 dòng, 2.113/65.752 đơn; train 4.823 dòng/1.690 đơn,
 test 1.176 dòng/423 đơn. Tree B được chọn bằng CV F1 0,7058; test F1 dòng
0,7098, F1 đơn 0,7100. Dummy F1 đơn 0,7123 do luôn dự đoán dương. Standard
Class có 248 FN/254 dòng dương. Đây là holdout lịch sử đã biết, không phải
validation độc lập mới. Không thay code mô hình, không chạy lại notebook/ML tests.
Các kết quả kiểm thử lịch sử được ghi riêng trong `REPAIR_VERIFICATION.md`.

## Cần xác nhận trước nộp

1. Template chính thức hoặc chấp thuận định dạng hiện tại từ giảng viên.
2. Phân công và đóng góp thực tế của hai thành viên; hiểu và giải thích sản phẩm.
3. Repository đã được giảng viên chấp thuận, rà soát cuối của nhóm và khai báo AI.
4. Nếu cần nộp slide: cập nhật deck cũ và kiểm tra toàn bộ deck riêng.

Commit/push cuối và SHA origin/main được xác minh sau khi hoàn tất kiểm tra;
SHA được báo ở phản hồi bàn giao, không tự ghi SHA của một commit vào chính nó.

## Cập nhật quy chuẩn hai bìa theo Word

Đã dùng Microsoft Word xuất đúng trang 1–2 của mẫu để đối chiếu trực quan,
đặt riêng tọa độ khung/logo/khối thông tin cho mỗi bìa. Kiểm tra font trực tiếp
trong PDF thành công: bìa chỉ có 14,0 và 15,0 pt; tiêu đề 15 pt đậm, bảng bìa hai
14 pt, không đánh số hoặc tràn sang trang ba. Xem `COVER_UPDATE_VERIFICATION.md`
và `COVER_TYPOGRAPHY_AUDIT.json`. Word mẫu bìa đã được đối chiếu; điều này không
thay thế template LaTeX chính thức của học phần vẫn chưa được cung cấp.

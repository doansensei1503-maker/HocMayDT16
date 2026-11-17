# Trạng thái báo cáo FIT4013 — 17/11/2026

**PDF: 40 trang A4, đã biên dịch và kiểm tra trực quan.**
**Template chính thức: chưa có để xác minh. Đóng góp thực tế: cần nhóm xác nhận.**

- Đầu ra: `report/final_report.pdf`; nguồn chính `report/main.tex` và sáu tệp
  `report/sections/`. Hai trang bìa không đánh số; bốn trang đầu dùng số La Mã,
  nội dung và tài liệu tham khảo dùng số Ả Rập. Có mục lục tự động, danh mục hình/bảng.
- Bìa: logo trích nguyên từ Word; trường/khoa Đại học Đại Nam; FIT4013, đề tài 16;
  tên đề tài đầy đủ; Hà Nội 2026. Không đưa nội dung chuyên môn của Word vào báo cáo.
- Giảng viên: ThS. Lê Thị Thùy Trang, khớp `fit4013_extracted.txt`.
- Sinh viên: Vũ Quốc Đoàn — 1871020143; Trần Đại Hiệp — 1871020223. Khớp
  yêu cầu người dùng và bìa Word. Lớp CNTT18-10, khóa K18, năm học 2026–2027.
- Sáu chương: hoàn thiện nội dung học thuật, công thức, phân tích mã và thực nghiệm;
  dựa trên artifact đã lưu, không tạo số liệu hoặc huấn luyện lại.
- Hình: toàn bộ 15 ảnh kết quả cũ (8 EDA train, 6 confusion matrices, 1 comparison),
  cộng sơ đồ pipeline LaTeX, trong 14 mục hình. Có phân tích văn bản đi kèm.
- Bảng: 13 bảng, gồm phân công, dữ liệu, leakage, repository, kiểm thử, split,
  metric, gap CV, cấp đơn, ablation, lỗi nhóm và importance. Năm bảng số liệu
  được sinh từ CSV/JSON bằng `scripts/report_tables.py`, không nhập metric bằng tay.
- Phân công: **đề xuất, chưa xác nhận** cả ở PDF lẫn `TEAM_ASSIGNMENT_PROPOSED.md`.
- Trình bày: A4, Times New Roman; thân bài, bảng và chú thích 13 pt; H1 14 pt đậm, căn giữa, viết hoa,
  H2 13 pt đậm, H3 13 pt đậm nghiêng. Bìa dùng riêng tiêu đề 15 pt đậm,
  chữ khác 14 pt, bảng nhóm 14 pt.
  PDF có font nhúng, tiếng Việt hiển thị; các trang đã được render để kiểm tra.
- Build: XeLaTeX ba lượt; không còn lỗi LaTeX, overfull/underfull box hoặc
  citation/reference chưa giải quyết. Còn cảnh báo Babel chưa nạp mẫu ngắt từ
  tiếng Việt và nhắc MiKTeX chưa kiểm tra cập nhật; không cản trở tạo PDF.
- Template: yêu cầu mục 2.3 nói nộp theo template học phần nhưng workspace chỉ có
  hướng dẫn trích xuất, không có template LaTeX chính thức. Bìa được dựng theo
  thông tin người dùng, chưa tự nhận đạt template chưa được cung cấp.

## Cập nhật heading và nguồn tham khảo

- Sáu chương đánh số tự động CHƯƠNG 1–6; mục lục và tham chiếu chéo đồng bộ.
- LỜI MỞ ĐẦU thay Tóm tắt; bảng phân công hai cột, hai thành viên, vẫn chờ xác nhận.
- Chương 3 có URL GitHub đầy đủ, nhấp được, không tràn lề.
- Đúng năm nguồn tham khảo; bỏ ba nguồn ngoài danh sách yêu cầu, thay dẫn chứng
  tương ứng bằng vị trí mã nguồn, không gán sang nguồn khác.
- Đã kiểm tra 12 H1, 49 H2, 27 chú thích; H3 được cấu hình nhưng chưa có trong nội dung.
- Bản hiện hành: xem `HEADING_VERIFICATION.md` và các JSON audit gắn SHA-256 PDF.

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

## Đối chiếu video — bản 40 trang hiện hành

Đã đọc trực tiếp trang quy định trong video tại các mốc khoảng 23:15 và
24:13–24:43, cùng ví dụ bìa và tài liệu tham khảo. Bản đầy đủ các điểm đạt,
chưa xác minh và khác biệt được chủ động giữ theo người dùng ở `VIDEO_REVIEW.md`.
Không có transcript đầy đủ; không khẳng định đã nghe trọn mọi lời hướng dẫn.

Đã áp dụng lề trái 2,5 cm, các lề còn lại 2 cm; văn bản 13 pt có baseline thực
19,5 pt (giãn dòng 1,5), bảng/mã giữ dòng gọn với cùng cỡ 13 pt. Tên bảng trên,
tên hình dưới; chú thích giữa/nghiêng 13 pt. Trích dẫn và danh mục theo tác giả–năm
APA-style, năm chưa rõ ghi n.d. Hai bìa và H1/H2/H3 giữ quy chuẩn đã chốt.
Mục lục/danh mục có bookmark; link tài liệu tham khảo đã sửa tới đúng PDF trang 40.

Cả 40 trang đã được render/kiểm tra; xem `PDF_REVIEW_AUDIT.json`,
`REPORT_NAVIGATION_AUDIT.json`, `VIDEO_LAYOUT_AUDIT.json` và
`COVER_TYPOGRAPHY_AUDIT.json`. VS Code đã mở trực tiếp bản PDF mới nhất bằng
PDF Preview. Không sửa code ML, dataset, notebook hoặc artifact thực nghiệm.

> Hồ sơ lịch sử cho lần chuẩn hóa bìa ở bản 37 trang. Bìa/font đã chốt vẫn được
> giữ trong bản 40 trang hiện hành; phần trình bày theo video và kiểm chứng mới
> nằm tại `VIDEO_REVIEW.md` cùng các JSON audit liên kết trong đó.

# Kiểm chứng cập nhật hai bìa và quy chuẩn font FIT4013

Ngày: 17/11/2026. PDF hiện hành: `report/final_report.pdf`, **37 trang A4**.
Thay thế trạng thái font/bố cục của bản 36 trang trước; giữ nguyên kết quả nghiên cứu.

## Đối chiếu trực tiếp Word

Mở `D:\FIT4006_DeTai38_BaoCao_Final.docx` bằng Microsoft Word ở chế độ chỉ đọc,
tắt macro và xuất riêng trang 1–2 thành `report/build/word_covers.pdf` để xem.
Đã kiểm tra trực quan cả hai trang mẫu và hai trang PDF LaTeX sau chỉnh sửa.
Không đưa tệp Word, PDF tham chiếu hoặc ảnh render vào Git.

- Bìa 1: khung kép đen khoảng 159 × 260,1 mm, bắt đầu tại x=22,5 mm, y=18 mm;
  trường/khoa phía trên, đường kẻ ngắn, logo phía dưới, tiêu đề giữa trang,
  thông tin giảng viên/sinh viên phía dưới và Hà Nội 2026 cuối trang.
- Bìa 2: khung theo vị trí riêng của mẫu, x=28,55 mm, y=18,1 mm, khoảng
  159 × 257,4 mm; vị trí/tỷ lệ logo theo trang Word thứ hai; bảng hai cột
  “Hạng mục / Thông tin”, giảng viên/nhóm/lớp/khóa/năm học, địa điểm/năm phía dưới.
- Logo PNG giữ nguyên byte; chỉ đổi kích thước hiển thị theo từng trang mẫu.
- Tiêu đề được đổi về 15 pt theo yêu cầu mới, không giữ 25/20/18 pt của Word.
  Tên đề tài dài được chia hai dòng, không ép nhỏ chữ.
- Các thông tin môn cũ bị thay bằng FIT4013, đề tài 16, tên đề tài đầy đủ,
  ThS. Lê Thị Thùy Trang; Vũ Quốc Đoàn 1871020143 và Trần Đại Hiệp 1871020223;
  lớp CNTT18-10, khóa K18, năm học 2026–2027, Hà Nội.

## Kiểm tra font thực từ PDF

Lệnh `py scripts/verify_report_typography.py` thành công, lưu bằng chứng ở
`docs/COVER_TYPOGRAPHY_AUDIT.json`.

| Thành phần | Kết quả thực trong PDF |
|---|---|
| Toàn bộ chữ dàn trên bìa 1 và bìa 2 | Chỉ 14,000 hoặc 15,000 pt; Times New Roman |
| Trường/khoa, tiêu đề báo cáo, học phần, đề tài và tên đề tài | 15 pt, đậm |
| Các thông tin khác trên hai bìa | 14 pt; không có span chữ nào nhỏ hơn 14 pt |
| Bảng nhóm trang 2, cả tiêu đề và nội dung | 14 pt |
| Vị trí chữ | Nằm trong khung tham chiếu của từng bìa |
| Số trang bìa | Không có |
| Trang PDF thứ 3 | Bắt đầu Tóm tắt; không có phần bìa bị tràn |
| Sáu H1 nội dung | 14 pt, đậm |
| 48 H2 | 13 pt, đậm |
| H3 | Định nghĩa 13 pt đậm nghiêng; nội dung hiện tại không có H3 |
| Văn bản thường, bảng, 27 chú thích hình/bảng | 13 pt, Times New Roman |

Cỡ dùng `bp` trong LaTeX, tương đương điểm Word/PDF (72/inch), để kết quả
kiểm tra trực tiếp không thấp hơn 14 pt vì khác biệt đơn vị TeX pt và PDF pt.
Audit font áp dụng mọi chữ dàn trong PDF. Logo và các biểu đồ raster giữ nguyên
hình nguồn; công thức toán giữ cỡ chỉ số trên/dưới tự nhiên, không coi chỉ số
toán là văn bản thân bài hoặc chữ trên bìa. `fix-cm` loại cảnh báo thay thế cỡ font toán.

## Build và kiểm tra bố cục

- XeLaTeX ba lượt qua `scripts/build_report.ps1`, `--disable-installer`,
  `-halt-on-error`, `-file-line-error`; helper kết thúc thành công.
- Log cuối không có lỗi LaTeX, overfull/underfull box, font size substitution
  hoặc citation/reference chưa giải quyết. Còn cảnh báo Babel chưa nạp mẫu
  ngắt từ tiếng Việt và thông báo MiKTeX chưa kiểm tra cập nhật, không chặn build.
- Đã render toàn bộ 37 trang và kiểm tra lại hai bìa ở kích thước đầy đủ,
  sau đó rà soát toàn bộ các trang còn lại vì thay đổi cỡ thân bài gây dàn lại trang.
  Không có chữ/bảng/hình bị cắt hay tràn lề; khung và logo không che nội dung.
- Định dạng bìa tách riêng ở `cover.tex`, phần thân ở `typography.tex`;
  bìa không kế thừa `small`/cỡ tiêu đề từ phần thân. Căn trái các ô p của bảng
  tránh giãn từ quá rộng khi dùng cỡ 13 pt.

## Kiểm tra giữ nguyên nội dung

Đối chiếu từng tệp của cả sáu phần với HEAD trước chỉnh sửa: giống hệt nội dung.
Phần 3 chỉ thêm cặp lệnh căn trái cho đoạn liệt kê notebook, không đổi một chữ.
Không có thay đổi ở `src`, `results`, `configs`, `notebooks`, `tests` hoặc
`report/tables`; không huấn luyện lại hay chạy thêm thực nghiệm. Mã nguồn, thuật
toán, các thước đo và số liệu giữ nguyên.

Bản Word đã được xác minh làm mẫu bìa; template LaTeX chính thức của FIT4013
vẫn chưa được cung cấp. Phân công vẫn là đề xuất cần thành viên xác nhận.
Các điều kiện nộp học phần còn lại nằm trong `FINAL_SUBMISSION_CHECKLIST.md`.
Commit SHA và đối chiếu origin/main được báo trong phản hồi bàn giao sau push.

# Biên dịch báo cáo FIT4013

Nguồn chính: `main.tex`, `cover.tex`, `frontmatter.tex`, `sections/01_...06_...`,
`references.tex` và `typography.tex`. Sáu phần nội dung dùng kết quả lịch sử đã lưu, không cần
huấn luyện lại mô hình để build PDF.

Từ gốc repository, với XeLaTeX/MiKTeX và Times New Roman:

```powershell
py scripts/report_tables.py
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build_report.ps1
```

Lệnh Python chỉ kiểm tra metric từ ma trận nhầm lẫn và sinh năm bảng LaTeX
từ CSV/JSON tổng hợp có sẵn. Nó không đọc dữ liệu thô và không huấn luyện.
Lệnh PowerShell chạy XeLaTeX ba lượt để ổn định mục lục, danh mục và tham chiếu,
tạo `report/final_report.pdf`. Tham số ExecutionPolicy chỉ áp dụng tiến trình
đang chạy, không đổi cấu hình PowerShell của máy. Nếu môi trường đã cho phép
chạy script, có thể dùng trực tiếp `.\scripts\build_report.ps1`.

Helper tìm XeLaTeX trên PATH hoặc MiKTeX trong LocalAppData, tắt installer tự
động và lưu log/auxiliary vào `report/build/` (gitignored). Không gọi Console
hay `kpsewhich`. Thiếu package thì dừng và báo tên; không tự cài phần mềm.

`generated.tex`, `analysis.tex`, `repair_analysis.tex` là nguồn tổng hợp/biên tập
cũ được giữ để truy vết; `main.tex` hiện không input ba tệp đó. Không chạy
`src.run` hoặc `src.reporting.render` chỉ để build báo cáo. Nếu đổi artifact
thực nghiệm, phải rà cả nội dung diễn giải ở `sections/`.

Logo trong `assets/dainam_logo.png` được trích nguyên trạng từ `word/media/image1.png`
của tệp Word người dùng cung cấp. Chỉ thiết kế bìa, logo và thông tin nhận diện
được tham khảo; không dùng nội dung chuyên môn của báo cáo Word. Xem
`assets/SOURCE.md` để biết phạm vi và nguồn.

Hiện chưa có template LaTeX chính thức FIT4013 trong workspace. Hai bìa theo
thông tin người dùng, cấu trúc sáu phần theo `docs/fit4013_extracted.txt`;
không tự nhận đã tuân thủ template chưa được cung cấp. Sau khi có template,
cần đối chiếu, build và kiểm tra từng trang lại.

## Quy chuẩn font hiện hành

- Bìa: Times New Roman; mọi tiêu đề và tên đề tài 15 pt đậm; chữ khác 14 pt;
  cả tiêu đề cột và nội dung bảng nhóm 14 pt. Không dùng lệnh giảm font trên bìa.
- Thân: Times New Roman 13 pt; H1 14 pt đậm, H2 13 pt đậm, H3 13 pt đậm nghiêng;
  bảng và chú thích 13 pt. Cỡ chỉ số toán theo quy tắc toán học thông thường.
- Cỡ được định nghĩa bằng `bp` (72 điểm/inch, tương ứng điểm Word/PDF), để kết
  quả trích trực tiếp trong PDF là 14,0/15,0 pt trên bìa và 13,0 pt trong thân.
- `cover.tex` đặt các thành phần theo tọa độ tham chiếu riêng của trang Word 1/2.
  `typography.tex` áp dụng sau hai bìa, giữ độc lập quy chuẩn bìa với phần thân.

Kiểm tra font thực trong PDF, nếu có PyMuPDF (hoặc bản cục bộ trong
`report/build/tools`, không commit):

```powershell
py scripts/verify_report_typography.py
```

Lệnh tạo `docs/COVER_TYPOGRAPHY_AUDIT.json`. Nó không thay PDF, dữ liệu hoặc mô hình.
Cần biên dịch xong rồi mới chạy kiểm tra; không đọc PDF khi compiler đang ghi tệp.

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
- Thân: Times New Roman 13 pt; H1 14 pt đậm, căn giữa, viết hoa, H2 13 pt đậm, H3 13 pt đậm nghiêng;
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

## Trình bày sau đối chiếu video

Thân A4 có lề trái 2,5 cm, phải/trên/dưới 2 cm; văn bản 13 pt trên baseline
19,5 pt. Bảng và mã dùng hàng gọn; cỡ chữ vẫn 13 pt. Chú thích bảng ở trên,
hình ở dưới, giữa và nghiêng 13 pt. Bìa không chịu thay đổi lề/thân vì tọa độ
riêng theo Word. APA-style dùng natbib với tác giả–năm, năm chưa rõ ghi n.d.;
không cần BibTeX/Biber vì các mục nguồn được quản lý trong `references.tex`.

Build cần thêm gói natbib, fix-cm và titlesec. Helper tắt cài tự động; nếu thiếu gói thì
cài bằng CLI MiKTeX được phép rồi chạy lại. Không huấn luyện lại để build.
Sau khi build xong, chạy:

```powershell
py scripts/verify_report_typography.py
py scripts/verify_report_navigation.py
py scripts/verify_video_layout.py
```

Các lệnh chỉ đọc PDF và sinh JSON audit trong docs. Xem `docs/VIDEO_REVIEW.md`
cho mốc video đã đọc và phân biệt quy định với minh họa. Video môn khác không
thay thế cấu trúc sáu phần, quy chuẩn font người dùng hoặc template FIT4013.

Có thể mở trực tiếp PDF trong VS Code bằng `code --reuse-window report/final_report.pdf`
với tiện ích `tomoki1207.pdf` (PDF Preview). Tệp được mở là PDF thật, không phải ảnh preview.

Heading được quản lý tập trung trong `typography.tex`; `partstart` tạo số chương
và nhãn tham chiếu tự động. Sáu chương giữ nguyên nội dung; có 5 nguồn tham khảo.
Xem [kiểm chứng heading](../docs/HEADING_VERIFICATION.md) cho bản hiện hành.

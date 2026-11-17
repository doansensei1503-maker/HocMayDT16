# Biên dịch báo cáo FIT4013

Nguồn chính: `main.tex`, `cover.tex`, `frontmatter.tex`, `sections/01_...06_...`
và `references.tex`. Sáu phần nội dung dùng kết quả lịch sử đã lưu, không cần
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

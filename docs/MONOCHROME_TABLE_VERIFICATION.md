# Kiểm chứng bảng trắng–đen — 17/11/2026

PDF: `report/final_report.pdf`, 40 trang.
SHA-256: `8416805cb04842bac17b78ca0f1d8d4dae948a83c7c276c7a498780c20ec24dd`.

- Bỏ toàn bộ `rowcolor` khỏi 13 bảng active và `scripts/report_tables.py`;
  không có cellcolor, columncolor, rowcolors hoặc macro tô nền còn lại trong report/scripts.
- Xóa hai định nghĩa màu bảng không dùng; giữ package xcolor/colortbl vì lệnh
  arrayrulecolor còn dùng hợp lệ để đặt đường kẻ đen. Giữ booktabs, độ dày nét,
  cột, padding, arraystretch 1,22, header đậm và các cực đại in đậm như trước.
- Kiểm tra trực tiếp drawing/text trong PDF: 13/13 bảng không có fill, chữ đen,
  nét kẻ đen, font Times New Roman 13 pt, nằm trong lề. Caption giữ 13 pt.
- So sánh nội dung ô của đủ 13 bảng với commit da3ce9f: giống hoàn toàn;
  giữ tên/caption, label, số liệu và tham chiếu. Script sinh bảng được chạy lại,
  kiểm tra sáu ma trận nhầm lẫn và metric đạt, không thực hiện training.
- XeLaTeX qua helper ba lượt thành công; không overfull/underfull hoặc cite/ref
  chưa giải quyết. Các audit typography, navigation, video layout và table đều đạt.
- Xem riêng 13 ảnh bảng ở mức 1,8x. Đối chiếu raster 38 trang ngoài vùng bảng
  với PDF đã duyệt trước: giống pixel. Hai trang PDF 20/21 được xem lại sau khi
  giữ mục kiểm thử với nội dung ở trang mới, tránh heading lẻ cuối trang.
- Hai bìa giống pixel bản trước; H1/H2/H3, sáu chương, hình ảnh và thực nghiệm
  không thay đổi. Bảng bìa giữ ngoại lệ 14 pt đã chốt.
- PDF mới đã được mở trực tiếp trong VS Code. AI_USAGE.md có phần khai báo
  người dùng cung cấp và giữ nhật ký hỗ trợ; không đưa khai báo vào thân báo cáo.

Bằng chứng: TABLE_LAYOUT_AUDIT.json, COVER_TYPOGRAPHY_AUDIT.json,
REPORT_NAVIGATION_AUDIT.json, VIDEO_LAYOUT_AUDIT.json, PDF_REVIEW_AUDIT.json.
Còn cảnh báo Babel thiếu mẫu ngắt từ tiếng Việt và nhắc cập nhật MiKTeX như trước;
không ngăn tạo PDF. Không thay dữ liệu, src, configs, notebooks hoặc tests.

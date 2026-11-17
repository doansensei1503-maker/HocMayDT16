# Đối chiếu video hướng dẫn và báo cáo FIT4013

Ngày kiểm tra: 17/11/2026. Video người dùng cung cấp:
[Hướng dẫn làm Báo cáo học phần mạng máy tính K18 – FITDNU](https://youtu.be/nF6O191S4XU),
tác giả Lê Văn Phong, thời lượng 25:18. Metadata công khai ghi ngày 08/10/2026.
Đây là tài liệu cho môn khác; yêu cầu người dùng và hướng dẫn FIT4013 được ưu tiên.

## Phạm vi thực sự đã xác minh

Ban đầu công cụ web không tải được trang, bộ trích video/phụ đề báo lỗi.
Sau đó đã đọc metadata qua oEmbed, xem 153 ảnh storyboard, và mở trình phát
Chrome thông thường tại các mốc cụ thể. Các khung đủ nét đã đọc được:

| Mốc quan sát thực tế | Nội dung được xác minh |
|---|---|
| Khoảng 08:43 | Minh họa bìa có khung, logo, tên học phần/đề tài. |
| Khoảng 20:53 | Trang tài liệu tham khảo nêu APA và ví dụ nguồn môn Mạng máy tính. |
| Khoảng 23:15 | Phần đầu trang quy định: quy mô, lề, font, giãn dòng, số trang, chú thích. |
| Khoảng 24:13 và 24:43 | Các quy định còn lại: hình rõ, mã chọn lọc, nguồn dẫn, khai báo AI. |

Các mốc là thời gian đọc từ trình phát, không suy từ vị trí ảnh thu nhỏ.
Đã đối chiếu hình ảnh trong `report/build/video-reference/`; ảnh/video tham chiếu
chỉ lưu cục bộ, không commit. **Không có transcript sử dụng được và chưa xác minh
trọn vẹn lời nói của giảng viên.** Không gọi việc xem các mốc này là đã nghe toàn bộ
video; không suy diễn yêu cầu bằng lời ngoài nội dung đọc rõ trên trang quy định.

## Quy định viết rõ, thao tác minh họa và quyết định áp dụng

Bảng dưới tóm lược các quy tắc nhìn thấy. Chúng là quy định cho FIT4006 trong
video; cột quyết định nêu phần được tiếp nhận cho báo cáo LaTeX FIT4013.

| Nhóm quy tắc quan sát | Tính chất | Áp dụng cho FIT4013 |
|---|---|---|
| Tối thiểu 30 trang, ngoài bìa; nội dung khớp sản phẩm | Quy định ghi rõ | Mục tiêu người dùng 35–40 trang và kiểm chứng CSV/JSON được giữ. Không dùng `.pkt`. |
| A4, lề trái 2,5 cm; ba lề khác 2 cm | Quy định ghi rõ | Áp dụng cho thân; giữ tọa độ bìa Word đã chốt. |
| Times New Roman 13; giãn dòng 1,5; văn bản căn đều | Quy định ghi rõ | Áp dụng văn bản thường; bảng/mã giữ dòng gọn với chữ 13 pt. |
| Số trang dưới, giữa; bìa không có số | Quy định ghi rõ | Giữ bìa trống số, đầu báo cáo La Mã, nội dung Ả Rập. |
| Tên bảng trên; tên hình dưới; chú thích giữa, nghiêng | Quy định ghi rõ | Áp dụng vị trí/căn/kiểu chữ. Giữ cỡ 13 pt theo người dùng, thay cỡ 12 trong video. |
| Nhắc hình/bảng trong bài; ảnh rõ và có chú thích | Quy định ghi rõ | Đối chiếu 14 hình/13 bảng và tham chiếu, gồm bảng phân công. |
| Mã chọn lọc, giải thích vai trò | Quy định ghi rõ | Giữ các đoạn mã ngắn có thật trong repository. Không nhập cấu hình mạng. |
| APA và dẫn nguồn cho nội dung kế thừa | Quy định ghi rõ | Danh mục tác giả–năm, xếp tên tác giả, thụt treo; không bịa năm chưa rõ. |
| Minh bạch AI và thành viên phải giải trình | Quy định ghi rõ | Duy trì `AI_USAGE.md`; phân công vẫn là đề xuất cần xác nhận. |

Các thao tác chọn chữ, bấm Heading, căn chỉnh trong Word là minh họa sử dụng
phần mềm. Trong LaTeX, dùng lệnh section/subsection/subsubsection, caption/label/ref
và danh mục tự động. Không tái hiện thao tác Word bằng các khoảng trắng gõ tay.

Những chi tiết của ví dụ như ba chương, tên học phần/giảng viên cũ, chủ đề mạng,
nguồn Cisco và tệp cấu hình mạng không chuyển vào báo cáo này. H1/H2/H3 vẫn
14/13/13 pt; bìa vẫn 15 pt đậm và chữ khác tối thiểu 14 pt. Không lấy cỡ chữ đang
hiện trên ribbon Word làm quy định mới khi người dùng đã chốt khác.

## Các điểm chưa đáp ứng trước sửa và kết quả sau sửa

| Hạng mục | Trước sửa | Sau sửa / bằng chứng |
|---|---|---|
| Lề thân bài | 3 / 2,3 / 2,5 / 2,5 cm | **ĐẠT:** trái 2,5; phải/trên/dưới 2 cm. |
| Giãn dòng văn bản | Baseline 15,6 pt với chữ 13 pt | **ĐẠT:** đo baseline 19,5 pt, tương đương 1,5 × 13 pt. |
| Tên bảng | Nằm dưới bảng | **ĐẠT:** cả 13 chú thích bảng nằm trên. |
| Chú thích | Chưa nghiêng/căn giữa nhất quán | **ĐẠT THEO QUY CHUẨN ĐÃ CHỐT:** 13 pt, nghiêng, giữa; tên hình ở dưới. |
| Nguồn tham khảo | Danh mục đánh số, không phải tác giả–năm | **ĐẠT:** APA-style tác giả–năm với natbib, 8 nguồn, năm chưa biết ghi n.d. |
| Link tài liệu tham khảo trong mục lục | Dẫn về trang kết luận | **ĐẠT:** trỏ đúng trang PDF 40. |
| Điều hướng danh mục | Thiếu mục/bookmark trong mục lục | **ĐẠT:** hai danh mục và mục lục có bookmark/điểm neo đúng. |
| Nhắc bảng phân công và cặp ma trận cây A/B | Thiếu tham chiếu số tự động | **ĐẠT:** bổ sung label/ref; bảng phân công vẫn ghi đề xuất. |
| Phép tính F1 bị ngắt qua trang | Tách kết quả khỏi phép tính | **ĐẠT:** giữ liền đoạn suy ra Precision/Recall/F1. |
| Số trang tổng | 37 trước thay dàn trang | **ĐẠT:** PDF cuối 40 trang, gồm bìa và các thành phần đầu/cuối. |
| Font và hai bìa | Đã có quy chuẩn riêng | **ĐẠT:** kiểm tra lại PDF; không giảm cỡ chữ để ép trang. |
| Sáu phần / số liệu / thuật toán | Đã đúng phạm vi | **GIỮ NGUYÊN:** không chạy lại mô hình hoặc đổi artifact. |
| Lời nói và transcript toàn video | Không có bản đọc hoàn chỉnh | **CHƯA XÁC MINH:** không khẳng định thêm yêu cầu ngoài trang quy định đã đọc. |
| Template LaTeX chính thức FIT4013 | Chưa được cung cấp | **CHƯA XÁC MINH:** video môn khác không thay thế template chính thức. |
| Đóng góp thực tế của nhóm | Chưa được hai thành viên xác nhận | **CHƯA XÁC NHẬN:** không biến bảng đề xuất thành lịch sử công việc. |

Phần tổng kết được biên tập gọn ba đoạn lặp lại để giữ giới hạn 40 trang sau
khi tăng giãn dòng. Không xóa kết quả, hạn chế Standard Class hay cảnh báo về
holdout lịch sử. Các trang float có hình/bảng giữ theo cơ chế LaTeX, không thêm
trang trắng hoặc phóng ảnh để kéo dài báo cáo.

## Kiểm chứng bản cuối

- XeLaTeX ba lượt thành công, PDF 40 trang A4; không còn overfull/underfull,
  font substitution hoặc tham chiếu/trích dẫn thiếu. Babel/MiKTeX còn các nhắc
  cấu hình ngắt từ/cập nhật không chặn build.
- `verify_report_typography.py`: 14/15 pt trên hai bìa, bảng nhóm 14 pt;
  thân/bảng/chú thích 13 pt; sáu H1 14 pt đậm, 48 H2 13 pt đậm; H3 định nghĩa
  13 pt đậm nghiêng, hiện không có H3 trong nội dung.
- `verify_video_layout.py`: baseline thực 19,5 pt; 13 tên bảng trên; 13 chú thích
  hình raster dưới hình; sơ đồ vector Hình 2 được xem trực quan; chú thích nghiêng.
- `verify_report_navigation.py`: mục lục/danh mục/tài liệu tham khảo có bookmark
  và liên kết đúng; các liên kết nội bộ có trang đích hợp lệ.
- Render và kiểm tra trực quan mọi trang 1–40: bìa, bảng, ảnh, công thức, mã,
  mục lục, danh mục, đánh số và APA. Không có chữ/hình/bảng bị cắt.
- Các JSON audit cùng SHA256 của PDF cuối nằm trong `docs/`.
- Đã cài tiện ích `tomoki1207.pdf` để mở PDF trực tiếp trong VS Code. Bản cuối
  được mở lại sau biên dịch; xác nhận cửa sổ `final_report.pdf - HocMayDT16 - Visual Studio Code`.

Không thay đổi `src`, `results`, `configs`, notebook hoặc tests ML. Chỉ sửa
markup báo cáo, kiểu xuất bảng và các kiểm tra tài liệu. Không công bố screenshot
video, cookie, luồng media, dữ liệu thô, model hoặc build files lên GitHub.

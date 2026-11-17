# FIT4013 — checklist bàn giao và trước nộp

## Đã kiểm tra trong lần hoàn thiện báo cáo

- [x] PDF thật 40 trang A4: `report/final_report.pdf`; XeLaTeX ba lượt.
- [x] Đủ sáu phần bắt buộc theo thứ tự trong hướng dẫn FIT4013.
- [x] Hai bìa đối chiếu trực quan với trang 1–2 Word, logo nguyên bản, không đánh số.
- [x] FIT4013, đề tài 16; tên đề tài đầy đủ; trường/khoa đúng.
- [x] Giảng viên ThS. Lê Thị Thùy Trang khớp tài liệu học phần.
- [x] Vũ Quốc Đoàn / 1871020143; Trần Đại Hiệp / 1871020223 khớp yêu cầu và Word.
- [x] Lớp CNTT18-10, khóa K18, năm học 2026–2027 theo yêu cầu người dùng.
- [x] Phân công ghi rõ đề xuất, chưa phải đóng góp đã xác nhận.
- [x] Số liệu đối chiếu sáu ma trận CSV, comparison, order JSON, ablation và lỗi nhóm.
- [x] 15 ảnh thực nghiệm, sơ đồ pipeline và 13 bảng có diễn giải; không dùng hình
      chuyên môn hoặc nội dung các chương của tài liệu Word.
- [x] Render và kiểm tra trực quan mọi trang; kiểm tra font, hình/bảng, mục lục,
      tham chiếu và trang tài liệu tham khảo. Không còn tràn hộp hoặc tham chiếu thiếu.
- [x] Khai báo AI được giữ và bổ sung trung thực trong `AI_USAGE.md`.
- [x] Không thay thuật toán, không huấn luyện lại, không coi holdout cũ là test mới.
- [x] Không đưa Word, raw CSV, model, split riêng hoặc file build vào commit báo cáo.

- [x] Bìa Times New Roman: tiêu đề/tên đề tài 15 pt đậm; chữ khác tối thiểu 14 pt;
      bảng nhóm cả tiêu đề lẫn nội dung 14 pt. Kiểm tra trực tiếp trên PDF.
- [x] H1 14 pt đậm; H2 13 pt đậm; H3 định nghĩa 13 pt đậm nghiêng;
      thân, bảng và chú thích 13 pt. Bìa không tràn sang trang ba.
- [x] Sáu phần không đổi nội dung; thuật toán, artifact và bảng số liệu không đổi.

- [x] Đối chiếu các quy định viết rõ trong video; các thao tác Word là minh họa,
      nội dung chuyên môn và quy mô nhóm môn khác không áp dụng.
- [x] Lề trái 2,5 cm; trên/dưới/phải 2 cm; baseline văn bản 19,5 pt với chữ 13 pt.
- [x] Tên bảng trên, hình dưới; chú thích giữa/nghiêng 13 pt theo quy chuẩn người dùng.
- [x] Tác giả–năm và danh mục APA-style; n.d. cho năm chưa được xác minh.
- [x] Link mục lục đến tài liệu tham khảo đúng; thêm điều hướng tới hai danh mục.
- [x] PDF 40 trang mới nhất đã mở trong VS Code; mọi trang đã được kiểm tra lại.
- [ ] Xác minh thêm lời nói ngoài trang quy định nếu cần: chưa có transcript đầy đủ.

## Nhóm cần xác nhận trước nộp

- [ ] Cung cấp template LaTeX FIT4013 chính thức hoặc xác nhận giảng viên chấp thuận
      định dạng hiện tại. Chưa có template để kiểm chứng; không đánh dấu đã đạt.
- [ ] Sau đối chiếu template, nếu phải sửa thì build và kiểm tra mọi trang lại.
- [ ] Hai thành viên xác nhận/điều chỉnh nhiệm vụ và ghi đóng góp thực tế có bằng chứng.
- [ ] Xác nhận GitHub `doansensei1503-maker/HocMayDT16` được giảng viên chấp thuận.
- [ ] Cả hai tự đọc và giải thích pipeline, số liệu, Standard Class, Dummy và giới hạn.
- [ ] Rà soát cuối, xác nhận khai báo AI và bản PDF chính thức sẽ nộp.
- [ ] Nếu cần slide: cập nhật nhận diện nhóm trong deck cũ và kiểm tra toàn bộ deck.

Cảnh báo không chặn build: Babel chưa nạp mẫu ngắt từ tiếng Việt; MiKTeX nhắc
kiểm tra cập nhật. Không có lỗi LaTeX làm dừng biên dịch trong bản cuối.
Commit SHA và đối chiếu origin/main ghi trong phản hồi bàn giao sau push.

## Cập nhật heading — 17/11/2026

- [x] H1 14 pt, đậm, giữa, viết hoa; sáu chương đánh số tự động, mục lục đúng.
- [x] Lời mở đầu và bảng phân công hai cột; không xác nhận thay nhóm.
- [x] GitHub đầy đủ, nhấp được trong Chương 3; đúng năm nguồn, không cite hỏng.
- [x] PDF 40 trang được rà trực quan; hai bìa giữ nguyên, font đạt 14/15 pt.
- [x] Thuật toán, dữ liệu và kết quả giữ nguyên; khai báo AI_USAGE được cập nhật.

## Kiểm tra bảng biểu — 17/11/2026

- [x] Đủ 13 bảng phần thân; header đậm nền nhẹ, hàng thoáng, số căn phải.
- [x] Toàn bộ chữ ô bảng TNR 13 pt; caption 13 pt; không tràn lề.
- [x] Giữ nguyên các số metric, thiếu dữ liệu, quy mô mẫu và phân tích lỗi.
- [x] Đã sửa script sinh bảng, kiểm tra tính lặp ổn định, không chạy ML.
- [x] Đã xem 40 trang và 13 ảnh bảng; PDF mới mở trong VS Code.

> Hồ sơ lịch sử cho bản 36 trang trước khi cập nhật font. Bản hiện tại có 37
> trang, bìa 14/15 pt và thân bài 13 pt. Kiểm chứng hiện hành nằm tại
> `COVER_UPDATE_VERIFICATION.md` và `COVER_TYPOGRAPHY_AUDIT.json`.

# Kiểm chứng báo cáo hoàn thiện — 17/11/2026

## Phạm vi

Hoàn thiện trực tiếp repository hiện tại theo yêu cầu trong tệp văn bản người dùng.
Tài liệu Word chỉ dùng thiết kế bìa, logo và nhận diện; không dùng nội dung chuyên môn.
Đọc bản trích FIT4013 trong `docs/fit4013_extracted.txt`, các module `src`, cấu hình,
bảng CSV/JSON, nguồn báo cáo cũ và hồ sơ kiểm thử trước khi biên tập.
Không thay đổi thuật toán, dữ liệu, artifact thực nghiệm hoặc chạy lại training/notebook.

## Kiểm tra nội dung và số liệu

- Sáu phần theo đúng thứ tự mục 2.2 hướng dẫn FIT4013; không dùng bố cục môn khác.
- Trường/khoa, tên đề tài, lớp/khóa/năm học theo yêu cầu người dùng.
  Giảng viên khớp dòng đầu bản trích hướng dẫn; tên và MSSV khớp bìa Word.
- Logo `word/media/image1.png` trích nguyên byte, kiểm tra trực quan, không vẽ lại.
- `py scripts/report_tables.py` thành công: đối chiếu sáu confusion CSV với
  Accuracy/Precision/Recall/F1 trong comparison, sai số < 1e-12; mỗi ma trận có
  1.176 dòng. Winner CV đúng manifest, order F1 đúng hai JSON (423 đơn), tổng
  lỗi nhóm đúng FN=248, FP=66. Năm bảng LaTeX được sinh từ artifact có sẵn.
- Kiểm tra tĩnh thành công: sáu phần; 15 ảnh kết quả tồn tại và được dùng;
  nhãn duy nhất, tham chiếu được giải quyết; cả tám mục tài liệu tham khảo có
  trích dẫn; không có FIT4006, tên giảng viên cũ hay nội dung mạng trong nguồn active.
- Chỉ số chính: tree B CV F1=0,7058; row F1=0,7098; order F1=0,7100;
  Dummy order F1=0,7123. Standard Class 248 FN/254 dòng dương. Tập test là
  lịch sử đã quan sát, không phải đánh giá mới hoặc bằng chứng nhân quả.
- Các bài kiểm thử ML trong báo cáo được ghi rõ là lịch sử; không chạy lại chúng
  để viết báo cáo. Fixture tổng hợp không được coi là dữ liệu thực nghiệm.

## PDF và kiểm tra trực quan

- XeLaTeX/MiKTeX, ba lượt, `--disable-installer`, `-halt-on-error`,
  `-file-line-error`; tạo `report/final_report.pdf`, 36 trang A4.
- Font Times New Roman thường/đậm/nghiêng, Consolas và font toán được nhúng.
  Kiểm tra programmatic bằng MuPDF: đủ 36 trang A4, mọi font có dữ liệu nhúng,
  không xuất hiện ký tự thay thế U+FFFD trong văn bản trích.
- Render toàn bộ PDF; rà soát tất cả trang: hai bìa, thông tin nhóm, mục lục,
  danh mục, công thức, mã ngắn, các bảng, sáu confusion matrices, tám EDA,
  comparison, phần thảo luận/kết luận và tài liệu tham khảo.
- Sau sửa một đoạn cuối để loại trang gần trống, so sánh raster xác nhận 26 trang
  không đổi so với bản đã xem. Kiểm tra lại trực quan 10 trang đổi vị trí/nội dung:
  trang 5, 6 và 29–36. Tổng phạm vi kiểm tra cuối: mọi trang 1–36.
- Có 14 mục hình chứa 15 ảnh kết quả và một sơ đồ pipeline; 13 bảng. Hình không
  bị cắt, bảng và đoạn mã không tràn lề; chú thích và diễn giải đầy đủ.
- Log cuối không có lỗi LaTeX, overfull/underfull box, undefined reference/citation.
  Còn Babel warning chưa nạp hyphenation tiếng Việt và nhắc MiKTeX chưa kiểm tra
  cập nhật. Không tuyên bố đã cấu hình hyphenation. Một số lần build sandbox báo
  không ghi được log MiKTeX trong profile; build cuối chạy với quyền phù hợp để
  compiler ghi log, không cài package hoặc mở MiKTeX Console.
- Thư viện render được tải vào `report/build/tools`, chỉ phục vụ kiểm tra,
  không đổi môi trường ML và không commit thư viện hay ảnh render.

## Nguồn tham khảo và giới hạn bàn giao

Mendeley DOI/version và nội dung tài liệu scikit-learn được mở trực tiếp ngày
17/11/2026. Liên kết Kaggle được mở nhưng không trả nội dung văn bản đọc được;
metadata uploader dùng hồ sơ xác minh trước, không tự nhận xác minh mới.
Hướng dẫn FIT4013 dùng bản trích người dùng chỉ định, không cần lấy nội dung
chuyên môn hoặc hướng dẫn từ Word. Chưa có template LaTeX chính thức trong workspace.

Bảng phân công là đề xuất; chưa có xác nhận đóng góp thực tế của hai sinh viên.
Không tạo tác giả hay lịch sử commit giả. `AI_USAGE.md` được giữ và bổ sung.
Slide là bản cũ, không thuộc phạm vi chứng nhận trực quan toàn bộ trong lần này.

## Git

Kiểm tra diff, cú pháp PowerShell, whitespace và danh sách tệp trước commit.
Chỉ đưa nguồn báo cáo, PDF, logo cho phép và tài liệu liên quan; không thêm raw
CSV, model, Word, split riêng, khóa bí mật hoặc build files. Giữ các thay đổi
đã stage từ đầu phiên và rà soát/cập nhật chúng cho phù hợp báo cáo cuối.
Remote `origin/main` trước thay đổi: `86c4742e1274d738f5fa08d4e577eefb570a551e`.
Commit cuối và đối chiếu remote được báo trong phản hồi bàn giao sau push.

Final helper execution through `cmd.exe` completed with exit code 0. The outer
PowerShell stderr redirection had previously reported exit code 1 despite all
three compiler passes completing; the cmd invocation avoids that wrapper issue.
The final PDF was again compared by raster: every page matches the reviewed layout.

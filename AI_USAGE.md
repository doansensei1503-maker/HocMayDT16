# KHAI BÁO SỬ DỤNG CÔNG CỤ AI

**Học phần:** Nhập môn Học máy – FIT4013
**Đề tài 16:** Dự đoán đơn hàng có nguy cơ giao trễ trong chuỗi cung ứng

Trong quá trình thực hiện bài tập lớn, nhóm có sử dụng OpenAI Codex để hỗ trợ một số công việc kỹ thuật, bao gồm gợi ý và hiệu chỉnh mã nguồn, kiểm tra lỗi chương trình, hỗ trợ hoàn thiện quy trình thực nghiệm và xử lý các vấn đề về định dạng, biên dịch báo cáo LaTeX.

Nhóm chịu trách nhiệm xem xét các phương án được đề xuất, kiểm tra tính chính xác của chương trình và kết quả thực nghiệm, đồng thời rà soát nội dung báo cáo trước khi nộp.

Việc sử dụng công cụ hỗ trợ không thay thế trách nhiệm học tập của các thành viên. Nhóm chịu trách nhiệm về sản phẩm cuối cùng và có khả năng trình bày, giải thích phương pháp, thuật toán và kết quả thực hiện đề tài.

## Nhật ký sử dụng và bằng chứng

AI (OpenAI Codex) hỗ trợ đọc tài liệu PDF, thiết kế phương pháp chống leakage, tạo mã nguồn, kiểm thử, notebook và bản thảo báo cáo trong phiên làm việc này theo yêu cầu người dùng. Các lệnh chạy và kết quả thực được lưu/ghi nhận trong docs/STATUS.md và results; không coi code được tạo là bằng chứng đã chạy dữ liệu thật. Không tạo tên thành viên, đóng góp hay lịch sử commit. Nhóm phải tự đọc, kiểm chứng và giải thích toàn bộ sản phẩm; bổ sung tên công cụ/phiên bản sử dụng thực tế và sửa đổi do người học thực hiện khi nộp bài. Không dùng AI để sinh nhãn, dữ liệu hay metric giả.

2026-11-16: Codex repaired Git remote synchronization, unified the split protocol, added aggregate sampling/order evaluation and a fixed-parameter training-CV ablation, preserved historical evidence, and ran verification. No team contributions or empirical scores were invented. See docs/REPAIR_VERIFICATION.md for actual execution results and limitations.

2026-11-17: AI-assisted review refined the provisional Vietnamese report using
existing experiment artifacts, translated the repair diagnostics, added a
reproducible XeLaTeX build script and updated submission documentation/slides.
No training, holdout tuning, notebook execution or new empirical metric was
performed for these edits. The team must verify the final wording and disclose
any additional AI use or human revisions before submission.

2026-11-17 — Hoàn thiện theo yêu cầu báo cáo 35–40 trang: Codex hỗ trợ đọc
hướng dẫn và mã nguồn, đối chiếu CSV/JSON đã lưu, mở rộng sáu phần tiếng Việt,
viết công thức và phân tích hạn chế, trích logo nguyên trạng và dựng hai bìa
với danh tính do người dùng cung cấp. Tạo script sinh bảng không huấn luyện,
biên dịch XeLaTeX và render PDF để kiểm tra từng trang. Không sinh nhãn hay metric,
không chạy lại mô hình/notebook/ML tests, không điều chỉnh theo test lịch sử.
Phân công ghi là đề xuất chưa xác nhận; không giả danh commit của sinh viên.
Nguồn Mendeley và tài liệu scikit-learn được tra cứu để kiểm tra dẫn nguồn.
Nhóm vẫn phải kiểm chứng, hiểu, giải trình và xác nhận đóng góp thật trước nộp.

2026-11-17 — Cập nhật theo quy chuẩn bìa mới: Codex dùng Word ở chế độ chỉ đọc
để xuất riêng hai bìa tham chiếu, căn lại khung/logo/khối thông tin, đặt tiêu đề
15 pt và chữ còn lại 14 pt. Phần thân áp dụng Times New Roman 13 pt và H1/H2/H3
14/13/13 theo yêu cầu. Hỗ trợ biên dịch, rà hình ảnh và kiểm tra font thực trong
PDF bằng PyMuPDF. Không thay nội dung chuyên môn, thuật toán hoặc số liệu; một
đoạn liệt kê notebook chỉ được đổi cách căn lề. Không chạy lại mô hình hay tạo
kết quả thực nghiệm mới. Phân công vẫn là đề xuất chưa được hai sinh viên xác nhận.

2026-11-17 — Đối chiếu video người dùng: Codex hỗ trợ truy cập nguồn công khai,
kiểm tra các khung trình phát tại phần quy định và phân biệt minh họa Word với
quy tắc có thể dùng trong LaTeX. Không có transcript đầy đủ nên không khai báo
đã nghe toàn bộ video. Áp dụng lề, giãn dòng, vị trí/kiểu chú thích và APA-style;
giữ các cỡ chữ đã chốt và sáu phần FIT4013. Ba đoạn mở đầu phần tổng kết được
biên tập gọn, không xóa hay sửa kết quả/hạn chế. Cập nhật tham chiếu, kiểm tra
font/điều hướng/PDF, mở bản mới trong VS Code. Không chạy lại hoặc sửa thuật toán,
không sinh dữ liệu/nhãn/metric và không biến phân công dự kiến thành đóng góp thật.

2026-11-17 — Cập nhật heading theo yêu cầu mới: Codex cấu hình titlesec tập trung,
đánh số sáu chương và đồng bộ mục lục/tham chiếu, biên tập lời mở đầu, bảng phân công
và thêm URL repository. Thu gọn danh mục còn năm nguồn được chỉ định; ba trích dẫn
nguồn ngoài danh sách được thay bằng dẫn chứng vị trí mã nguồn tương ứng. Kiểm tra
font, liên kết và toàn bộ 40 trang sau XeLaTeX; hai bìa không đổi. Không chạy lại
training/notebook, không sửa thuật toán, dữ liệu hay số liệu thực nghiệm. Phân công
vẫn là đề xuất chờ xác nhận, không được coi là lịch sử đóng góp thực tế.

2026-11-17 — Chuẩn hóa toàn bộ 13 bảng phần thân: Codex thiết kế style chung,
chuyển sang tabularx, header nền nhẹ/đậm, đệm hàng và căn số; sửa cả script sinh
năm bảng. Bổ sung kiểu lưu/hướng xử lý dựa trên data_dictionary.csv, feature_audit.csv
và hợp đồng src/data.py đã có; không tự tạo dữ liệu. In đậm cực đại theo cột ở
hai bảng metric và giải thích cách đọc; không thay tiêu chí chọn mô hình.
Kiểm tra lại metric từ sáu confusion matrices, kiểm tra đầu ra sinh lặp ổn định,
đối chiếu các số thập phân với bản trước, biên dịch XeLaTeX, xem 40 trang và
13 ảnh chi tiết bảng, mở PDF mới trong VS Code. Không chạy lại ML/notebook hoặc
sửa thuật toán, nhãn, mẫu và số liệu. Phân công tiếp tục chờ nhóm xác nhận.

2026-11-17 — Chuyển 13 bảng phần thân sang trắng–đen theo yêu cầu: bỏ tô nền trong nguồn LaTeX và script sinh bảng, giữ header đậm, font 13 pt, kích thước cột, số liệu và caption; chuyển đường kẻ thành đen. Không chạy lại mô hình. Giữ hai bìa và cấu hình heading.

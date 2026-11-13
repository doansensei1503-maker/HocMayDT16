# Kế hoạch theo phụ thuộc và kết quả
1. Đọc tài liệu và nguồn: đã đọc PDF người dùng; annotation xác nhận slug Kaggle kết thúc -analysis. Không có AGENTS.md trong workspace trống.
2. Lập đối chiếu: requirements_traceability.md phân biệt rubric PDF với yêu cầu triển khai bổ sung của người dùng.
3. Kiểm tra schema trước training: đã xác minh hai file trong ZIP, CP1252, 180519×53 và mô tả target 0/1.
4. Xây lõi: data audit → group split → Pipeline A/B → CV trên train → khóa lựa chọn → test → lỗi ẩn danh.
5. Kiểm thử: 12 tests pass, gồm fixture tổng hợp phần mềm và contract thật tách biệt.
6. Chạy thật: baseline, Dummy, KNN/cây A/B; xuất bảng, hình, model. Notebook xác minh riêng; xem STATUS cập nhật cuối.
7. Báo cáo: sáu phần LaTeX, bảng/hình thật, slide nguồn. PDF chính thức bị chặn bởi compiler/template; đóng góp thành viên và GitHub cần nhóm tự bổ sung.
Không tự mở rộng mô hình, đổi dataset, push hoặc tạo đóng góp giả.

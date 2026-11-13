# Kết quả thực nghiệm thật

Run: results/runs/20261113T091908949239Z

SHA256: fa6d022ed437155e1a2f0378710602848703c8a7f203f7ff5d77805bf8480aa6

Tổng dữ liệu: 180519; dùng 5999 dòng; train 4823, test 1176.

Mô hình chọn bằng CV F1: tree_B. Không dùng test để chọn mô hình.



name,train_f1,cv_f1,test_f1,test_precision,test_recall,test_accuracy
baseline_tree_A,0.9994148624926856,0.6690671501845532,0.6588628762541806,0.6985815602836879,0.6234177215189873,0.6530612244897959
dummy_A,0.694369247428262,0.6943692728746124,0.6991150442477876,0.5374149659863946,1.0,0.5374149659863946
knn_A,0.9994148624926856,0.6668484672497889,0.6767676767676768,0.7230215827338129,0.6360759493670886,0.673469387755102
tree_A,0.7645753479927375,0.6741151774802926,0.6687898089171974,0.6730769230769231,0.6645569620253164,0.6462585034013606
knn_B,1.0,0.6714149185764907,0.6937759336099585,0.7294938917975567,0.6613924050632911,0.6862244897959183
tree_B,0.7136723163841808,0.7057533447737926,0.7097966728280961,0.8533333333333334,0.6075949367088608,0.7329931972789115


baseline_tree_A: train−CV F1=0.3303; CV−test F1=0.0102. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.

dummy_A: train−CV F1=-0.0000; CV−test F1=-0.0047. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.

knn_A: train−CV F1=0.3326; CV−test F1=-0.0099. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.

tree_A: train−CV F1=0.0905; CV−test F1=0.0053. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.

knn_B: train−CV F1=0.3286; CV−test F1=-0.0224. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.

tree_B: train−CV F1=0.0079; CV−test F1=-0.0040. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.

knn: B−A CV F1=0.0046; test F1=0.0170.

tree: B−A CV F1=0.0316; test F1=0.0410.

Ma trận test: TN=478, FP=66, FN=248, TP=384. FN bỏ sót đơn trễ; FP gây cảnh báo và phân bổ nguồn lực không cần thiết. Xác suất chưa hiệu chuẩn.

First Class: n=203, dương=193, FN=0, FP=10, FNR=0.0000, FPR=1.0000. Số đếm theo dòng, các dòng cùng đơn phụ thuộc nhau.

Same Day: n=71, dương=27, FN=0, FP=0, FNR=0.0000, FPR=0.0000. Số đếm theo dòng, các dòng cùng đơn phụ thuộc nhau.

Second Class: n=198, dương=158, FN=0, FP=40, FNR=0.0000, FPR=1.0000. Số đếm theo dòng, các dòng cùng đơn phụ thuộc nhau.

Standard Class: n=704, dương=254, FN=248, FP=16, FNR=0.9764, FPR=0.0356. Số đếm theo dòng, các dòng cùng đơn phụ thuộc nhau.

Tỷ lệ lỗi nhóm phải đi kèm mẫu số; mô tả không chứng minh nguyên nhân. Standard Class cần kiểm tra riêng vì bỏ sót có thể tập trung theo nhóm. Không dùng quan sát test này để chỉnh mô hình trong cùng thí nghiệm.

B có thêm lịch tạo đơn, nhưng khác biệt có thể do tương quan theo thời gian của tập dữ liệu. Random group split không đo khái quát sang tương lai. Một lần chia và tập con chưa đủ kết luận ổn định hoặc hiệu quả kinh doanh.
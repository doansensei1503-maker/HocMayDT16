from pathlib import Path
import json
import shutil
import pandas as pd

def render(out):
    out=Path(out)
    m=json.loads((out/'manifest.json').read_text(encoding='utf-8'))
    if m['status']!='COMPLETED':
        raise ValueError('Cannot report incomplete experiment')
    d=pd.read_csv(out/'tables'/'comparison.csv')
    winner=d.set_index('name').loc[m['selected_by_cv']]
    lines=['# Kết quả thực nghiệm thật',f'Run: {out.as_posix()}',f'SHA256: {m["data_sha256"]}',f'Tổng dữ liệu: {m["full_rows"]}; dùng {m["used_rows"]} dòng; train {m["train_rows"]}, test {m["test_rows"]}.',f'Mô hình chọn bằng CV F1: {m["selected_by_cv"]}. Không dùng test để chọn mô hình.','',d[['name','train_f1','cv_f1','test_f1','test_precision','test_recall','test_accuracy']].to_csv(index=False)]
    for _,r in d.iterrows():
        lines.append(f'{r["name"]}: train−CV F1={r["train_minus_cv_f1"]:.4f}; CV−test F1={r["cv_minus_test_f1"]:.4f}. Đây là dấu hiệu mô tả, không phải bằng chứng nhân quả.')
    pairs=[]
    for algo in ['knn','tree']:
        a=d.set_index('name').loc[algo+'_A']; b=d.set_index('name').loc[algo+'_B']
        pairs.append(f'{algo}: B−A CV F1={b.cv_f1-a.cv_f1:.4f}; test F1={b.test_f1-a.test_f1:.4f}.')
    lines+=pairs
    errors=pd.read_csv(out/'tables'/'errors_by_Shipping_Mode.csv').set_index('Shipping Mode')
    cm=pd.read_csv(out/'tables'/f'{m["selected_by_cv"]}_confusion.csv',index_col=0)
    tn,fp,fn,tp=cm.to_numpy().ravel()
    lines += [f'Ma trận test: TN={tn}, FP={fp}, FN={fn}, TP={tp}. FN bỏ sót đơn trễ; FP gây cảnh báo và phân bổ nguồn lực không cần thiết. Xác suất chưa hiệu chuẩn.']
    for group,row in errors.iterrows():
        lines.append(f'{group}: n={int(row.n)}, dương={int(row.actual_positive)}, FN={int(row.fn)}, FP={int(row.fp)}, FNR={row.fn_rate:.4f}, FPR={row.fp_rate:.4f}. Số đếm theo dòng, các dòng cùng đơn phụ thuộc nhau.')
    lines += ['Tỷ lệ lỗi nhóm phải đi kèm mẫu số; mô tả không chứng minh nguyên nhân. Standard Class cần kiểm tra riêng vì bỏ sót có thể tập trung theo nhóm. Không dùng quan sát test này để chỉnh mô hình trong cùng thí nghiệm.','B có thêm lịch tạo đơn, nhưng khác biệt có thể do tương quan theo thời gian của tập dữ liệu. Random group split không đo khái quát sang tương lai. Một lần chia và tập con chưa đủ kết luận ổn định hoặc hiệu quả kinh doanh.']
    summary='\n\n'.join(lines)
    (out/'summary_vi.md').write_text(summary,encoding='utf-8')
    cols=['train_f1','cv_f1','test_accuracy','test_precision','test_recall','test_f1']
    def esc(v):
        return str(v).replace('_',r'\_').replace('%',r'\%').replace('&',r'\&')
    tex=[r'\begin{tabular}{lrrrrrr}',r'\hline',r'Model & Train F1 & CV F1 & Acc & Prec & Recall & F1 \\',r'\hline']
    for _,r in d.iterrows():
        tex.append(esc(r['name'])+' & '+' & '.join(f'{r[c]:.3f}' for c in cols)+r' \\')
    tex += [r'\hline',r'\end{tabular}']
    (out/'tables'/'comparison.tex').write_text('\n'.join(tex),encoding='utf-8')
    # Publish only aggregate or privacy-filtered review artifacts, never split IDs/models/raw data.
    public_tables=Path('results/tables'); public_figs=Path('results/figures')
    public_tables.mkdir(parents=True,exist_ok=True); public_figs.mkdir(parents=True,exist_ok=True)
    for path in (out/'tables').iterdir():
        if path.name!='split.csv' and path.is_file(): shutil.copy2(path,public_tables/path.name)
    for path in (out/'figures').glob('*.png'): shutil.copy2(path,public_figs/path.name)
    shutil.copy2(out/'manifest.json',public_tables/'experiment_manifest.json')
    (public_tables/'summary_vi.md').write_text(summary,encoding='utf-8')
    text=[f'\\paragraph{{Phạm vi chạy thực tế}} Dữ liệu có {m["full_rows"]} dòng; thí nghiệm dùng {m["used_rows"]} dòng: train {m["train_rows"]}, test {m["test_rows"]}. Số nhóm tương ứng là {m["train_groups"]} và {m["test_groups"]}.',r'\resizebox{\textwidth}{!}{\input{../results/tables/comparison.tex}}',f'Mô hình chọn trước đánh giá test: {esc(m["selected_by_cv"])}; CV F1={winner.cv_f1:.4f}. Accuracy={winner.test_accuracy:.4f}, Precision={winner.test_precision:.4f}, Recall={winner.test_recall:.4f}, F1={winner.test_f1:.4f}. ROC-AUC={winner.test_roc_auc:.4f}, PR-AUC={winner.test_pr_auc:.4f}.',f'Ma trận nhầm lẫn: TN={tn}, FP={fp}, FN={fn}, TP={tp}. Không coi recall cao của Dummy (dự đoán tất cả trễ) là bằng chứng mô hình hữu ích.']
    for pair in pairs: text.append(esc(pair))
    baseline=d.set_index('name').loc['baseline_tree_A']
    text.append(f'Cây mặc định có train F1={baseline.train_f1:.4f}, CV F1={baseline.cv_f1:.4f}; chênh lệch lớn gợi ý overfitting. Mô hình chọn có chênh lệch train--CV={winner.train_minus_cv_f1:.4f}. Một split chưa cho phép kết luận tổng quát.')
    for group,row in errors.iterrows():
        text.append(f'{esc(group)}: {int(row.n)} dòng, {int(row.actual_positive)} dương, FN={int(row.fn)}, FP={int(row.fp)}. FNR={row.fn_rate:.4f}, FPR={row.fp_rate:.4f}.')
    text.append('Lỗi tập trung cần được điều tra bằng dữ liệu vận hành; đây là bằng chứng mô tả, không là nguyên nhân đã xác minh. Không điều chỉnh mô hình dựa trên những quan sát test này.')
    for name,caption in [('comparison.png','So sánh các cấu hình đã định trước.'),(m['selected_by_cv']+'_confusion.png','Ma trận nhầm lẫn của mô hình chọn bằng CV.'),('01_classes.png','Phân bố nhãn trên train.'),('05_shipping.png','Phân bố nhãn theo phương thức giao hàng trên train.'),('08_month.png','Tỷ lệ giao trễ theo tháng tạo đơn trên train.')]:
        text.append(r'\begin{figure}[ht]\centering\includegraphics[width=.9\textwidth]{../results/figures/'+name+r'}\caption{'+caption+r'}\end{figure}')
    Path('report').mkdir(parents=True, exist_ok=True)
    Path('report/generated.tex').write_text('\n\n'.join(text),encoding='utf-8')

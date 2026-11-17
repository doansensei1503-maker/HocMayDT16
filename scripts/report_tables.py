"""Render report tables only from existing aggregate artifacts; never train."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / 'results/tables'
OUT = ROOT / 'report/tables'


def read(name):
    with (TABLES / name).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def esc(value):
    return str(value).replace('_', r'\_').replace('%', r'\%').replace('&', r'\&')


def table(name, headers, rows, caption, label, spec, *, best_columns=(), groups=None, note=None):
    """Render 13pt tables; bold maxima only for metrics where larger is better."""
    maxima = {col: max(float(row[col]) for row in rows) for col in best_columns}
    text = [r'\begin{table}[!htbp]\centering',
            r'\caption{' + caption + r'}\label{' + label + '}',
            r'\begin{tabularx}{\linewidth}{' + spec + r'}\toprule']
    if groups:
        text += [r'\rowcolor{reportheader} ' + groups]
    text += [r'\rowcolor{reportheader} ' + ' & '.join(r'\theadcell{' + h + '}' for h in headers) + r' \\\midrule']
    for row in rows:
        cells = []
        for col,value in enumerate(row):
            cell = esc(value)
            if col in maxima and float(value) == maxima[col]:
                cell = r'\textbf{' + cell + '}'
            cells.append(cell)
        text.append(' & '.join(cells) + r' \\')
    text += [r'\bottomrule\end{tabularx}']
    if note:
        text += [r'\par\smallskip\raggedright ' + note]
    text += [r'\end{table}']
    (OUT / name).write_text('\n'.join(text) + '\n', encoding='utf-8')


def model_cells(name):
    algorithm, flow = name.rsplit('_', 1)
    labels = {'baseline_tree': 'Cây cơ sở', 'dummy': 'Dummy', 'knn': 'K-NN', 'tree': 'Cây'}
    return [labels[algorithm], flow]


def main():
    OUT.mkdir(exist_ok=True)
    models = read('comparison.csv')
    for model in models:
        name = model['name']
        cm = read(name + '_confusion.csv')
        tn, fp = (int(cm[0][k]) for k in ['pred_0', 'pred_1'])
        fn, tp = (int(cm[1][k]) for k in ['pred_0', 'pred_1'])
        assert tn + fp + fn + tp == 1176
        expected = {'test_accuracy': (tn+tp)/1176, 'test_precision': tp/(tp+fp),
                    'test_recall': tp/(tp+fn), 'test_f1': 2*tp/(2*tp+fp+fn)}
        for metric, value in expected.items():
            assert abs(float(model[metric]) - value) < 1e-12, (name, metric)
        print(f'{name}: TN={tn}, FP={fp}, FN={fn}, TP={tp}')
    manifest = json.loads((TABLES / 'experiment_manifest.json').read_text(encoding='utf-8'))
    assert max(models, key=lambda m: float(m['cv_f1']))['name'] == manifest['selected_by_cv']
    metric_keys = ['cv_f1','test_accuracy','test_precision','test_recall','test_f1']
    table('model_metrics.tex', ['Mô hình','Luồng','F1','Accuracy','Precision','Recall','F1'],
          [model_cells(m['name']) + [f'{float(m[k]):.4f}' for k in metric_keys] for m in models],
          'So sánh sáu ứng viên: CV trên train và metric trên test lịch sử.', 'tab:metrics', 'Ycrrrrr',
          best_columns=range(2,7),
          groups=r'\multicolumn{2}{c}{\theadcell{Ứng viên}} & \theadcell{CV} & \multicolumn{4}{c}{\theadcell{Test}} \\',
          note=r'In đậm: giá trị lớn nhất từng cột; chọn mô hình bằng CV F1, không theo test. Cây cơ sở là baseline\_tree; Cây là tree đã tìm tham số.')
    table('generalization.tex', ['Mô hình','Luồng','Train F1','CV F1','SD CV','Train--CV'],
          [model_cells(m['name']) + [f'{float(m[k]):.4f}' for k in ['train_f1','cv_f1','cv_f1_std','train_minus_cv_f1']] for m in models],
          'Mức khớp trên train, CV và chênh lệch F1 của sáu ứng viên.', 'tab:gaps', 'Ycrrrr')
    orders = []
    for name in ['tree_B','dummy_A']:
        m = json.loads((TABLES / (name+'_order_metrics.json')).read_text())
        tn, fp = m['confusion_matrix'][0]
        fn, tp = m['confusion_matrix'][1]
        assert m['orders'] == 423 and abs(m['f1']-2*tp/(2*tp+fp+fn)) < 1e-12
        orders.append(model_cells(name)+[f'{m[k]:.4f}' for k in ['accuracy','precision','recall','f1']])
    table('order_metrics.tex', ['Mô hình','Luồng','Accuracy','Precision','Recall','F1'], orders,
          'Metric theo đơn, xác suất trung bình và ngưỡng 0,5 cố định.', 'tab:orders', 'Ycrrrr', best_columns=range(2,6),
          note=r'In đậm: giá trị lớn nhất từng cột; đơn vị đánh giá là đơn hàng.')
    ablation = read('time_ablation_cv.csv')
    rows = []
    for algorithm in ['knn','tree']:
        a, b = [next(float(r['test_f1']) for r in ablation if r['algorithm']==algorithm and r['flow']==f) for f in ['A','B']]
        rows.append([algorithm, f'{a:.4f}', f'{b:.4f}', f'{b-a:+.4f}'])
    table('ablation.tex', ['Thuật toán','A: CV F1','B: CV F1','B--A'], rows,
          'Ablation lịch trên CV train với tham số của A được giữ cố định.', 'tab:ablation', 'Yrrr')
    errors = read('errors_by_Shipping_Mode.csv')
    table('shipping_errors.tex', ['Phương thức','n','Dương','FN','FP','FNR','FPR'],
          [[r['Shipping Mode']] + [str(int(float(r[k]))) for k in ['n','actual_positive','fn','fp']] + [f'{float(r[k]):.4f}' for k in ['fn_rate','fp_rate']] for r in errors],
          'Lỗi theo dòng của cây B, kèm mẫu số nhóm dịch vụ.', 'tab:shipping-errors', 'Yrrrrrr')
    assert sum(int(r['fn']) for r in errors) == 248
    assert sum(int(r['fp']) for r in errors) == 66
    print('VERIFIED: six confusion matrices, row metrics, CV winner, order F1 and grouped errors; no training.')


if __name__ == '__main__':
    main()

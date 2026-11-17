"""Inspect actual PDF font sizes and bounds; does not train or edit ML artifacts.

Requires PyMuPDF. The local review-only installation can live in report/build/tools.
"""
import json
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL_TOOLS = ROOT / 'report/build/tools'
if LOCAL_TOOLS.is_dir():
    sys.path.insert(0, str(LOCAL_TOOLS))
import pymupdf


def compact(text):
    return re.sub(r'\s+', '', text)


def spans(page):
    return [s for b in page.get_text('dict')['blocks'] if 'lines' in b
            for line in b['lines'] for s in line['spans'] if s['text'].strip()]


def at_size(span, size):
    return abs(span['size'] - size) < .015


def main():
    pdf = pymupdf.open(ROOT / 'report/final_report.pdf')
    cover_titles = ['TRƯỜNG ĐẠI HỌC ĐẠI NAM', 'KHOA CÔNG NGHỆ THÔNG TIN',
                    'BÁO CÁO HỌC PHẦN', 'NHẬP MÔN HỌC MÁY — FIT4013', 'ĐỀ TÀI 16',
                    'DỰ ĐOÁN ĐƠN HÀNG CÓ NGUY CƠ', 'GIAO TRỄ TRONG CHUỖI CUNG ỨNG']
    result = {'pages': len(pdf),
              'pdf_sha256': hashlib.sha256((ROOT / 'report/final_report.pdf').read_bytes()).hexdigest(),
              'covers': [], 'body': {}}
    for index in range(2):
        page = pdf[index]
        ss = spans(page)
        assert all(s['size'] >= 14-.015 for s in ss)
        assert all(at_size(s, 14) or at_size(s, 15) for s in ss)
        assert all('TimesNewRoman' in s['font'] for s in ss)
        for title in cover_titles:
            matching = [s for s in ss if compact(title) in compact(s['text'])]
            assert matching, (index+1, title)
            assert all(at_size(s, 15) and 'Bold' in s['font'] for s in matching)
        # Rectangles match the respective Word page, with a small stroke allowance.
        frame = pymupdf.Rect(22.5, 18, 181.5, 278.1) if index == 0 else pymupdf.Rect(28.55, 18.1, 187.55, 275.5)
        frame = pymupdf.Rect(*(v*72/25.4 for v in frame))
        for s in ss:
            assert frame.contains(pymupdf.Rect(s['bbox'])), (index+1, s['text'], s['bbox'])
        assert not any(s['text'].strip().isdigit() for s in ss), 'Unexpected cover page number'
        for text in ['1871020143', '1871020223', 'ThS. Lê Thị Thùy Trang', 'CNTT18-10', 'K18', '2026–2027']:
            assert compact(text) in compact(page.get_text()), (index+1, text)
        for forbidden in ['FIT4006', 'Lê Văn Phong', 'ĐỀ TÀI 38', 'Packet Tracer']:
            assert compact(forbidden) not in compact(page.get_text())
        result['covers'].append({'page': index+1, 'sizes_pt': sorted({round(s['size'], 3) for s in ss}),
                                  'min_pt': round(min(s['size'] for s in ss), 3),
                                  'titles_15pt_bold': True, 'all_text_times_new_roman': True,
                                  'inside_word_frame': True, 'page_number': False})
    # Table headings and contents are explicitly 14 points, including bold headings.
    table_spans = [s for s in spans(pdf[1]) if 185*72/25.4 <= s['bbox'][1] <= 242*72/25.4]
    assert table_spans and all(at_size(s, 14) for s in table_spans)
    for header in ['Hạng mục', 'Thông tin']:
        assert any(compact(header) == compact(s['text']) for s in table_spans)
    result['covers'][1]['table_all_14pt'] = True
    assert compact(pdf[2].get_text()).startswith(compact('LỜI MỞ ĐẦU')), 'Cover overflow onto page 3'

    body_spans = [s for page in list(pdf)[2:] for s in spans(page)]
    math_scripts = set()
    for page in list(pdf)[2:]:
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                if any(s['font'].startswith('CM') for s in line['spans']):
                    math_scripts.update(tuple(s['bbox']) for s in line['spans']
                                        if 'TimesNewRoman' in s['font'] and at_size(s, 9.1))
    body_text = [s for s in body_spans if 'TimesNewRoman' in s['font']
                 and tuple(s['bbox']) not in math_scripts]
    assert all(at_size(s, 13) or (at_size(s, 14) and 'Bold' in s['font']) for s in body_text)
    assert not any('Arial' in s['font'] or 'Consolas' in s['font'] for s in body_spans)
    h1 = ['Đặt vấn đề và phân tích yêu cầu', 'Thiết kế giải pháp và quy trình học máy',
          'Phân tích mã nguồn và chức năng', 'Thử nghiệm và kết quả',
          'Thảo luận và so sánh', 'Tổng kết và hướng phát triển']
    expected_h1 = [f'CHƯƠNG {i}. {title.upper()}' for i,title in enumerate(h1,1)]
    expected_h1 += ['LỜI MỞ ĐẦU', 'PHÂN CÔNG NHIỆM VỤ', 'MỤC LỤC',
                    'DANH MỤC HÌNH ẢNH', 'DANH MỤC BẢNG BIỂU', 'TÀI LIỆU THAM KHẢO']
    found_h1 = []
    for page in list(pdf)[2:]:
        for block in page.get_text('dict')['blocks']:
            lines = [line for line in block.get('lines', []) if any(at_size(s,14) for s in line['spans'])]
            if not lines:
                continue
            heading = ' '.join(s['text'] for line in lines for s in line['spans'])
            assert compact(heading) in [compact(x) for x in expected_h1], heading
            for line in lines:
                assert all(at_size(s,14) and 'Bold' in s['font'] and 'Italic' not in s['font'] for s in line['spans'])
                assert abs((line['bbox'][0]+line['bbox'][2])/2 - (25*72/25.4+(595.276-45*72/25.4)/2)) < 1, line
            found_h1.append(compact(heading))
    assert sorted(found_h1) == sorted(map(compact,expected_h1)), found_h1
    result['body'] = {'h1_14pt_bold': True, 'h1_centered_uppercase': True, 'h1_count': len(found_h1), 'times_text_sizes_pt': sorted({round(s['size'], 3) for s in body_text}),
                      'normal_tables_captions_13pt': True, 'h2_13pt_bold': True,
                      'h3': '13pt bold italic configured; no H3 heading in current content',
                      'page3_starts_introduction': True, 'math_script_spans_9pt1': len(math_scripts)}
    # H2 headings use numbered text lines; check the entire heading line's fonts.
    h2_count = 0
    caption_count = 0
    for page in list(pdf)[2:]:
        for b in page.get_text('dict')['blocks']:
            for line in b.get('lines', []):
                ss = [s for s in line['spans'] if s['text'].strip()]
                text = ''.join(s['text'] for s in ss)
                if re.fullmatch(r'[1-6]\.\d+', text.strip()) and abs(ss[0]['bbox'][0]-25*72/25.4)<1 and all('Bold' in s['font'] for s in ss):
                    assert all(at_size(s, 13) and 'Bold' in s['font'] for s in ss), text
                    h2_count += 1
                if re.match(r'^(Hình|Bảng)\s*\d+:', text):
                    assert all(at_size(s, 13) for s in ss), text
                    caption_count += 1
    expected_h2 = sum(p.read_text(encoding='utf-8-sig').count(r'\subsection{')
                      for p in (ROOT / 'report/sections').glob('*.tex'))
    assert h2_count == expected_h2, (h2_count, expected_h2)
    assert caption_count == 27, caption_count
    result['body'].update(h2_count=h2_count, caption_count=caption_count)
    result['note'] = ('Cover audit includes every typeset text span. Body normal text, tables and captions are 13pt; '
                      'mathematical subscripts use their natural script size. Raster logos/plots retain source artwork.')
    path = ROOT / 'docs/COVER_TYPOGRAPHY_AUDIT.json'
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

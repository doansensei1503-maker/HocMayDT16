"""Audit actual PDF table fonts, header fills and layout; no ML execution."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'report/build/tools'))
import pymupdf


def main():
    path = ROOT/'report/final_report.pdf'
    pdf = pymupdf.open(path)
    checked = []
    for number,page in enumerate(pdf,1):
        if number <= 2:  # Covers have their independently locked 14/15pt styles.
            continue
        drawings = page.get_drawings()
        rules = sorted([d['rect'].y0 for d in drawings if d['type']=='s'
                        and abs(d.get('width',0)-.9564)<.015
                        and abs(d['rect'].width-467.717)<1 and d['rect'].height<.1])
        assert len(rules)%2 == 0, (number,rules)
        spans = [s for b in page.get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l['spans'] if s['text'].strip()]
        for top,bottom in zip(rules[::2],rules[1::2]):
            cells = [s for s in spans if top < (s['bbox'][1]+s['bbox'][3])/2 < bottom]
            assert cells
            assert all(abs(s['size']-13)<.015 and 'TimesNewRoman' in s['font'] for s in cells),number
            assert all(s['bbox'][0]>=70.866-1 and s['bbox'][2]<=538.583+1 for s in cells),(number, cells)
            assert 56 < top < bottom < 785.3,(number,top,bottom)
            fills = [d['rect'] for d in drawings if d['fill'] and len(d['fill'])==3
                     and all(abs(a-b)<.003 for a,b in zip(d['fill'],(.902,.925,.945)))
                     and top < d['rect'].y0 < bottom]
            assert fills,(number,top)
            headers = [s for s in cells if any(r.contains(pymupdf.Point((s['bbox'][0]+s['bbox'][2])/2,(s['bbox'][1]+s['bbox'][3])/2)) for r in fills)]
            assert headers and all('Bold' in s['font'] for s in headers),number
            captions = [s for s in spans if s['bbox'][3]<=top+1 and re.match(r'^Bảng\s*\d+:',s['text'])]
            assert captions,number
            caption = max(captions,key=lambda s:s['bbox'][1])
            index = int(re.search(r'\d+',caption['text'])[0])
            checked.append({'table':index,'pdf_page':number,'all_cell_text_13pt_times_new_roman':True,
                            'header_bold_light_fill':True,'inside_text_margins':True,
                            'bounds_pt':[70.866,round(top,3),538.583,round(bottom,3)]})
    assert sorted(x['table'] for x in checked)==list(range(1,14)),checked
    result={'pdf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'pages':len(pdf),
            'tables_checked':len(checked),'arraystretch':1.22,'cover_tables':'unchanged 14pt exception',
            'tables':checked}
    (ROOT/'docs/TABLE_LAYOUT_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()

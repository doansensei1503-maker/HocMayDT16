"""Verify actual PDF bookmarks and links rather than only LaTeX source labels."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
local_tools = ROOT / 'report/build/tools'
if local_tools.is_dir():
    sys.path.insert(0, str(local_tools))
import pymupdf


def compact(text):
    return re.sub(r'\s+', '', text)


def main():
    path = ROOT / 'report/final_report.pdf'
    pdf = pymupdf.open(path)
    titles = ['Mục lục', 'Danh mục hình', 'Danh mục bảng', 'Tài liệu tham khảo']
    headings = {}
    for number, page in enumerate(pdf, 1):
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    if abs(span['size']-14) < .015 and 'Bold' in span['font']:
                        for title in titles:
                            if compact(span['text']) == compact(title):
                                headings[title] = number
    assert set(headings) == set(titles), headings
    bookmarks = pdf.get_toc()
    verified = []
    for title in titles:
        found = [entry for entry in bookmarks if compact(entry[1]) == compact(title)]
        assert len(found) == 1 and found[0][2] == headings[title], (title, found, headings)
        verified.append({'title': title, 'pdf_page': headings[title], 'bookmark_correct': True})
    toc_start = headings['Mục lục']-1
    toc_end = headings['Danh mục hình']-1
    checked_toc_links = {}
    for page in list(pdf)[toc_start:toc_end]:
        for link in page.get_links():
            text = compact(page.get_textbox(link['from']))
            for title in titles[1:]:
                if compact(title) == text:
                    assert link.get('page', -1)+1 == headings[title], (title, link)
                    checked_toc_links[title] = True
    assert set(checked_toc_links) == set(titles[1:]), checked_toc_links
    internal = 0
    for page in pdf:
        for link in page.get_links():
            if link['kind'] in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED) and 'page' in link:
                assert 0 <= link['page'] < len(pdf), link
                internal += 1
    assert internal > 0
    result = {'pdf_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'pages': len(pdf), 'bookmarks': verified,
              'toc_links_correct': checked_toc_links,
              'internal_links_with_valid_page': internal}
    (ROOT / 'docs/REPORT_NAVIGATION_AUDIT.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

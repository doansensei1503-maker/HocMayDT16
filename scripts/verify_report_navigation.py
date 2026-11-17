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
    titles = ['MỤC LỤC', 'DANH MỤC HÌNH ẢNH', 'DANH MỤC BẢNG BIỂU', 'TÀI LIỆU THAM KHẢO']
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
    toc_start = headings['MỤC LỤC']-1
    toc_end = headings['DANH MỤC HÌNH ẢNH']-1
    checked_toc_links = {}
    for page in list(pdf)[toc_start:toc_end]:
        for link in page.get_links():
            text = compact(page.get_textbox(link['from']))
            for title in titles[1:]:
                if compact(title) == text:
                    assert link.get('page', -1)+1 == headings[title], (title, link)
                    checked_toc_links[title] = True
    assert set(checked_toc_links) == set(titles[1:]), checked_toc_links
    front = ['LỜI MỞ ĐẦU', 'PHÂN CÔNG NHIỆM VỤ']
    for title in front:
        found = [entry for entry in bookmarks if compact(entry[1]) == compact(title)]
        assert len(found) == 1 and found[0][2] == 3, (title,found)
    chapters = []
    toc_text = compact(''.join(p.get_text() for p in list(pdf)[toc_start:toc_end]))
    for i,source in enumerate(sorted((ROOT/'report/sections').glob('*.tex')),1):
        title = re.search(r'\\partstart\{([^}]+)\}',source.read_text(encoding='utf-8-sig'))[1].upper()
        found = [entry for entry in bookmarks if compact(entry[1]) == compact(title)]
        assert len(found) == 1, (title,found)
        target = found[0][2]
        full_title = f'CHƯƠNG {i}. {title}'
        assert compact(full_title) in compact(pdf[target-1].get_text()),full_title
        assert compact(full_title) in toc_text,full_title
        chapter_links = [link for p in list(pdf)[toc_start:toc_end] for link in p.get_links()
                         if compact(title) in compact(p.get_textbox(link['from']))]
        assert len(chapter_links) == 1 and chapter_links[0].get('page',-1)+1 == target, (title,chapter_links)
        chapters.append({'title':full_title,'pdf_page':target,'toc_title_and_target_correct':True})
    github = 'https://github.com/doansensei1503-maker/HocMayDT16'
    github_pages = [p for p in pdf if any(l.get('uri') == github for l in p.get_links())]
    assert github_pages and any(compact(github) in compact(p.get_text()) for p in github_pages)
    for p in github_pages:
        for link in p.get_links():
            if link.get('uri') == github:
                assert link['from'].x0 >= 25*72/25.4-1 and link['from'].x1 <= p.rect.width-20*72/25.4+1
    refs = (ROOT/'report/references.tex').read_text(encoding='utf-8-sig')
    keys = set(re.findall(r'\\bibitem\[[^]]+\]\{([^}]+)\}',refs))
    assert keys == {'fit','dataco','kaggle','knn','tree'},keys
    active = '\n'.join(p.read_text(encoding='utf-8-sig') for p in (ROOT/'report/sections').glob('*.tex'))
    citations = {key.strip() for group in re.findall(r'\\cite[a-z]*\{([^}]+)\}',active) for key in group.split(',')}
    assert citations == keys, (citations,keys)
    internal = 0
    for page in pdf:
        for link in page.get_links():
            if link['kind'] in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED) and 'page' in link:
                assert 0 <= link['page'] < len(pdf), link
                internal += 1
    assert internal > 0
    result = {'pdf_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'pages': len(pdf), 'bookmarks': verified, 'chapters': chapters,
              'front_matter_targets_correct': True, 'github_clickable_full_url_within_margins': True,
              'bibliography_keys': sorted(keys), 'citations_resolved_exact_five_sources': True,
              'toc_links_correct': checked_toc_links,
              'internal_links_with_valid_page': internal}
    (ROOT / 'docs/REPORT_NAVIGATION_AUDIT.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

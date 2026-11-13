from pathlib import Path
p=Path('report/main.tex')
s=p.read_text(encoding='utf-8-sig')
s=s.replace(r'\section{Thảo luận và so sánh}',r'\section{Thảo luận và so sánh}'+'\n'+r'\input{analysis.tex}')
p.write_text(s,encoding='utf-8')

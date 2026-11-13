"""Execute notebooks locally; outputs are actual kernel executions."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient
root=Path.cwd()
for path in sorted((root/'notebooks').glob('*.ipynb')):
    nb=nbformat.read(path,as_version=4)
    for i,cell in enumerate(nb.cells):
        cell['id']=f'cell-{i}'
    NotebookClient(nb,timeout=600,kernel_name='python3',resources={'metadata':{'path':str(root)}}).execute()
    nbformat.write(nb,path)
    print('EXECUTED',path.name,flush=True)

$ErrorActionPreference = 'Stop'
py -m pytest -q
if ($LASTEXITCODE -ne 0) { throw 'Tests failed' }
py -m src.run --config configs/default.json
if ($LASTEXITCODE -ne 0) { throw 'Experiment failed' }
py -X utf8 -m scripts.finalize_evidence
if ($LASTEXITCODE -ne 0) { throw 'Evidence generation failed' }

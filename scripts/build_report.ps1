[CmdletBinding()]
param(
    [switch]$BuildSlides
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$xelatexCommand = Get-Command 'xelatex' -ErrorAction SilentlyContinue
$xelatexPath = if ($xelatexCommand) {
    $xelatexCommand.Source
}
else {
    Join-Path $env:LOCALAPPDATA 'Programs\MiKTeX\miktex\bin\x64\xelatex.exe'
}

if (-not (Test-Path -LiteralPath $xelatexPath -PathType Leaf)) {
    throw 'XeLaTeX was not found on PATH or in the standard MiKTeX user-install path. Install/configure MiKTeX or TeX Live and retry.'
}

$kpsewhichCommand = Get-Command 'kpsewhich' -ErrorAction SilentlyContinue
$kpsewhichPath = if ($kpsewhichCommand) {
    $kpsewhichCommand.Source
}
else {
    Join-Path (Split-Path -Parent $xelatexPath) 'kpsewhich.exe'
}
if (-not (Test-Path -LiteralPath $kpsewhichPath -PathType Leaf)) {
    throw 'kpsewhich was not found; cannot safely preflight TeX packages without triggering an on-demand installer.'
}

$requiredTexFiles = @(
    'fontspec.sty',
    'babel.sty',
    'vietnamese.ldf',
    'geometry.sty',
    'graphicx.sty',
    'booktabs.sty',
    'hyperref.sty',
    'infwarerr.sty'
)
$missingTexFiles = @()
$previousErrorPreference = $ErrorActionPreference
try {
    $ErrorActionPreference = 'Continue'
    foreach ($texFile in $requiredTexFiles) {
        $resolvedTexFile = & $kpsewhichPath $texFile 2>$null
        $lookupExitCode = $LASTEXITCODE
        if ($lookupExitCode -ne 0 -or -not $resolvedTexFile) {
            $missingTexFiles += $texFile
        }
    }
}
finally {
    $ErrorActionPreference = $previousErrorPreference
}
if ($missingTexFiles.Count -gt 0) {
    throw "Required TeX files are not installed: $($missingTexFiles -join ', '). Install them manually in the user-level TeX distribution. This script never opens the MiKTeX Console or installs packages."
}

$requiredReportFiles = @(
    'report\main.tex',
    'report\generated.tex',
    'report\analysis.tex',
    'report\repair_analysis.tex',
    'results\tables\comparison.tex',
    'results\tables\tree_B_order_metrics.json',
    'results\tables\dummy_A_order_metrics.json',
    'results\tables\time_ablation_cv.csv',
    'results\tables\sampling_groups.json',
    'results\figures\comparison.png',
    'results\figures\baseline_tree_A_confusion.png',
    'results\figures\dummy_A_confusion.png',
    'results\figures\knn_A_confusion.png',
    'results\figures\knn_B_confusion.png',
    'results\figures\tree_A_confusion.png',
    'results\figures\tree_B_confusion.png',
    'results\figures\01_classes.png',
    'results\figures\02_missing.png',
    'results\figures\03_numeric_hist.png',
    'results\figures\04_boxplot.png',
    'results\figures\05_shipping.png',
    'results\figures\06_regions.png',
    'results\figures\07_correlation.png',
    'results\figures\08_month.png'
)

foreach ($relativePath in $requiredReportFiles) {
    $path = Join-Path $repositoryRoot $relativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Required report input is missing: $relativePath"
    }
}

$timesFont = Join-Path $env:WINDIR 'Fonts\times.ttf'
if (-not (Test-Path -LiteralPath $timesFont -PathType Leaf)) {
    throw "Times New Roman was not found at $timesFont. Install the required font before building."
}
if ($BuildSlides) {
    $arialFont = Join-Path $env:WINDIR 'Fonts\arial.ttf'
    if (-not (Test-Path -LiteralPath $arialFont -PathType Leaf)) {
        throw "Arial was not found at $arialFont. Install the required font before building slides."
    }
}

if (-not (Test-Path -LiteralPath (Join-Path $repositoryRoot 'docs\fit4013_extracted.txt'))) {
    Write-Warning 'The official instructions text is missing; template compliance cannot be checked.'
}
else {
    Write-Warning 'This build uses the provisional article source, not a verified official course template.'
}

function Invoke-XeLatexBuild {
    param(
        [Parameter(Mandatory = $true)][string]$SourceDirectory,
        [Parameter(Mandatory = $true)][string]$SourceFile,
        [Parameter(Mandatory = $true)][string]$JobName,
        [Parameter(Mandatory = $true)][string]$PublishedPdf
    )

    $buildDirectory = Join-Path $SourceDirectory 'build'
    New-Item -ItemType Directory -Path $buildDirectory -Force | Out-Null
    $logPath = Join-Path $buildDirectory ($JobName + '-build.log')
    Set-Content -LiteralPath $logPath -Value "XeLaTeX build: $SourceFile" -Encoding UTF8

    Push-Location $SourceDirectory
    try {
        for ($pass = 1; $pass -le 2; $pass++) {
            Write-Host "Building $SourceFile (pass $pass/2)..."
            $arguments = @(
                '-interaction=nonstopmode',
                '-halt-on-error',
                '-file-line-error',
                "-output-directory=$buildDirectory",
                "-jobname=$JobName",
                $SourceFile
            )
            $previousErrorPreference = $ErrorActionPreference
            try {
                $ErrorActionPreference = 'Continue'
                & $xelatexPath @arguments 2>&1 | Tee-Object -FilePath $logPath -Append
                $compilerExitCode = $LASTEXITCODE
            }
            finally {
                $ErrorActionPreference = $previousErrorPreference
            }
            if ($compilerExitCode -ne 0) {
                $compilerLog = Get-Content -LiteralPath $logPath -Raw
                if ($compilerLog -match "File '([^']+\.sty)' not found") {
                    throw "Required LaTeX package '$($Matches[1])' is missing. Install it in the user-level TeX distribution, then retry. See $logPath"
                }
                throw "XeLaTeX failed on pass $pass for $SourceFile (exit $compilerExitCode). See $logPath"
            }
        }
    }
    finally {
        Pop-Location
    }

    $builtPdf = Join-Path $buildDirectory ($JobName + '.pdf')
    if (-not (Test-Path -LiteralPath $builtPdf -PathType Leaf)) {
        throw "XeLaTeX returned success but did not produce $builtPdf"
    }
    if ((Get-Item -LiteralPath $builtPdf).Length -le 0) {
        throw "The generated PDF is empty: $builtPdf"
    }

    Copy-Item -LiteralPath $builtPdf -Destination $PublishedPdf -Force
    Write-Host "PDF created: $PublishedPdf"
    Write-Host "Build log: $logPath"
}

$reportDirectory = Join-Path $repositoryRoot 'report'
Invoke-XeLatexBuild `
    -SourceDirectory $reportDirectory `
    -SourceFile 'main.tex' `
    -JobName 'final_report' `
    -PublishedPdf (Join-Path $reportDirectory 'final_report.pdf')

if ($BuildSlides) {
    $slidesDirectory = Join-Path $repositoryRoot 'slides'
    $presentationSource = Join-Path $slidesDirectory 'presentation.tex'
    if (-not (Test-Path -LiteralPath $presentationSource -PathType Leaf)) {
        throw "Slide source is missing: $presentationSource"
    }
    Invoke-XeLatexBuild `
        -SourceDirectory $slidesDirectory `
        -SourceFile 'presentation.tex' `
        -JobName 'presentation' `
        -PublishedPdf (Join-Path $slidesDirectory 'presentation.pdf')
}

Write-Host 'Build completed. PDF visual inspection and official-template compliance must be verified separately.'

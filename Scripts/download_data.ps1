# scripts/download_data.ps1
# Run from project root in PowerShell
mkdir data\raw -ErrorAction SilentlyContinue
Write-Host "Downloading HiRISE sample (Zenodo) - if direct link fails, download manually from Zenodo page..."
curl -L -o data\raw\hirise_landmarks_v3.zip "https://zenodo.org/record/2538136/files/hirise-map-proj-v3_2.zip"
Write-Host "If curl failed, open https://zenodo.org/record/2538136 and download file manually into data\\raw"

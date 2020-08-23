$PathToFiles = 'Notebooks/data/transcripts/Chappelle'
#Get-Content -Path .\*.txt | ConvertTo-Json | Out-Host
(Get-Content -Path $PathToFiles) |
    ForEach-Object { $_ -Replace '' }
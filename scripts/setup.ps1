param (
    [string]$endpoint = "",
    [string]$key = "",
    [string]$location = ""
 )

[System.Environment]::SetEnvironmentVariable('azurecognitiveservicesendpoint', $endpoint, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable('azurecognitiveserviceskey', $key, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable('azurecognitiveserviceslocation', $location, [System.EnvironmentVariableTarget]::Machine)

cd C:\
mkdir code
cd code
git clone "https://github.com/ACloudGuru/content-AI-900.git"

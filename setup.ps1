param (
    [string]$endpoint = "",
    [string]$key = "",
    [string]$location = ""
 )

[System.Environment]::SetEnvironmentVariable('azurecognitiveservicesendpoint', $endpoint, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable('azurecognitiveserviceskey', $key, [System.EnvironmentVariableTarget]::Machine)
[System.Environment]::SetEnvironmentVariable('azurecognitiveserviceslocation', $location, [System.EnvironmentVariableTarget]::Machine)

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco install python --version=3.9.6 -y
choco install git.install -y

$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
Update-SessionEnvironment

python -m pip install -U pip

pip install azure-cognitiveservices-vision-computervision==0.9.0
pip install azure-cognitiveservices-vision-face==0.5.0
pip install azure-ai-textanalytics==5.1.0
pip install Pillow==8.3.1

cd C:\
mkdir code
cd code
git clone "https://github.com/ACloudGuru/content-AI-900.git"

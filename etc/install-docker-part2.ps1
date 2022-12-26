Set-Content -Value "`{`"experimental`":true`}" -Path C:\ProgramData\docker\config\daemon.json
restart-service docker
cd 'C:\Program Files\'
mkdir "Linux Containers"
cd '.\Linux Containers\'
curl -OutFile release.zip https://github.com/linuxkit/lcow/releases/download/v4.14.35-v0.3.9/release.zip
Expand-Archive -DestinationPath . .\release.zip
rm release.zip
Install-WindowsFeature Hyper-V –IncludeManagementTools –Restart
docker run -it --platform=linux busybox echo "LCOW on a Windows Server!"
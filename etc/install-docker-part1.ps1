Uninstall-Package Docker -ProviderName DockerProvider
Install-Module "DockerMsftProvider" -Force
Update-Module "DockerMsftProvider"
Install-Package Docker -ProviderName "DockerMsftProvider" -Update -Force
Install-WindowsFeature Containers
Restart-Computer
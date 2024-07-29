@echo off
setlocal

:: Define paths
set "scriptDir=%~dp0"
set "scriptPath=%scriptDir%\FLStudioRPC.bat"
set "fl64Path=%scriptDir%FL64.exe"
set "flstudioRPCPath=%scriptDir%assets\FLStudioRPC.exe"
set "iconPath=%scriptDir%assets\icon.ico"
set "shortcutName=FL Studio RPC"
set "shortcutPath=%USERPROFILE%\Desktop\%shortcutName%.lnk"

:: Open FL64.exe
start "" "%fl64Path%"

:: Wait for 3 seconds
timeout /t 3 /nobreak >nul

:: Open FLStudioRPC.exe
start "" "%flstudioRPCPath%"

:: Create shortcut if it doesn't exist
if not exist "%shortcutPath%" (
    powershell "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%shortcutPath%'); $s.TargetPath = '%scriptPath%'; $s.IconLocation = '%iconPath%, 0'; $s.Save()"
)

endlocal

@echo off
adb devices
set IP="1"

for /f "tokens=3 delims=: " %%i  in ('netsh interface ip show config name^="Wi-Fi" ^| findstr "IP Address" ^| findstr [0-9]') do set IP=%%i

adb -s emulator-5560 shell settings put global http_proxy %IP%:8080
adb -s emulator-5560 shell settings put global https_proxy %IP%:8080
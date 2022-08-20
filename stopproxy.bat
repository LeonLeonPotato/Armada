@echo off
adb devices
adb -s emulator-5560 shell settings put global http_proxy :0
adb -s emulator-5560 shell settings put global https_proxy :0
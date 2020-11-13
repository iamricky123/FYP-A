@echo OFF
setlocal
call "%~dp0..\system\setenv.bat"

@"ruby.exe" "%ENV_WEBUI_BIN%"\rackup "%ENV_WEBUI_ROOT%/config.ru" %*

endlocal

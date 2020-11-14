@echo OFF
setlocal
call "%~dp0..\system\setenv.bat"

@"ruby.exe" "%ENV_WEBUI_BIN%"\%~n0 %*

endlocal

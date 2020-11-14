@echo OFF
setlocal
call "%~dp0..\system\setenv.bat"

@"ruby.exe" "%ENV_WEBUI_BIN%"\rake -f "%ENV_WEBUI_ROOT%/Rakefile" %*

endlocal

@echo OFF
setlocal
call "%~dp0..\system\setenv.bat"

set prompt=%username%@%computername%:$p [arachni-shell]$$ 
cmd.exe %*

endlocal

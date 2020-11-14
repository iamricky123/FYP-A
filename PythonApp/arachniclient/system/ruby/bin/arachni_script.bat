@ECHO OFF
IF NOT "%~f0" == "~f0" GOTO :WinNT
@"C:\builds\arachni\system\ruby\bin\ruby.exe" "C:/builds/arachni/system/ruby/bin/arachni_script" %1 %2 %3 %4 %5 %6 %7 %8 %9
GOTO :EOF
:WinNT
@"C:\builds\arachni\system\ruby\bin\ruby.exe" "%~dpn0" %*

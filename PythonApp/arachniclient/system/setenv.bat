@echo OFF

set ENV_ROOT=%~dp0
set ENV_RUBY_BIN=%ENV_ROOT%ruby\bin
set ENV_WEBUI_ROOT=%ENV_ROOT%arachni-ui-web
set ENV_WEBUI_BIN=%ENV_WEBUI_ROOT%\bin

:: Arachni packages run the system in production.
set RAILS_ENV=production

set ARACHNI_FRAMEWORK_LOGDIR=%ENV_ROOT%\logs\framework
set ARACHNI_WEBUI_LOGDIR=%ENV_ROOT%\logs\webui

:: PhantomJS cache needs to be per package to prevent conflicts.
set USERPROFILE=%ENV_ROOT%home

For /F "Delims=" %%I In ('echo "%PATH%" ^| find /C /I "%ENV_RUBY_BIN%"') Do set pathExists=%%I 2>Nul
If %pathExists%==0 set PATH=%ENV_RUBY_BIN%;%PATH%

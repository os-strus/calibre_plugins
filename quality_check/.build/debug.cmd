@echo off
call build.cmd

set CALIBRE_DEVELOP_FROM=
set CALIBRE_OVERRIDE_LANG=

echo Starting calibre in debug mode
"C:\Program Files\Calibre2\calibre-debug" -g
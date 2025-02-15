@echo off
set CALIBRE_DIRECTORY=C:\Program Files\Calibre2

cd ..
if exist "translations" (
    cd translations
    set PYTHONIOENCODING=UTF-8
    for %%f in (*.po) do (
        echo Compiling translation for: %%~nf
        if defined CALIBRE_DIRECTORY (
            "%CALIBRE_DIRECTORY%\calibre-debug.exe" -c "from calibre.translations.msgfmt import main; main()" %%~nf
        ) else (
            calibre-debug.exe -c "from calibre.translations.msgfmt import main; main()" %%~nf
        )
    )
    cd ..
) else (
    echo No translations subfolder found
)

echo Copying common files for zip
xcopy ..\common\common_*.py . /Y > nul

C:\tls\Python313\python ..\common\build.py
if %ERRORLEVEL% neq 0 goto :ExitPoint

echo Deleting common files after zip
del common_*.py

rem Determine the zip file that just got created
for /F "delims=" %%I in ('DIR "*.zip" /A-D /B /O:D') do set "PLUGIN_ZIP=%%I"

echo Installing plugin "%PLUGIN_ZIP%" into calibre...
if defined CALIBRE_DIRECTORY (
    "%CALIBRE_DIRECTORY%\calibre-customize" -a "%PLUGIN_ZIP%"
) else (
    calibre-customize -a "%PLUGIN_ZIP%"
)
echo Build completed successfully

:ExitPoint
cd .build

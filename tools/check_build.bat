@echo off
setlocal
cd /d "%~dp0.."
echo [Yetrealm Wiki] Installing dependencies...
python -m pip install -r requirements.txt
if errorlevel 1 goto fail
echo [Yetrealm Wiki] Building with mkdocs build --strict...
python -m mkdocs build --strict
if errorlevel 1 goto fail
echo.
echo Build passed. The wiki project is valid.
pause
exit /b 0
:fail
echo.
echo Build failed. Read the error messages above.
pause
exit /b 1

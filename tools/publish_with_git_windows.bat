@echo off
setlocal
set REPO_URL=https://github.com/Alixn-mc/Yetrealm-Wiki.git
set TARGET=%USERPROFILE%\Desktop\Yetrealm-Wiki

echo This script requires Git in PATH.
echo It will clone the wiki repo to:
echo %TARGET%
echo.
pause

if exist "%TARGET%\.git" (
  echo Existing Git repo found. Pulling latest changes...
  cd /d "%TARGET%"
  git pull origin main
) else (
  git clone %REPO_URL% "%TARGET%"
)

if errorlevel 1 goto fail

echo Copying wiki project files...
robocopy "%~dp0.." "%TARGET%" /MIR /XD ".git" "site" /XF "yetrealm_wiki_mkdocs_material.zip"
if %ERRORLEVEL% GEQ 8 goto fail

cd /d "%TARGET%"
git add .
git commit -m "Initial official Yetrealm Wiki"
git push origin main
if errorlevel 1 goto fail

echo.
echo Push completed. Now open GitHub Settings ^> Pages and choose GitHub Actions.
pause
exit /b 0

:fail
echo.
echo Something failed. GitHub Desktop is usually easier if this script fails.
pause
exit /b 1

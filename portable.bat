@echo off
if not exist releases mkdir releases
set /p VERSION=<latest.txt
del /q portable
md portable

portable.py

cd portable
if not exist espeak cp -r ..\espeak espeak
copy ..\latest.txt Version.halconfig
rm -rf plugins
cp -r ..\plugins .
cp -r ..\data\spam data

7za a HAL_PE_%VERSION%.7z *
del ..\releases\HAL_PE_%VERSION%.7z
move HAL_PE_%VERSION%.7z ..\releases
echo Done

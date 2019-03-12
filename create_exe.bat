@echo off
endlocal


set "curPath=%CD%"
mkdir tmp

echo.
echo  - Copying files...
copy checkLib.py tmp\
copy icon.ico tmp\ 
copy interactGUI.py tmp\
copy main.py tmp\ 
copy mainUI.py tmp\ 
copy myClass.py tmp\ 
copy myConstants.py tmp\ 
copy myFunctions.py tmp\
copy Version.txt tmp\

rem change the directory to tmp. We will create our exe here
cd tmp\
set /p buildName=<Version.txt

set "filename=PTA_%buildName%_NT"
echo.
echo  - MAKING EXE %filename% ...

rem run py installer
pyinstaller --clean --icon icon.ico --onefile --name %filename% -w main.py

rem copy the exe file back to original folder
echo.
echo - copying %filename%.exe...
copy dist\%filename%.exe ..\

rem remove the tmp directory
echo.
echo - Removing directory tmp...
cd..
rd /s/q tmp

echo - *********** The exe %filename%.exe is ready in %curPath%!!
endlocal
pause

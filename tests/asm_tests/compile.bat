@echo off

if "%1" == "" (
    echo ?: error: path not gived
    echo    compile.bat [asm-file] [output]
    echo:
    exit /b
)

if not exist %1 (
    echo %1: error: path does not exists
    echo:
    exit /b
)

:: create temporal folder
if not exist tmp (
    mkdir tmp
)

:: compile asm file to object
nasm -fwin32 %1 -o tmp/%1.obj

:: enter in workspace
cd tmp

:: compile object to exe
gcc %1.obj -o %1.exe

:: execute program
%1.exe

:: return to the original position
cd ..

:: remove temporal folder
@RD /S /Q tmp

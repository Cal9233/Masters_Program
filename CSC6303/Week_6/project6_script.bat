@echo off
setlocal enabledelayedexpansion

REM Author: Calvin Malagon
REM Script: CalvinMalagonProject6 Creator
REM Description: Creates a folder on desktop and generates a text file with even numbers 1-50

REM Create the project folder on desktop
set FOLDER_NAME=CalvinMalagonProject6
mkdir "%FOLDER_NAME%"

REM Check if folder was created successfully
if not exist "%FOLDER_NAME%" (
    echo Error: Could not create folder %FOLDER_NAME%
    pause
    exit /b 1
)

echo Folder "%FOLDER_NAME%" created successfully.

REM Create the text file with even numbers from 1 to 50
set OUTPUT_FILE=%FOLDER_NAME%\even_numbers.txt

REM Clear the file if it exists, or create a new one
echo Writing even numbers from 1 to 50... > "%OUTPUT_FILE%"

REM Enable delayed variable expansion for the loop
setlocal enabledelayedexpansion

REM Loop through numbers 1 to 50 and write even numbers to file
for /L %%i in (1,1,50) do (
    set /a remainder=%%i%%2
    if !remainder! == 0 (
        echo %%i >> "%OUTPUT_FILE%"
    )
)

echo Even numbers have been written to "%OUTPUT_FILE%"
echo.
echo Script completed successfully!
echo Press any key to exit...
pause > nul
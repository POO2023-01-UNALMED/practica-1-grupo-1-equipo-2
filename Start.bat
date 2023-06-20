@echo off
if exist "%USERPROFILE%\Documents\GitHub\practica-1-grupo-1-equipo-2\src_py\main.py" (
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" "%USERPROFILE%\Documents\GitHub\practica-1-grupo-1-equipo-2\src_py\main.py"
) else if exist "%USERPROFILE%\Downloads\main.py" (
    "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" "%USERPROFILE%\Downloads\main.py"
) else (
    echo No se encontró el archivo main.py
)
pause
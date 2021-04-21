set CURRENT_DIR=%~dp0
set OUTPUT_PATH=%CURRENT_DIR%..\..\
set BASIC_MODULE_PATH=%CURRENT_DIR%..\..\PythonBasicModule
set PYTHON_NAME=GenerateClientProto
rd /s /q build
rd /s /q dist
del /s /q /f %PYTHON_NAME%.spec
del /s /q /f %OUTPUT_PATH%%PYTHON_NAME%.exe
pyinstaller.exe -F -p %BASIC_MODULE_PATH% %PYTHON_NAME%.py
xcopy dist\%PYTHON_NAME%.exe %OUTPUT_PATH% /c/q/e
rd /s /q build
pause
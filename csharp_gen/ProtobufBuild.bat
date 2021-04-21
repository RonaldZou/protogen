@echo off
echo /********************************************************************
echo  Start %0
echo ********************************************************************/

set CurrentDir=%~dp0
set BUILD_EXE=%CurrentDir%GenerateClientProto.exe
set PROTO_PATH=%CurrentDir%protos
set OUTPUT_PATH=%CurrentDir%output
set TOOL_PATH=%CurrentDir%

%BUILD_EXE% %PROTO_PATH% %OUTPUT_PATH% %TOOL_PATH%

:succeed
echo /********************************************************************
echo  %~n0%~x0 Succeed
echo ********************************************************************/
pause
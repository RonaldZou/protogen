@echo on
chcp 65001
cd client_lua
call build.bat protos
XCOPY file\MsgId.lua ..\output /s /f /e /y
XCOPY file\msg.pb ..\output /s /f /e /y
pause
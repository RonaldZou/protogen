echo off
setlocal enabledelayedexpansion
chcp 65001

SET IN = "%1"

echo syntax = "proto3"; > protobuf\msg.proto
echo import "options.proto"; >> protobuf\msg.proto
for %%i in (%1\*.proto) do (
	@type %%i >> protobuf\msg.proto
	@echo. >> protobuf\msg.proto
)

cd protobuf
protoc --descriptor_set_out=options.protobin --include_imports options.proto
java -jar createMsgId.jar msg.proto union.proto ../file/
MsgTableGen.exe
protoc --descriptor_set_out=../file/msg.pb --include_imports msg.proto

XCOPY ..\file\msg.pb ..\file\msg_preEnc.pb /f /y

"aes.exe" ..\file/msg.pb aesEncodeMessage

echo backup msg_preEnc finish, msg encrypt finish

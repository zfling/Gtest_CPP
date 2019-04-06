@echo off
echo -----------------------------------------------------------------------------------------------------------
SETX CygWin_DIR C:\software\developer\cygwin64\bin\
SETX Linux_ADDR 192.168.3.70
SETX Rsync_ADDR zfling@192.168.3.70::zfl_gtest
SETX SSH_ADDR zfl@192.168.3.70
SETX Linux_Dir /home/zfl/code/gtest/proj
echo ---Restart Visual Studio Code---
@echo on

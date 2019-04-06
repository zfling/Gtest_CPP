@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Clear Build Directory---
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; make clean"
@echo on

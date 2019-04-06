@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Generate Makefile---
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./scripts/newMakefile.py"
@echo on

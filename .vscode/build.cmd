@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Build Executable Program---
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./scripts/newMakefile.py ; make"
@echo on

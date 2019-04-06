@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---rsync code and build program---
%CygWin_DIR%rsync -azvP ./ --include-from=./.vscode/include.txt --exclude-from=./.vscode/exclude.txt --exclude '/*' --password-file=./.vscode/password %Rsync_ADDR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Build Executable Program---
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./scripts/newMakefile.py ; make"
@echo on

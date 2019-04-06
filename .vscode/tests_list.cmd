@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Case Lists---
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./build/run_tests --gtest_list_tests > ./build/CasesList.txt"
echo -----------------------------------------------------------------------------------------------------------
echo ---Rsync CasesList.txt---
%CygWin_DIR%rsync -azvP --password-file=./.vscode/password %Rsync_ADDR%/build/CasesList.txt ./.vscode/
@echo on

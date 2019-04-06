@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---rsync code---
%CygWin_DIR%rsync -azvP ./ --include-from=./.vscode/include.txt --exclude-from=./.vscode/exclude.txt --exclude '/*' --password-file=./.vscode/password %Rsync_ADDR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Build Executable Program and Run execution file---
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./scripts/newMakefile.py ; make; ./build/run_tests --gtest_filter=* --gtest_color=yes --gtest_print_time=yes"
@echo on

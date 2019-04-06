@echo off
echo -----------------------------------------------------------------------------------------------------------
echo ---rsync code---
@echo on
%CygWin_DIR%rsync -azvP --delete ./ --include-from=./.vscode/include.txt --exclude-from=./.vscode/exclude.txt --exclude '/*' --password-file=./.vscode/password %Rsync_ADDR%
::%CygWin_DIR%rsync -azvP ./ --password-file=./.vscode/password %Rsync_ADDR%


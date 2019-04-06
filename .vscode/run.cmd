@echo off
::echo ---CygWin Directory Show---
::echo %CygWin_DIR%
echo -----------------------------------------------------------------------------------------------------------
echo ---Execute Program---
::%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./build/run_tests --gtest_filter=* --gtest_color=yes --gtest_print_time=yes"
%CygWin_DIR%ssh %SSH_ADDR% "cd %Linux_Dir% ; ./build/run_tests --gtest_filter=ContainerLibTest.* --gtest_color=yes --gtest_print_time=yes"
echo -----------------------------------------------------------------------------------------------------------
@echo on


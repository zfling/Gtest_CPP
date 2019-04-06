#!/usr/local/python37/bin/python3
# -*- coding: utf-8 -*

import os
import time

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return dirs


def template_deal(xxx_list, sub_len, xxx_flag, sub_dirs):
    #print(xxx_list)
    #print(len(xxx_list))
    for loop in range(0, sub_len):
        #print("loop : %d" % loop)  # 增加源文件对应的路径信息
        for addLine in xxx_list:
            tmpLine = addLine.replace("xxx", sub_dirs[loop])
            tmpLine = tmpLine.replace("XXX", sub_dirs[loop].upper())
            f_write.write(tmpLine)
    return xxx_flag + 1


def all_deal(sall, sline, sub_len, sub_dirs, fwrite):
    if sall in sline:
        f_write.write(sline)
        tmp = ""
        for loop in range(0, sub_len):
            if loop == 0:
                tmp = sall.split()[1] + " = $(" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ") \\\n"
                if "INC_DIR" in sall:
                    tmp = sall.split()[1] + " = -I$(" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ") \\\n"
                f_write.write(tmp)
                tmp = "\t\t$(TEST_" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ")"
                if "INC_DIR" in sall:
                    tmp = "\t\t-I$(TEST_" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ")"
                if loop < (sub_len - 1):
                    tmp = tmp + " \\\n"
                else:
                    tmp = tmp + "\n"
                f_write.write(tmp)
                continue
            tmp = "\t\t$(" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ") \\\n"
            if "INC_DIR" in sall:
                tmp = "\t\t-I$(" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ") \\\n"
            f_write.write(tmp)
            tmp = "\t\t$(TEST_" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ")"
            if "INC_DIR" in sall:
                tmp = "\t\t-I$(TEST_" + sub_dirs[loop].upper() + "_" + sall.split()[1] + ")"
            if loop < (sub_len - 1):
                tmp = tmp + " \\\n"
            else:
                tmp = tmp + "\n"
            f_write.write(tmp)


if __name__ == '__main__':
    print("+++Current Work Directory:" + os.getcwd() +"+++")
    sub_dirs = file_name('./app/src')
    print(sub_dirs)
    sub_len = len(sub_dirs)
    f_read = open('./scripts/templet', 'r')
    f_write = open('./Makefile', 'w', encoding='utf-8')
    xxx_flag = 0
    xxx_list = []
    for line in f_read:
        # print("---" + line + "---")
        if "# Date" in line:
            tmp = "# Date   : " + time.strftime("%Y-%m-%d") +"\n"
            f_write.write(tmp)
            continue
        if "XXX begin" in line:
            xxx_flag = 1
            continue  # 路径等重要信息保存开始阶段
        if "XXX end" in line:
            xxx_flag = 2
        if xxx_flag == 1:
            xxx_list.append(line)
            continue  # 把路径等重要信息模板添加到list中，随后使用
        if xxx_flag == 2:
            xxx_flag = template_deal(xxx_list, sub_len, xxx_flag, sub_dirs)
            continue  # 路径等重要信息处理完成
        # 处理ALL类相关文本
        if "ALL SRC_BUILD" in line:
            all_deal("ALL SRC_BUILD", line, sub_len, sub_dirs, f_write)
            continue
        if "ALL SRC_OBJS" in line:
            all_deal("ALL SRC_OBJS", line, sub_len, sub_dirs, f_write)
            continue
        if "ALL INC_DIR" in line:
            all_deal("ALL INC_DIR", line, sub_len, sub_dirs, f_write)
            continue
        if "ALL INC_HEADERS" in line:
            all_deal("ALL INC_HEADERS", line, sub_len, sub_dirs, f_write)
            continue
        if "XXX OBJ begin" in line:
            xxx_flag = 4
            xxx_list = []
            continue
        if "XXX OBJ end" in line:
            xxx_flag = 5
        if xxx_flag == 4:
            xxx_list.append(line)
            continue
        if xxx_flag == 5:
            xxx_flag = template_deal(xxx_list, sub_len, xxx_flag, sub_dirs)
            continue  # 路径等重要信息处理完成
        f_write.write(line)
    f_read.close()
    f_write.close()
    print("Close Files")

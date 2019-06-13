#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
__auther__ = "JE2Se"

new_list = []
def xiaoxiaole() :
    file = "oldDict.txt"
    with open(file, "r", encoding="utf-8") as f:
        file_2 = f.readlines()
        for file in file_2 :
            new_list.append(file)
            file1 = set(new_list)    #使用set()过滤掉重复元素
        end_file = list(file1)
        for out in end_file :
            with open("newDict.txt","a+",encoding="utf-8") as f:   
                f.write(out)
                print(out)

if __name__ =="__main__":
    xiaoxiaole()
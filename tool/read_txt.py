# -*- coding: utf-8 -*- 
# @Time : 2021/3/8 14:43 
# @Author : WSL
# @File : read_txt.py

def read_txt(filename):
    filepath = "./data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        # print(f.readlines())
        return f.readlines()

if __name__ == '__main__':
    # read_txt("login.txt")
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))

    print(arrs[1:])

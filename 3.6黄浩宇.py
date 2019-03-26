#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  :2019/3/6 16:51
# @Author:Liu Guoyang
# @File  :day8_work.py

# info = {
#     '001': {'姓名': None, '年龄': None, '电话号码': None, '地址': None},
#     '002': None,
#     '003': None
# }


def gainKey(gain_serial, dict5):
    """获取成员信息的key"""
    key = tuple(dict5[gain_serial])
    return key  # ('姓名', '年龄', '电话号码', '地址')


def isExist(serial1, dict1):
    """判断成员是否已经存在"""
    for x in dict1:
        if serial1 == x:
            # print("成员已存在")
            return x
        else:
            pass
            # print("成员不存在")


def choiceMenu():
    """菜单选择"""
    print("*" * 30)
    print("1、添加成员信息")
    print("2、根据编号查看成员信息")
    print("3、修改成员信息")
    print("4、删除成员信息")
    print("5、查看所有成员信息")
    print("0、退出")
    print("*" * 30)

    choice_menu = int(input("请选择操作："))

    return choice_menu


def addMember(dict_add):
    """添加成员信息"""
    serial_input = input("请输入新成员编号：")
    judge_result = isExist(serial_input, dict_add)  # 判断是否存在

    if judge_result is None:

        name_input = input("请输入新增成员姓名：")
        age_input = int(input("请输入新增成员年龄："))
        tel_input = int(input("请输入新增成员电话号码："))
        address_input = input("请输入新增成员地址：")

        info = {'姓名': name_input, '年龄': age_input, '电话号码': tel_input, '地址': address_input}
        dict_add[serial_input] = info

        print(member_info[serial_input])
    else:
        print("已经存在{}编号的成员，添加失败！".format(serial_input))


def showUseSerial(dict2):
    """根据编号查询成员信息"""
    serial2 = input("输入你要查询的成员的编号：")
    judge_result2 = isExist(serial2, dict2)

    if judge_result2 is not None:
        print(dict2[serial2], "\n查询成功！！！")
    else:
        print("不存在{}编号的成员，信息查询失败！".format(serial2))


def modifyMember(dict3):
    """修改成员信息"""
    modify_serial = input("请输入你要修改的成员编号：")
    judge_result3 = isExist(modify_serial, dict3)

    if judge_result3 is not None:  # 如果成员不存在
        while True:

            print("*" * 15)
            print("1、修改电话")
            print("2、修改地址")
            print("3、查看修改")
            print("0、返回上一层")
            print("*" * 15)

            modify_choice = int(input("请输入需要修改的项目："))
            key = gainKey(modify_serial, dict3)  # 获取一个成员的key

            if 0 < modify_choice < 3:

                modify = input("请输入新{}：".format(key[modify_choice+1]))
                dict3[modify_serial][key[modify_choice+1]] = modify

                print("修改成功！！！")

            elif modify_choice == 3:
                print(dict3[modify_serial])

            elif modify_choice == 0:  # 返回上一层
                break

    else:
        print("不存在{}编号的成员，信息修改失败！".format(modify_serial))


def delMember(dict4):
    """删除成员信息"""
    del_serial = input("请输入将要删除的成员编号:")
    judge_result4 = isExist(del_serial, member_info)

    if judge_result4 is None:
        print("不存在{}编号的成员，成员删除失败！".format(del_serial))
    else:
        del dict4[del_serial]
        print("删除成功！！！")


def showAllMember(dict6):
    """遍历查看所有成员信息"""
    for y in dict6:
        print("共{}条成员信息，如下：\n编号为{}的成员信息为：".format(len(dict6), y), dict6[y])


if __name__ == '__main__':

    member_info = {}

    while True:
        choice = choiceMenu()

        if choice == 1:
            addMember(member_info)  # 添加成员信息

        if choice == 2:
            showUseSerial(member_info)  # 查看特定成员信息

        if choice == 3:
            modifyMember(member_info)  # 修改成员信息

        if choice == 4:
            delMember(member_info)  # 删除成员信息

        if choice == 5:
            showAllMember(member_info)  # 显示所有成员信息

        if choice == 0:
            break

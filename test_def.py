all_info = []


def cxbg():
    print("*" * 50)
    print("操作说明：")
    print("创建名单--1")
    print("显示/修改名单--2")
    print("查询名单--3")
    print("退出系统--0")
    print("*" * 50)


def create_list():
    create_dic = {}
    create_name = input("请输入姓名(按“0”取消创建)：")
    if (create_name == "0"):
        return
    create_sex = input("请输入性别(按“0”取消创建)：")
    if (create_sex == "0"):
        return
    create_age = input("请输入年龄(按“0”取消创建)：")
    if (create_age == "0"):
        return
    create_phone = input("请输入电话(按“0”取消创建)：")
    if (create_phone == "0"):
        return
    create_dic['姓名']=create_name
    create_dic['性别'] = create_sex
    create_dic['年龄'] = create_age
    create_dic['电话'] = create_phone
    all_info.append(create_dic)


def show_info():
    print("1-----查询")
    print("2-----修改")
    show_act = input("请输入操作代码：")
    for i in show_act:
        if  (i == "1" and len(all_info) != 0) :
            print("姓名\t\t性别\t\t年龄\t\t电话")
            print("=" * 50)
            for dic_info1 in all_info:
                print("%s\t\t%s\t\t%s\t\t%s" % (dic_info1['姓名'],
                                                   dic_info1['性别'],
                                                   dic_info1['年龄'],
                                                   dic_info1['电话']))
            print("=" * 50)
        elif (i == "2" and len(all_info) != 0):
            name = input("需要修改的名字：")
            for dic_info2 in all_info:
                if  (name == dic_info2['姓名']):
                    dic_info2['姓名'] = input("新名字：")
                    dic_info2['性别'] = input("新性别：")
                    dic_info2['年龄'] = input("新年龄：")
                    dic_info2['电话'] = input("新电话：")
                    break
                else :
                    print("无此人信息")
        elif (len(all_info) == 0):
            print("无信息")


def serach_info():
    serach_name = input("输入需要查询的姓名：")
    for name in all_info:
        if  (name['姓名'] == serach_name):
            print("%s\t\t%s\t\t%s\t\t%s" % (name['姓名'],
                                            name['性别'],
                                            name['年龄'],
                                            name['电话']))
            break
        print("无该人信息")

import test_def
while 1:
    test_def.cxbg()
    order_str = input("请输入指令：")

    if  (order_str == "1") :
        # TODO 添加名单
        test_def.create_list()
    elif (order_str == "2"):
        #TODO 显示/修改名单
        test_def.show_info()
    elif (order_str == "3"):
        #TODO 查询名单
        test_def.serach_info()
    elif (order_str == "0"):
        print("已退出系统")
        break
    else:
        print("输入有误，重新输入：")
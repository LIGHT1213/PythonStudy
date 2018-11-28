Tempin=input("请输入一个带符号的数组")
if Tempin[0:-1] in ['1','2','3','4','5','6','7','8','9','0']:
    if Tempin[-1] in ['f','F']:
        C=(eval(Tempin[:-1])-32)/1.8
        print("转化后的温度为{:.2f}C".format(C))
    elif Tempin[-1] in ['c','C']:
        F=1.8*eval(Tempin[:-1])+32
        print("转化后的温度为{:.2f}F".format(F))
    else:
        print("输入格式错误")
else:
    print("输入格式错误")
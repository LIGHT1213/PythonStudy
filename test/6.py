def cul():
    num1=input("请输入第一个整数")
    num2=input("请输入第二个整数")
    num1=int(num1)
    num2=int(num2)
    t1=num1
    t2=num2
    if num1>=num2:
        while num1>0:
            if num2%num1==0 and t1%num1==0:
                return num1
            else:
                num1=num1-1
    else:
         while num2>0 and t2 %num2==0:
            if num1%num2==0:
                return num2
            else:
                num2=num2-1
    return
print(cul())
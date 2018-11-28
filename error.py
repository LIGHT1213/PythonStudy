t=1
while t==1:    
    try:
        x=int(input('x='))
        y=int(input('y='))
        print('x+y=',x+y)
    except:
        print('输入内容必须为整数')
    else:
        t=0

'''
try:
    2/0   #引发除0异常
except:
    print('出错了')

x=[1,2,3]
try:
    print(x[3])   #引发下标超出范围异常
except:
    print('出错了')



def dosome():    #定义函数
    try:
        print(5/0)    #引发除0异常
    except:
        print("出错了")     #发生异常时执行
    finally:
        print("finally部分已经执行")    #不管异常都会执行
    print('over')    #正常执行

dosome()



# 异常类名
raise IndexError

#异常类实例
x=IndexError()
raise x



x=0
assert x!=0,'变量x的值不能为0'

'''
try:
    import math
    x=-5
    assert x>=0,'参数x必须为非负数'
except Exception as ex:
    print('异常类型:',ex.__class__.__name__)
    print('异常信息：',ex)


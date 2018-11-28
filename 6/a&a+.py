f = open('1.txt', 'a+') #打开文件,返回一个文件对象

content = input("请输入写入的内容：")

f.write (content)

str=f.read()

f.close()                    #关闭文件

print(str)

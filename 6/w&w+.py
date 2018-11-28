f = open('1.txt', 'w+') #打开文件,返回一个文件对象

content = input("请输入写入的内容：")

str=f.read()

f.write (content)

#f.write (content)


f.close()                    #关闭文件

print(str)

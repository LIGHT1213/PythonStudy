'''
f = open("1.txt",'r+')  #打开文件,返回一个文件对象

str = f.read()             # 调用文件的 read()方法方法读取文件内容
f.write ('  python 100')

f.close()                    #关闭文件

print(str);



'''
f = open('1.txt', 'r+')             #打开文件,返回一个文件对象
content = input("请输入写入的内容：")
f.seek(3)
f.write (content)

f.close()                    #关闭文件



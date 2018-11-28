f = open("C:\\Users\\pan39\\Desktop\\工具\\python3\\6\\test.txt")             #打开文件,返回一个文件对象
list= f.readlines()             # 调用文件的 readlines()方法方法读取文件内容
f.close()                    #关闭文件
print(list)

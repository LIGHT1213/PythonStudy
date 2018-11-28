f = open("test.txt")             #打开文件,返回一个文件对象
str = f.read()             # 调用文件的 read()方法方法读取文件内容
f.close()                    #关闭文件
print(str);

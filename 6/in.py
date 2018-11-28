f = open("test.txt")             #打开文件,返回一个文件对象
for line in f:
    print(line)                   #打印line
f.close()                    #关闭文件

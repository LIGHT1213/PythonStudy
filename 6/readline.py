f = open("test.txt")             #打开文件,返回一个文件对象
while True:                        #循环读取
    chunk = f.readline()            #每次读取一行
    if not chunk:                  #如果没有读取到内容，则退出循环
        break
    print(chunk)                   #打印chunk
f.close()                    #关闭文件

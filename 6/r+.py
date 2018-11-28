f = open('1.txt', 'r+')             #打开文件,返回一个文件对象
content = input("请输入写入的内容：")
f.seek(3)
f.write (content)
f.close()                    #关闭文件

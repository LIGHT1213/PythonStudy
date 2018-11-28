myfile=open('2.txt','wb')  # 以wb方式打开二进制文件
myfile.write('aaaaa')     # 出错，二进制文件只能写入byte字符串
myfile.write(b'eeee')     #正确，以bytes字符串写入文件
myfile.write(b'ffff')
myfile.write(b'ggggg')
myfile.close()
myfile=open('2.txt','r')   #以r方式打开，作为文本文件访问
print(myfile.read())

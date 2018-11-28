#一行
#方法一：

f = open("G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data1.txt")

a=f.read()

a
#'34 78 47 787 84 25 69 25 58 67 52 77 12 67 325 33'

L1=a.split()

#方法二：

f.seek(0)

a=f.readline()

a
#'34 78 47 787 84 25 69 25 58 67 52 77 12 67 325 33‘

L1=a.split()
#方法三：
f.seek(0)

a=f.readlines()
a

#['34 78 47 787 84 25 69 25 58 67 52 77 12 67 325 33']
L1=a[0].split()
f.close()

#转化为整数数据
for i in range(0,len(L1)):

L1[i]=int(L1[i])

L1




# 一列
f = open("G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data2.txt")

a=f.read()

a

#'34\n78\n47\n787\n84\n25\n69\n25\n58\n67\n52\n77\n12\n67\n325\n33'

L2=a.splitlines()
L2
#['34', '78', '47', '787', '84', '25', '69', '25', '58', '67', '52', '77', '12', '67', '325', '33']

f.seek(0)

L2=f.readlines()

L2

#['34\n', '78\n', '47\n', '787\n', '84\n', '25\n', '69\n', '25\n', '58\n', '67\n', '52\n', '77\n', '12\n', '67\n', '325\n', '33']

f.close()




# 多行多列
f = open("G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data3.txt")
a=f.read()

L3=a.split()

L3
f.close()





#快速列表访问方式
L4=list(open("G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data3.txt"))
L5=[]
L6=[0]*100
for i in L4:
    L5.extend(i.split(', ')
)
for i in range(len(L5)):
    L6[i]=int(L5[i])

L4
L5

#结构数据读取
a=list(open("G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data4.txt"))
L7=[]
for i in a:

    L7.append(i.split())

for i in range(0,len(L7)):

    for j in range(3,len(L7[i])):

        L7[i][j]=int(L7[i][j])



#数值数据输出
L1=[34, 78, 47, 787, 84, 25, 69, 25, 58, 67, 52, 77, 12, 67, 325, 33]

f=open('G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data5.txt','w')

for i in L1:

    f.write(repr(i)+'\n')

f.close()


#结构数据输出
f=open('G:\\教学改革\\Python程序设计与应用开发录音材料\\第六章\\data6.txt','w')
s=''

for a in L7:

    for i in range(0,3):  #连接前3个字符串

        s=s+a[i]+','

    for i in range(3,len(a)-1):  #连接后12个是整数

        s=s+repr(a[i])+','

    s=s+repr(a[len(a)-1])+'\n'  #  连接最后1个整数，回车符结束

f.write(s)

#401
f.close()











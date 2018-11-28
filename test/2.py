s=list(open('C:\\Users\\pan39\\Desktop\\工具\\python3\\test\\grade2.txt'))
Ls=[]
for x in s:
    Ls.append(x.split())
for x in Ls:
    for i in range(1,len(x)):
        if x[i] =='及格':
            x[i]=-1
        elif x[i]=='不及格':
            x[i]=-2
        else:
            x[i]=int(x[i])
Ld=[]
d=dict({1:'优秀',2:'合格',3:'不合格'})

for x in Ls:
    sum=x[1]+x[2]+x[3]
    if x[4]==-2:
        key=3
    else:
        if x[1]>=80 and x[2]>=80 and x[3]>=80 and sum>= 255:
            key=1
        elif x[2]>=60 and x[3]>60 and sum>= 180:
            key=2
        else:
            key=3
    Ld.append([x[0], d[key]])
f=open('C:\\Users\\pan39\\Desktop\\工具\\python3\\test\\result.txt','w')
for x in Ld:
    f.write('%s\t%s\n'%(x[0],x[1]))
f. close()

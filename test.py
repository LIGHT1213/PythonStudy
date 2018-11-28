s=list(open('C:\\1.txt'))
###print(s)
Ls=[]
for x in s:
    Ls.append(x.split())
for x in Ls:
    for i in range(1,len(x)):
        x[i]=int(x[i])
Ld=[]
d=dict({1:"优秀",2:"合格",3:"不合格"})
for x in Ls:
    TTT=x[1]+x[2]+[3]
    if TTT>=180 and x[2]>=60 and x[3]>=60:
        KEY=2
    elif TTT>=255 and x[1]>=80 and x[2]>=80 and x[3]>=80:
        KEY=1
    elif TTT<180 or x[1]>=60 or x[2]>=60 or x[3]>=80:
        KEY=3
    Ld.append([[x[0],d[KEY]])
f=open('C:\\result.txt','w')
for x in Ld:
    f.write('%s\t%s\n'%(x[0],x[1]))
f. close()

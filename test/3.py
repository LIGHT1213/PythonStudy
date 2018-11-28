s=list(open('C:\\Users\\pan39\\Desktop\\工具\\python3\\test\\customer.txt'))
Ls=[]
for x in s:
    Ls.append(x.split())
for x in Ls:
    
    for i in range(1,len(x)):
        x[i]=x[i]
ld=[]
d=dict({1:'男',2:'女'})
for x in Ls:
    z=str(x[1])
    l=int(z[16])
    n=int(z[6:10])
    if l%2==0:
        key=2
    else:
        key=1
    ld.append([x[0],str(2018-n-1),d[key]])
f=open('C:\\Users\\pan39\\Desktop\\工具\\python3\\test\\result.txt','w')
for x in ld:
    f.write('%s\t%s\t%s\n'%(x[0],x[1],x[2]))
f. close()

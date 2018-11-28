s=list(open('C:\\Users\\pan39\\Desktop\\工具\\python3\\score1.txt'))
ls=[]
for x in s:
    ls.append(x.split())
#print(ls)
lt=[]
n59=0
n6070=0
n7080=0
n8090=0
n100=0
zf=0
an=0
for x in ls:
    t1=float(x[1])
    t2=float(x[2])
    he= t1*0.4+t2*0.6
    zf=zf+he
    if he<60:
        n59=n59+1
    elif he>=60 and he<70:
        n6070=n6070+1
    elif he>=70 and he <80:
        n7080=n7080+1
    elif he>=80 and he<90:
        n8090=n8090+1
    elif he>=90:
        n100=n100+1
    st=str(he)
    lt.append([x[0],st])
    an=an+1
#print(lt)
print("班级总人数为",an)
print("班级60以下人数",n59)
print("班级60到70人数",n6070)
print("班级70到80人数",n7080)
print("班级80到90人数",n8090)
print("班级90以上人数",n100)
pp=zf/an
print("班级总评分",pp)
f=open('C:\\Users\\pan39\\Desktop\\工具\\python3\\score2.txt','w')
for x in ls:
    f.write('%s\t%s\n'%(x[0],x[1]))
f. close()

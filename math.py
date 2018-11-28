work=[]
for i in range(365):  #生成一个工作列表
    work.append(1)
day=0.01
dayuk=1
i=1
while i<=365:
    t=dayuk
    for j in range(1,8):
        if i+j>=365  or work[i+j-2]==0:
            dayuk=t
            i=i+j
            break
        elif j in [1,2,3]:
            dayuk=dayuk
        elif j in [4,5,6,7]:
            dayuk=dayuk*(1+day)
    i=i+7
print("up={:.10f}".format(dayuk)) 


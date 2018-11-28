import time
def cut():
    p=dict({1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31})
    r=dict({1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31})
    k=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    wn=int(k[0:4])
    wy=int(k[5:7])
    wr=int(k[8:10])
    z=wr-1
    x=1
    if wn%100==0 and wn%400==0:
        while x<wy:
            z=z+r[x]
            x=x+1
    elif wn%4==0:
        while x<wy:
            z=z+r[x]
            x=x+1
    else :
        while x<wy:
            z=z+p[x]
            x=x+1
    return z
print(cut())

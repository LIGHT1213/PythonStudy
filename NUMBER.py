for i in range(1,10):
    print(" "*(15-i),end="")
    n=i
    while n>=1:
        
        if n==1:
            print(' ',end="")
        elif n==2:
            print(' ',end="")
        else:
            print(n,end="")
        n-=1
    n+=1
        
    while n<i:
        n+=1
        if n==1:
            print(' ',end="")
        elif n==2:
            print(' ',end="")
        else:
            print(n,end="")
    print("\n")
        
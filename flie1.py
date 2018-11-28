try:
    s=list(open('C:\\Users\\pan39\\Desktop\\工具\\python3\\sc1.txt'))
    ls=[]
    for x in s:
        ls.append(x.split())
except FileNotFoundError:
    print("文件未找到")
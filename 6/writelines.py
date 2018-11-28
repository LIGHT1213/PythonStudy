fo = open('1.txt', "w+")
ls = ["python1   ", "python2   ", "python3"]
fo.writelines(ls)
for line in fo:
   print(line)
fo.close()

# pathon普通与numpy的效率对比
#向量相加--python


def pythonsum(n):
#    a=range(n)
#    b=range(n)
    a=[]
    b=[]
    c=[]
    for i in range(n):
        a.append(i**2)
        b.append(i**3)
        c.append(a[i]+b[i])
    return c
 

#向量相加--Numpy
import numpy as np
def numpysum(n):
    a=np.arange(n)**2
    b=np.arange(n)**3
    c=a+b
    return c

#结果比较
import sys
from datetime import datetime
import numpy as np
size=1000
start=datetime.now()
c=pythonsum(size)
delta=datetime.now()-start
print('The last 2 elements of the sum',c[0:3])
print('PythonSum elapsed time in microsecomds ',delta.microseconds)

start=datetime.now()
c=numpysum(size)
delta=datetime.now()-start
print('The last 2 elements of the sum',c[-2:])
print('NumPySum elapsed time in microsecomds ',delta.microseconds)


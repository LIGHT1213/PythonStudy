


import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
arr1

data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)

arr2

arr2.ndim

arr2.shape

arr1.dtype

np.zeros(10)

np.zeros((3,6))

np.empty((2,3,2))

np.arange(15)

arr=np.array([[1.,2.,3.],[4.,5.,6.]])

arr

arr*10

arr*arr

arr-arr

1/arr

arr*0.5
#一维数组的切片与索引
arr=np.arange(10)

arr

arr[5]

arr[5:8]

arr[5:8]=12

arr_slice[1]=12345

arr

arr_slice[:}=64

#多维数组的切片与索引
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])

arr2d[0][2]

arr2d[0,2]

arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

arr3d

arr3d[0]

arr2d[:2]


arr2d[:2,1:]

arr2d[1,:2]

arr2d[2,:1]

arr2d[:,:1]

#数组转置
arr4=np.arange(15).reshape((3,5))

arr4
arr4.T

arr5=np.random.randn(6,3)

np.dot(arr5.T,arr5)

#组合数组
a=np.arange(9).reshape(3,3)

b=2*a

np.hstack((a,b)))

np.concatenate((a,b),axis=1)

np.vstack((a,b))



#数组的分割
a=np.arange(9).reshape(3,3)
np.hsplit(a,3)

#数组的属性
b=np.arange(24).reshape(2,12)

b.ndim

b.size


#数组的转换
b.tolist()

###通用函数
arr = np.arange(10)
np.sqrt(arr)

#数学与统计方法
arr = np.random.randn(5, 4) # 标准正态分布数据
arr
arr.mean()
np.mean(arr)
arr.sum()

arr.mean(axis=1)
arr.sum(0)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr
arr.cumsum(0)
arr.cumprod(1)

      

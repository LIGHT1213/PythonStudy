###利用NumPy进行历史股价分析
import sys
import numpy as np
#读入文件
c,v=np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)

#计算成交量加权平均价格
vwap = np.average(c, weights=v)
print("VWAP =", vwap)

#算术平均值函数
print("mean =", np.mean(c))

#时间加权平均价格
t = np.arange(len(c))
print("twap =", np.average(c, weights=t))

#寻找最大值和最小值
h,l=np.loadtxt('data.csv', delimiter=',', usecols=(4,5), unpack=True)
print("highest =", np.max(h))
print("lowest =", np.min(l))
print((np.max(h) + np.min(l)) /2)

print("Spread high price", np.ptp(h))
print("Spread low price", np.ptp(l))

#统计分析

c=np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print("median =", np.median(c))
sorted = np.msort(c)
print("sorted =", sorted)

N = len(c)
#print("middle =", sorted[(N - 1)/2])
#print("average middle =", (sorted[N /2] + sorted[(N - 1) / 2]) / 2)

print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean())**2))

#股票收益率
c=np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

returns = np.diff( c ) / c[ : -1]
print("Standard deviation =", np.std(returns))

logreturns = np.diff( np.log(c) )

posretindices = np.where(returns > 0)
print("Indices with positive returns", posretindices)

annual_volatility = np.std(logreturns)/np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1./252.)
print("Annual volatility", annual_volatility)

print("Monthly volatility", annual_volatility * np.sqrt(1./12.))


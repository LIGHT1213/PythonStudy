import matplotlib.pyplot as plt


#####matplotlib创建图表
plt.plot([1,2,3,2,3,2,2,1])
plt.show()

plt.plot([4,3,2,1],[1,2,3,4])
plt.show()


#更多简单的图形
x = [1,2,3,4]
y = [5,4,3,2]

plt.figure()

plt.subplot(2,3,1)
plt.plot(x, y)

plt.subplot(232)
plt.bar(x, y)

plt.subplot(233)
plt.barh(x, y)

plt.subplot(234)
plt.bar(x, y)
y1 = [7,8,5,3]
plt.bar(x, y1, bottom=y, color = 'r')

plt.subplot(235)
plt.boxplot(x)

plt.subplot(236)
plt.scatter(x,y)

plt.show()



#####figure与subplot
#figure对象

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.show()

from numpy.random import randn
plt.plot(randn(50).cumsum(), 'k--')
fig.show()

_ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
plt.close('all')

fig, axes = plt.subplots(2, 3)
axes

#颜色、标记和线型
x = [1,2,3,4]
y = [5,4,3,2]


plt.figure()

plt.plot(x,y,linestyle='--',color='g')

#误差条形图
x = np.arange(0, 10, 1)

y = np.log(x)

xe = 0.1 * np.abs(np.random.randn(len(y)))

plt.bar(x, y, yerr=xe, width=0.4, align='center', ecolor='r', color='cyan',
                                                    label='experiment #1');

plt.xlabel('# measurement')
plt.ylabel('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')

plt.show()

#饼图
plt.figure(1, figsize=(8, 8))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

labels = 'Spring', 'Summer', 'Autumn', 'Winter'
values = [15, 16, 16, 28]
explode =[0.1, 0.1, 0.1, 0.1]

plt.pie(values, explode=explode, labels=labels,
    autopct='%1.1f%%', startangle=67)

plt.title('Rainy days by season')

plt.show()



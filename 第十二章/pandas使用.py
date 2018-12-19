import numpy as np
import pandas as pd
import sys
from pandas import Series, DataFrame


###pandas
#Series
obj = Series([4, 7, -5, 3])
obj

arr=np.array([4,7,-5,3])
arr

obj.values
obj.index

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2

obj2.index

obj2['a']

obj2['d'] = 6
obj2[['c', 'a', 'd']]

obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)

#字典
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
obj3

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
obj4

pd.isnull(obj4)
pd.notnull(obj4)

obj4.isnull()

obj3
obj4
obj3 + obj4

obj4.name = 'population'
obj4.index.name = 'state'
obj4


#dataframe
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame

DataFrame(data, columns=['year', 'state', 'pop'])

frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
frame2
frame2.columns

frame2['state']
frame2.year
frame2.ix['three']

frame2['debt'] = 16.5
frame2


frame2['debt'] = np.arange(5.)
frame2

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2

frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2.columns
frame2.values

pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
frame3

#Pandas索引对象
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
index


###数据读取
#读取文本格式数据

df = pd.read_csv('G:data/ex1.csv')
df

pd.read_table('G:data/ex1.csv', sep=',')

pd.read_csv('G:data/ex2.csv', header=None)
pd.read_csv('G:data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])

names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('G:data/ex2.csv', names=names, index_col='message')

parsed = pd.read_csv('G:data/csv_mindex.csv', index_col=['key1', 'key2'])
parsed

list(open('G:data/ex3.txt'))
result = pd.read_table('G:data/ex3.txt', sep='\s+')
result


#JSON数据

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
              {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
#将json格式转化为Python对象
import json
result = json.loads(obj)
result

#将Python对象转化为json格式
asjson = json.dumps(result)  

siblings = DataFrame(result['siblings'], columns=['name', 'age'])
siblings















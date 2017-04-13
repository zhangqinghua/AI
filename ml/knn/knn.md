# kNN_近邻算法·

简单地说，k-近邻算法采用测量不同特征值之间的距离方法进行分类。 
优点：精度高、对异常值不敏感、无数据输入假定。 

缺点：计算复杂度高、空间复杂度高。 适用数据范围：数值型和标称型。 



每部电影的打斗镜头数、接吻镜头数以及电影评估类型

|            电影名称            | 打斗镜头 | 接吻镜头 | 电影类型 |
| :------------------------: | :--: | :--: | :--: |
|       California Man       |  3   | 104  | 爱情片  |
| He’s Not Really into Dudes |  2   | 100  | 爱情片  |
|      Beautiful Woman       |  1   |  81  | 爱情片  |
|      Kevin Longblade       | 101  |  10  | 动作片  |
|      Robo Slayer 3000      |  99  |  5   | 动作片  |
|          Amped II          |  98  |  2   | 动作片  |
|           Unknow           |  18  |  90  |  未知  |

```python
from math import log
def calcShannonEnt(dataSet):
# 计算数据集中实例的总数。
numEntries = len(dataSet)
# 创建一个数据字典，它的键值是最后一列的数值 
# 如果当前键值不存在，则 扩展字典并将当前键值加入字典。每个键值都记录了当前类别出现的次数。
labelCounts = {}
for featVec in dataSet:
	currentLabel = featVec[-1]
	if currentLabel not in labelCounts.keys():
		labelCounts[currentLabel] = 0
	labelCounts[currentLabel] += 1
# 使用所有类标 签的发生频率计算类别出现的概率
shannonEnt = 0.0
for key in labelCounts:
	prob = float(labelCounts[key]) / numEntries
	shannonEnt -= prob * log(prob, 2)
return shannonEnt
```




import numpy as np
import matplotlib.pyplot as plt

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(curLine)
    return np.array(dataMat, dtype=np.float)

# 计算两个向量的欧式距离
def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA - vecB, 2)))

# 为给定数据集构建一个包含k个随机质心的集合
def randCent(dataSet, k):
	# 有多少列数据
    n = np.shape(dataSet)[1]
    # 创建一个k行n列的0矩阵
    centroids = np.mat(np.zeros((k,n)))
    # 以通过找到数据集每一维的最小和最大值来完成。然 后生成0到1.0之间的随机数并通过取值范围和最小值，以便确保随机点在数据的边界之内 
    for j in range(n):
    	# 选取单列最小值 
        minJ = min(dataSet[:,j]) 
        # 单列最大值-最小值
        rangeJ = max(dataSet[:,j]) - minJ
        centroids[:,j] = np.mat(minJ + rangeJ * np.random.rand(k,1))
    return centroids

dataMat = loadDataSet('testSet.txt')

centroids = randCent(dataMat, 4)

plt.plot(dataMat[:, 0], dataMat[:, 1], 'ro')
plt.plot(centroids[:, 0], centroids[:, 1], 'go')
plt.show()



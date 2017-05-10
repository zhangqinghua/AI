from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine) #map all elements to float()
        dataMat.append(curLine)
    return array(dataMat, dtype = float)

# 计算两个向量的欧式距离
def distEclud(vecA, vecB):
	return sqrt(sum(power(vecA - vecB, 2)))

# 为给定数据集构建一个包含k个随机质心的集合
def randCent(dataSet, k):
	# 有多少列数据
    n = shape(dataSet)[1]
    # 创建一个k行n列的0矩阵
    centroids = mat(zeros((k,n)))
    # 以通过找到数据集每一维的最小和最大值来完成。然 后生成0到1.0之间的随机数并通过取值范围和最小值，以便确保随机点在数据的边界之内 
    for j in range(n):
    	# 选取单列最小值 
        minJ = min(dataSet[:,j]) 
        # 单列最大值-最小值
        rangeJ = max(dataSet[:,j]) - minJ
        centroids[:,j] = mat(minJ + rangeJ * random.rand(k,1))
    return centroids

def kMeans(dataSet, k, distMeans = distEclud, createCent = randCent):
    # 有80行
    m = shape(dataSet)[0]
    # 簇分配结果矩阵, 一列记录簇索引值，第二列存储误差。这里的误差是指当前点到簇质心的距离，后边 会使用该误差来评价聚类的效果。
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf # 最近的距离
            minIndex = -1 # 最近的中心点
            # 找出第i个点跟哪个中心点最近
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI;
                    minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            # 标识第i个点所属的中心点
            clusterAssment[i, :] = minIndex, minDist**2
        # 重新计算中心点, 找出每个中心点所对应的点，计算它们的中心点
        for cent in range(k):
            # clusterAssment[:, 0].A 中心点下标
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis = 0)
    return centroids, clusterAssment

dataMat = loadDataSet('testSet.txt')

centroids, clusterAssment =  kMeans(dataMat, 4)

# test = mat(array([[1,2], [3, 4]]))
# print(test[:, 0].A)
# print(test[:, 0].A == 1)
# print(nonzero(test[:, 0].A == 1)[0])

# test = mat(array([[1,2], [3, 4]]))
# print(test)
# print(test[:, 0])
# print(test[:, 0].A)

# print(nonzero(array([0, 1, 2, 3])).A)
# print(array([0, 1, 2, 3]).A)

# centroids = randCent(dataMat, 4)

plt.plot(dataMat[:, 0], dataMat[:, 1], 'ro')
plt.plot(centroids[:, 0], centroids[:, 1], 'go')
plt.show()



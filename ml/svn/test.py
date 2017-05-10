from sklearn import svm
import matplotlib.pyplot as plt


def draw(dataSet, labels):
	x = []
	y = []
	for data in dataSet:
		x.append(data[0]) 
		y.append(data[1]) 

	plt.figure("SVM")
	plt.plot(x, y, 'ro')

	plt.show()

x = [[1, 1.2], [2, 1], [3, 1], [1, 2.8], [2, 3], [3, 3]]
y = ['0', '0', '0', '1', '1', '1']

clf = svm.SVC(kernel = 'linear')

clf.fit(x, y)

print(clf)

# get support vectors
print(clf.support_vectors_)

# get indices of support vectors
print(clf.support_)

print(clf.n_support_)

clf.predict([2, 0])


draw(x, y)
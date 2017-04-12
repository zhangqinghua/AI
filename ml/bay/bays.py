from numpy import ones, log, array

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec

# dataSet ['a', 'b', 'c', 'a', 'c']
# return ['a', 'b', 'c']
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

# 词集模型, 每个词只能出现一次
# vocabList ['a','b','c']
# inputSet ['c','d,'e']
# return [0, 0, 1]
def setOfWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

# 词袋模型，每个单词可以出现 多次
def bagOfWordsVecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

# 计算每个词属于侮辱性词的概率
def trainNB(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    
    # 如果其中一个概率值为0，那么后的乘积也为0。为降低 这种影响，可以将所有词的出现数初始化为1，并将分母初始化为2。 
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0

    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 另一个遇到的问题是下溢出，这是由于太多很小的数相乘造成的。
    # 当计算乘积 p(w0|ci)p(w1|ci)p(w2|ci)...p(wN|ci)时，由于大部分因子都非常小，
    # 所以程序会下溢出或者 得到不正确的答案。（读者可以用Python尝试相乘许多很小的数，后四舍五入后会得到0。）
    # 一 种解决办法是对乘积取自然对数。在代数中有ln(a*b) = ln(a)+ln(b)，于是通过求对数可以 避免下溢出或者浮点数舍入导致的错误。
    # 同时，采用自然对数进行处理不会有任何损失
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom) 
    
    return p0Vect, p1Vect, pAbusive

# 朴素贝叶斯分类函数  
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0 :
        return 1
    return 0
    
    
listOposts, listClasses = loadDataSet()
myVocabList = createVocabList(listOposts)

trainMat = []
for postinDoc in listOposts:
    trainMat.append(bagOfWordsVecMN(myVocabList, postinDoc))

p0V, p1V, pAb = trainNB(trainMat, listClasses)
print(p0V)


testEntry = ['love', 'stupid', 'stupid']
thisDoc = array(bagOfWordsVecMN(myVocabList, testEntry))
print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))


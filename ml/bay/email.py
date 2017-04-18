'''
使用朴素贝叶斯对电子邮件进行分类  

Created on 2017年4月12日

@author: ZhangQinghua
'''
import re
from ml.bay import bayes
from ml.bay.bayes import setOfWord2Vec, trainNB, classifyNB
from numpy import array
import random

# 接受一个大字符串并将其解析为字符串列表。该函数去掉少于两 个字符的字符串，并将所有字符串转换为小写
def textParse(bigString):
    listOfTokens = re.split(r'\W+', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]
 
# 对贝叶斯垃圾邮件分类器进行自动化处理
# 导入文件夹spam与ham 下的文本文件，并将它们解析为词列表 。接下来构建一个测试集与一个训练集，两个集合中的 邮件都是随机选出的。
def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        # 垃圾邮件
        wordList = textParse(open("email/spam/%d.txt" % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        # 普通邮件
        wordlist = textParse(open("email/ham/%d.txt" % i).read())
        docList.append(wordlist)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = bayes.createVocabList(docList)
    
    trainingSet = list(range(50))
    
    # 随机选取10个测试集
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    
    
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWord2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
         
    # 训练数据     
    p0V, p1V, pSpam = trainNB(array(trainMat), array(trainClasses))
    
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWord2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print("The error rate is: ", float(errorCount / len(testSet)))

for i in range(10):
    spamTest()


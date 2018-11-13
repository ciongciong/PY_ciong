from numpy import *   #写成这样就可以不用加numpy.；写成import numpy as ny就要加ny.
import operator
def creatdateset():
    group=array([[1,1],[1,1.1],[0,1]])
    labels=['A','A','B']
    return group,labels

def classify0(inX,dataSet,labels,k):#inX表示要预测的目标向量
    dataSetSize=dataSet.shape[0]    #0行1列，shape[0]表示计算dataSet矩阵有几行，也表示有几组数据
    diffMat=tile(inX,(dataSetSize,1))-dataSet   #做差过的矩阵，用目标向量inX-训练样本集dataSet的矩阵
    sqdiffMat=diffMat**2   #矩阵各元素均平方
    sqDistance=sqdiffMat.sum(axis=1)
    Distances=sqDistance**0.5
    # return Distance   测试发现，Distance可以用
    sortedDistIndicies = Distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),\
                            key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr=open(filename)
    arrayoLines=fr.readlines()
    numberofLines=len(arrayoLines)
    returnMat=zeros((numberofLines,3))#元组
    classLabelVetor=[]
    index=0
    for line in arrayoLines:
        line=line.strip()#清除每行字符串的空格
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVetor.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVetor


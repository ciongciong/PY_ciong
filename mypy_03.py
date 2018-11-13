import kNN
group,lables=kNN.creatdateset()
print(group)
print(lables)
# 测试1，测试距离计算
# Distances=kNN.classify0([0,0],group,lables,1)
# print(Distance)

# 测试2，sortedClassCount=sorted(classCount.items(),
#                                 key=operator.itemgetter(1),reverse=True)
# classCount={'A',1}
# sortedClassCount=sorted(classCount.iteritems(),\
#                  key=operator.itemgetter(1),reverse=True)
# py3.7中dict不能用iteritems，只能items
A=kNN.classify0([0,0],group,lables,1)
print(A)
datingDataMat,datingLabels=kNN.file2matrix('H:\电影\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
print(datingDataMat)
print(datingLabels)

import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)#223将该图片放置在被分为2行2列的画布中的从左到右从上到下的第3块区域
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2],marker='*',color='red')
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
# ax.scatter(marker='o',color='black')
plt.show()


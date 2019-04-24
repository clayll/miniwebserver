import numpy as np

from sklearn import preprocessing
from sklearn import feature_selection
from sklearn import decomposition


num1 = np.random.randint(1,100,(3,4)).astype(np.float)
num2 = np.random.randint(1,30,(3,1)).astype(np.float)


num3 =np.array( [[0, 2, 0, 3],
[0, 1, 4, 3],
[0, 1, 1, 3]])

num4 = np.array([[2,8,4,5],
[6,3,0,8],
[5,4,9,1]])

# 归一化
def guiyi():
    array =preprocessing.MinMaxScaler()
    array1 = array.fit_transform(num1,num2)
    print(array1)
# 标准化
def stander():
    array2 = preprocessing.StandardScaler().fit_transform(num1,num2)
    print(array2)
    var = feature_selection.VarianceThreshold()
    var.fit(num3,num2)
    array3 = var.transform(num3)
    print(array3)

# 降维
def pca():
    pca = decomposition.PCA()
    array4 = pca.fit_transform(num4)
    print(num4)
    print(array4)


if __name__ == '__main__':
    # guiyi()
    # stander()
    # pca()

    print(1.1*1.6)
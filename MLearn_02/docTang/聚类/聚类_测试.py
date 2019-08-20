import numpy as np
import os
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)
from sklearn.datasets import make_blobs

blob_centers = np.array(
    [[0.2,2.3],
     [-1.5,2.3],
     [-2.8,1.8],
     [-2.8,2.8],
     [-2.8,1.3]])

blob_std =np.array([0.4,0.3,0.1,0.1,0.1])


class ClusterTest:
    def __init__(self):
        pass

    def initBlobsData(self):
        blob_centers = np.array(
            [[0.2, 2.3],
             [-1.5, 2.3],
             [-2.8, 1.8],
             [-2.8, 2.8],
             [-2.8, 1.3]])

        blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])
        X, y = make_blobs(n_samples=2000, centers=blob_centers,
                          cluster_std=blob_std, random_state=7)
        return X,y

    def plot_clusters(self,X, y=None):
        plt.scatter(X[:, 0], X[:, 1], c=y, s=1)
        plt.xlabel("$x_1$", fontsize=14)
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
        plt.figure(figsize=(8, 4))
        plt.show()


    def kmeansTest(self):
        X,y = self.initBlobsData()
        self.plot_clusters(X)

if __name__ == '__main__':
    ct = ClusterTest()
    ct.kmeansTest()
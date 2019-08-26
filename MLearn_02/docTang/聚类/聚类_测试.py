import numpy as np
import os
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib.image import imread

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



    def plot_centroids(self,centroids, weights=None, circle_color='w', cross_color='k'):
        if weights is not None:
            centroids = centroids[weights > weights.max() / 10]
        plt.scatter(centroids[:, 0], centroids[:, 1],
                    marker='o', s=30, linewidths=8,
                    color=circle_color, zorder=10, alpha=0.9)
        plt.scatter(centroids[:, 0], centroids[:, 1],
                    marker='x', s=50, linewidths=50,
                    color=cross_color, zorder=11, alpha=1)

    def plot_decision_boundaries(self,clusterer, X, resolution=1000, show_centroids=True,
                                 show_xlabels=True, show_ylabels=True):
        mins = X.min(axis=0) - 0.1
        maxs = X.max(axis=0) + 0.1
        xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                             np.linspace(mins[1], maxs[1], resolution))
        Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        plt.contourf(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                     cmap="Pastel2")
        plt.contour(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                    linewidths=1, colors='k')
        self.plot_data(X)
        if show_centroids:
            self.plot_centroids(clusterer.cluster_centers_)

        if show_xlabels:
            plt.xlabel("$x_1$", fontsize=14)
        else:
            plt.tick_params(labelbottom='off')
        if show_ylabels:
            plt.ylabel("$x_2$", fontsize=14, rotation=0)
        else:
            plt.tick_params(labelleft='off')

    def plot_data(self, X):
        plt.plot(X[:, 0], X[:, 1], 'k.', markersize=2)

    def kmeansTest(self):
        X,y = self.initBlobsData()
        self.plot_clusters(X)
        k = 5
        kmeans = KMeans(n_clusters=k, random_state=42,n_init=10)
        y_pred = kmeans.fit_predict(X)
        plt.figure(figsize=(8, 4))
        self.plot_decision_boundaries(kmeans, X)
        plt.show()

    # 查看不同的迭代次数
    def kmeansShow_iter(self):
        k = 5
        X, y = self.initBlobsData()
        kmeans1 = KMeans(n_clusters=k, random_state=1, n_init=2,max_iter=1,init="random")
        kmeans2 = KMeans(n_clusters=k, random_state=1, n_init=2, max_iter=2,init="random")
        kmeans3 = KMeans(n_clusters=k, random_state=1, n_init=2, max_iter=3,init="random")
        kmeans1.fit(X)
        kmeans2.fit(X)
        kmeans3.fit(X)
        plt.figure(figsize=(12,8))
        plt.subplot(321)
        self.plot_data(X)
        self.plot_centroids(kmeans1.cluster_centers_, circle_color='r', cross_color='k')
        plt.title('Update cluster_centers')

        plt.subplot(322)
        self.plot_decision_boundaries(kmeans1,X)
        plt.title('Lable')

        plt.subplot(323)
        self.plot_data(X)
        self.plot_decision_boundaries(kmeans1, X)
        self.plot_centroids(kmeans2.cluster_centers_, circle_color='r', cross_color='k')
        plt.subplot(324)
        self.plot_decision_boundaries(kmeans2, X)

        plt.subplot(325)
        self.plot_data(X)
        self.plot_decision_boundaries(kmeans2, X)
        self.plot_centroids(kmeans3.cluster_centers_, circle_color='b', cross_color='k')

        plt.subplot(326)

        self.plot_decision_boundaries(kmeans3, X)

        plt.show()

    # 找到最佳簇数,如果k值越大，得到的结果肯定会越来越小！！！，根据到所有各个点的平方和距离 Sum of squared distances of samples to their closest cluster center.

    def clusters_inertia(self):
        k = 5
        X, y = self.initBlobsData()
        preKMeans = [KMeans(n_clusters=k).fit(X) for k in range(1,10)]
        plt.figure(figsize=(8,6))
        plt.plot(range(1,10),[i.inertia_ for i in preKMeans],'bo-')
        plt.show()

    #
    def clusters_silhouette(self):
        k = 5
        X, y = self.initBlobsData()
        preKMeans = [KMeans(n_clusters=k).fit(X) for k in range(1, 10)]

        plt.figure(figsize=(8,5))
        plt.plot( range(2,10),[silhouette_score(X,preKMeans[i].predict(X))  for i in range(1,9)],"yo-")
        plt.show()

    def keansPic(self):
        img = imread(r"./聚类算法-实验/ladybug.png")
        img = img.reshape(-1,3)
        kmeans = KMeans(n_clusters=8,random_state=1)
        kmeans.fit(img)
        print(kmeans.cluster_centers_.shape)
        print(kmeans.labels_.shape)
        print(kmeans.cluster_centers_[kmeans.labels_.shape])


if __name__ == '__main__':
    import math
    ct = ClusterTest()
    # ct.kmeansTest()
    # ct.kmeansShow_iter()
    # ct.clusters_inertia()
    # ct.clusters_silhouette()
    ct.keansPic()
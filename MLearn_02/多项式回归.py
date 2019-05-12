import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


class PolynomialRegression():

    def __init__(self):

            data = np.genfromtxt("./datas/job.csv", delimiter=",")
            self.x = data[1:, 1, np.newaxis]
            self.y = data[1:, 2, np.newaxis]


    def runLineRegression(self):
        regression = LinearRegression()
        regression.fit(self.x, self.y)
        print(regression.coef_, regression.intercept_)
        print(regression.predict([[11]]))

        plt.plot(self.x,self.y,'c.')
        plt.plot(self.x,regression.predict(self.x),'r')
        plt.show()

    def runPolynomialFeatures(self):
        polynomial = PolynomialFeatures(degree=4)
        x_poly = polynomial.fit_transform(self.x)

        line = LinearRegression()
        line.fit(x_poly,self.y)

        print(line.coef_,line.intercept_)

        plt.plot(self.x, self.y, 'c.')
        plt.plot(self.x, line.predict(x_poly), 'r')
        # plt.show()

if __name__ == '__main__':
    polynoial = PolynomialRegression()
    # polynoial.runLineRegression()
    polynoial.runPolynomialFeatures()
# coding:utf-8
import numpy as np

seed = 3

def generateds():
    rdm = np.random.RandomState(seed)
    X = rdm.randn(500, 2)
    Y = [int(x1*x1 + x2*x2 < 2) for (x1, x2) in X]
    Y_COLOR = [['RED' if y else "BLUE"] for y in Y]

    X = np.vstack(X).reshape(-1, 2)
    Y = np.vstack(Y).reshape(-1, 1)
    return X, Y, Y_COLOR
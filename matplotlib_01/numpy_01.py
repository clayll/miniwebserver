import  numpy as np

a = np.array([[1,3,4],[2,3,7]])
# print(a)
# b = np.ones((1,3),dtype=np.int)
# print(b)




c = np.array([[[1,3,4],[2,3,7]],[[1,2,3],[1,2,3]]])
d = np.ones((1,3))


x = a.transpose()
print(x)
print("*"*30)
z = np.where(x<3,7,89)
print(z)



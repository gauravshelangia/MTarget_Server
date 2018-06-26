import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

dataset = np.loadtxt("one.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,1:27]
Y = dataset[:,0]-624
Y = Y.astype(int)
s = X.shape
#Y = Y.reshape(23,28)

for i in range(s[0]):
    for j in range(s[1]):
        if (X[i][j]< -50):
            X[i][j]= X[i][j]


X_ = np.zeros((1,644))
X_[0]=-100
i=24
#X_.reshape(644,1)
X_[0,Y] = X[:,i]
S = X_.reshape(23,28)
#X_[Y] = X[1]
print X[:,i]
print X_.shape
#X_1 = X[:,0].reshape()

#img = plt.imread("first_floor.png")
#fig,ax = plt.subplots()
#ax.imshow(img)
plt.contour(S)
plt.show(block=True)

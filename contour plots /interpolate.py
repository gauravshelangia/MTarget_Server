import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import copy

dataset = np.loadtxt("one.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,1:27]
Y = dataset[:,0]-624
Y = Y.astype(int)
s = X.shape

for i in range(s[0]):
    for j in range(s[1]):
        if (X[i][j]< -50):
            X[i][j]= X[i][j]

X_ = np.zeros((1,644))
X_[0]=-100
i=21
X_[0,Y] = X[:,i]
S = X_.reshape(23,28)
old = copy.copy(S)

#print old

# matrix to track the original signal strenght -- shouldn't change
A = np.ones((23,28))
A[S==-100] = 0

# interpolate the S -- fill the empty grid
for itr in range(3000):
    for i in range(23):
        for j in range(28):
            if (A[i][j]!=1):
                if(j==0):
                    if(i==0):
                        S[i,j] = ( S[i,j+1] + S[i+1,j] )/2
                    elif(i==22):
                        S[i,j] = (S[i-1,j] + S[i,j+1])/2
                    else:
                        S[i,j] = (S[i,j+1]+S[i-1,j]+S[i+1,j])/3

                elif (i==0):
                    if(j==0):
                        S[i,j] = ( S[i,j+1] + S[i+1,j] )/2
                    elif(j==27):
                        S[i,j] = ( S[i,j-1] + S[i+1,j] )/2
                    else:
                        S[i,j] = (S[i,j+1]+S[i,j-1]+S[i+1,j])/3

                elif(j==27):
                    if(i==0):
                        S[i,j] = ( S[i,j-1] + S[i+1,j] )/2
                    elif(i==22):
                        S[i,j] = (S[i,j-1] + S[i-1,j])/2
                    else:
                        S[i,j] = (S[i-1,j]+S[i+1,j]+S[i,j-1])/3

                elif(i==22):
                    if(j==0):
                        S[i,j] = (S[i-1,j] + S[i,j+1])/2
                    elif(j==27):
                        S[i,j] = (S[i,j-1] + S[i-1,j])/2
                    else:
                        S[i,j] = (S[i,j-1]+S[i,j+1]+S[i-1,j])/3
                else:
                    S[i,j]= (S[i,j-1] + S[i,j+1] + S[i-1,j] + S[i+1,j])/4


    diff = old-S
    square = np.square(diff)
    sum_mean = np.sum(square)/(23*28)
    #plt.figure()
    #plt.contour(S)

plt.contour(S)
plt.show()

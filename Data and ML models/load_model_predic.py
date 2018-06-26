from keras.models import load_model
import numpy as np
from keras.utils import np_utils

dataset = np.loadtxt("rssi2ghz_train.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,1:27]
Y = dataset[:,0]
Y =np_utils.to_categorical(Y, 1101)


M = load_model('mtarget_model.h5')
k = X[27,:]
x = k.reshape(1,26)
result = M.predict(x)
print(result.argmax(axis = 1)[0])

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np
from keras import backend as K
import tensorflow as tf
from keras.models import load_model
from keras.models import model_from_json
from tensorflow.contrib.learn.python.learn.utils import export
from tensorflow.contrib.session_bundle import exporter
import tflearn
from keras import regularizers
from keras.regularizers import l2

n_classes = 1268

model = load_model('mtarget_model_full1.h5')

accuracy = 0
for exp in range(101):
    datasettest = np.loadtxt("rssi2ghtest_1.csv", delimiter=",")
    # split into input (X) and output (Y) variables
    #np.random.shuffle(datasettest)
    noise = np.random.normal(0,5,datasettest.shape[0]*26)
    noise = noise.reshape(datasettest.shape[0],26)

    Xtest = datasettest[:,1:27]
    Xtest = Xtest + noise
    Y = datasettest[:,0]
    Ytest = tflearn.data_utils.to_categorical(Y, n_classes)

    #print "evaluating"
    # calculate predictions
    #predictions = model.predict(Xtest)
    #p = predictions.argmax(axis = 1)
    #print p
    #print Y
    scores = model.evaluate(Xtest,Ytest,verbose=0)
    accuracy = accuracy+scores[1]*100
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))



print "accuracy is ", accuracy/100

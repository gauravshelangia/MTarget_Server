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


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# load pima indians dataset
dataset = np.loadtxt("rssi2ghztrain_1.csv", delimiter=",")
# split into input (X) and output (Y) variables
np.random.shuffle(dataset)
X = dataset[:,1:27]
Y = dataset[:,0]
n_classes = 1268
print(Y.argmax(axis = 0))
Y =tflearn.data_utils.to_categorical(Y, n_classes)

# creating callbacks for early stopping
earlyStopping=keras.callbacks.EarlyStopping(monitor='acc', patience=100, verbose=0, mode='auto')
# create model
model = Sequential()
model.add(Dense(100, input_dim=26, activation='relu'))
model.add(Dense(60, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(n_classes, activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
# Fit the model
for epoch in range(5000):
    fit = model.fit(X, Y, nb_epoch=1, batch_size=20,validation_split=0.2, verbose=1)
    print epoch
    if fit.history['val_acc'][0]*100 >= 99.5     :
        break;

# calculate predictions
k = X[0,:]
x = k.reshape(1,26)
result = model.predict(x)

print((result.argmax(axis = 1)))


# save model for later purpose only single file can be loaded into dl4j
model.save('mtarget_model_full1.h5') ## sometime doesnot work nno need to check now

# save model in json file
# serialize model to JSON
model_json = model.to_json()
with open("Mtarget_Model_json", "w") as json_file:
    json_file.write(model_json)

# Save model weights
model.save_weights('Mtarget_weights')
M = load_model('mtarget_model_full1.h5')

print ("result from saved model ")

k = X[0,:]
x = k.reshape(1,26)
result = M.predict(x)

print((result.argmax(axis = 1)))


#sess = K.get_session()
#tf.train.write_graph(sess.graph_def,'models/', 'ts_bin_graph.pb',as_text=False)

#layer = model.layers
#    saver = tf.train.Saver({'w':layer.get_weights})
#w = layer[0].get_weights()
#saver = tf.train.Saver({'w':w})

# round predictions
#rounded = [round(x) for x in predictions]
#print(rounded)

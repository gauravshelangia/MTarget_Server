import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
import csv
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.utils import np_utils


def import_data(path):
    print("loading training data")
    data = np.genfromtxt(path, delimiter=',')
    data = data.astype('int')
    X = data[:,1:27]
    Y = data[:,0:1]
    return X,Y


trainX, trainY = import_data("data_openspace/tt.csv")
trainY =np_utils.to_categorical(trainY, 1101)
#trainY = list(trainY).asint16
#trainY = tf.one_hot(trainY,1101)

print trainX.shape
print trainY.shape

# number of nodes in input layer
nodes_input = trainX.shape[1]
# number of neuron in hidden layer
nodes_hl1 = 100
# number of nodes in second hidded layer
nodes_hl2 = 60
# number of nodes in output layer
nodes_output = 1101 #trainY.shape[1]

# define placeholders
x = tf.placeholder(tf.float32, [None, trainX.shape[1]])
y = tf.placeholder(tf.int32, [None, nodes_output])
print y.shape

epochs = 5000
learning_rate = 0.001

weights = {
    'hidden1': tf.Variable(tf.random_normal([nodes_input, nodes_hl1])),
    'hidden2': tf.Variable(tf.random_normal([nodes_hl1, nodes_hl2])),
    'output': tf.Variable(tf.random_normal([nodes_hl2,nodes_output]))
}

biases = {
    'hidden1': tf.Variable(tf.random_normal([nodes_hl1])),
    'hidden2': tf.Variable(tf.random_normal([nodes_hl2])),
    'output': tf.Variable(tf.random_normal([nodes_output]))
}

print weights['hidden1'].get_shape()
print weights['output'].get_shape()

# hidden layer 1
hidden_layer_mat_add_op_1 = tf.add(tf.matmul(x, weights['hidden1']), biases['hidden1'])
hidden_layer_act_1 = tf.nn.relu(hidden_layer_mat_add_op_1)
# hidden layer 2
hidden_layer_mat_add_op_2 = tf.add(tf.matmul(hidden_layer_act_1, weights['hidden2']), biases['hidden2'])
hidden_layer_act_2 = tf.nn.relu(hidden_layer_mat_add_op_2)
# output layer
output_layer_mat_add_out = tf.add(tf.matmul(hidden_layer_act_2, weights['output']), biases['output'])
output_layer = tf.nn.relu(output_layer_mat_add_out)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output_layer,labels= y))
#cost = tf.squared_difference(output_layer,y)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
init = tf.global_variables_initializer()


with tf.Session() as sess:
    # create initialized variables
    sess.run(init)
    c = 100
    for epoch in range (epochs):
        C = 0
        epoch_loss = 0
        #_,c = sess.run([optimizer,cost],feed_dict={x: trainX, y: trainY})
        for i in range(trainX.shape[0]):
            #print trainX[i,:]
            _, c = sess.run([optimizer, cost], feed_dict = {x: [trainX[i,:]], y: [trainY[i]]})
            epoch_loss += c
            #print y
        print "Cost after epoch ", epoch," is : ", epoch_loss

    print weights['hidden1'].eval(sess)
    #print " weights at output layer", weights['output'].eval()
    #print " weights at hidden layer", tf.transpose(weights['hidden']).eval()
    """
    testx = np.linspace(0,2*np.pi,num=1000)
    testx = np.array([testx]).T
    print testx.shape
    testY  = sess.run(test_op,feed_dict={testX: testx} )
    """
    #print weights['hidden'].get_shape()

    #pred_temp = tf.equal(tf.argmax(output_layer, 1), tf.argmax(y, 1))
    #accuracy = tf.reduce_mean(tf.cast(pred_temp, "float"))

#plt.plot(trainX,trainY,label='train')
#plt.plot(testx,testY,label='test')
#plt.show(block=False)

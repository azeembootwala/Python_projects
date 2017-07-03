import numpy as np
import tensorflow as tf
from sklearn.utils import shuffle
from process_AB import get_data


def tar2ind(Y):
    N = len(Y)
    D = len(set(Y))
    ind = np.zeros((N,D))
    for i in range(0,N):
        ind[i,Y[i]]=1
    return ind
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))
def forward(X,W1,B1,W2,B2):
    Z = tf.nn.sigmoid(tf.matmul(X,W1)+B1)
    return tf.matmul(Z,W2)+B2

def main():
    X,Y = get_data()
    X,Y = shuffle(X,Y)
    ind_mat = tar2ind(Y)
    N,D = X.shape
    M = 6
    K = len(set(Y))

    W1 = init_weights([D,M])
    b1 = init_weights([M])
    W2 = init_weights([M,K])
    b2 = init_weights([K])

    tfX = tf.placeholder(tf.float32,[None,D])
    tfY = tf.placeholder(tf.float32,[None,K])

    logit = forward(tfX,W1,b1,W2,b2)

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=ind_mat,logits=logit))

    training_op = tf.train.GradientDescentOptimizer(0.1).minimize(cost)
    predict_op = tf.argmax(logit,1)

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    for i in range(0,100000):
        sess.run(training_op,feed_dict={tfX:X,tfY:ind_mat})
        pred=sess.run(predict_op,feed_dict={tfX:X,tfY:ind_mat})
        if i % 50==0:
            print(np.mean(pred==Y))






if __name__=="__main__":
    main()

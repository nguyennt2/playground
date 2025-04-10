import tensorflow as tf
from tensorflow.keras.backend import K

def relu(x):
    return K.maximum(0, x)
def sigmoid(x):
    return 1 / (1 + K.exp(-x))

import tensorflow as tf
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, TimeDistributed
from tensorflow.keras.models import Sequential


def build_cnn():
    """
    CNN to extract spatial features from hand landmarks
    Input per frame: (21 landmarks, 3 values)
    """

    cnn = Sequential(name="Hand_CNN")

    cnn.add(Conv1D(64, kernel_size=3, activation='relu',
                   input_shape=(21, 3)))
    cnn.add(MaxPooling1D(pool_size=2))

    cnn.add(Conv1D(128, kernel_size=3, activation='relu'))
    cnn.add(MaxPooling1D(pool_size=2))

    cnn.add(Flatten())

    return cnn

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, TimeDistributed
from models.cnn_model import build_cnn


def build_lstm(num_classes):
    """
    Full CNN + LSTM model
    """

    cnn = build_cnn()

    model = Sequential(name="CNN_LSTM_Gesture_Model")

    # Apply CNN to each frame
    model.add(TimeDistributed(cnn, input_shape=(30, 21, 3)))

    # Temporal learning
    model.add(LSTM(128, return_sequences=False))
    model.add(Dropout(0.3))

    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    return model

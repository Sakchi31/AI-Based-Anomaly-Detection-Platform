import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(8, activation='relu', input_shape=(3,)),
    Dense(4, activation='relu'),
    Dense(8, activation='relu'),
    Dense(3)
])

model.compile(optimizer='adam', loss='mse')

train_data = np.array([
    [70,98,36.5],
    [75,97,36.6],
    [72,99,36.7],
    [80,97,36.5],
    [65,98,36.4]
])

model.fit(train_data, train_data, epochs=50, verbose=0)

def detect_autoencoder(data):

    reconstructed = model.predict(data)

    loss = np.mean((data - reconstructed)**2)

    if loss > 1:
        return "ANOMALY"

    return "NORMAL"
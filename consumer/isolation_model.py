from sklearn.ensemble import IsolationForest
import numpy as np

train_data = np.array([
    [70,98,36.5],
    [75,97,36.6],
    [72,99,36.7],
    [80,97,36.5],
    [65,98,36.4]
])

model = IsolationForest(contamination=0.1)

model.fit(train_data)

def detect(data):

    result = model.predict(data)

    if result[0] == -1:
        return "ANOMALY"

    return "NORMAL"
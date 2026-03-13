import numpy as np

def preprocess(vitals):

    heart_rate = vitals["heart_rate"]
    spo2 = vitals["spo2"]
    temperature = vitals["temperature"]

    return np.array([[heart_rate, spo2, temperature]])
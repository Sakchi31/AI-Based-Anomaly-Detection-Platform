import random
import time

from consumer.preprocess import preprocess
from consumer.isolation_model import detect
from database.db import cursor, conn

while True:

    vitals = {
        "patient_id": random.randint(1,10),
        "heart_rate": random.randint(50,140),
        "spo2": random.randint(85,100),
        "temperature": round(random.uniform(36,39),2)
    }

    processed = preprocess(vitals)

    status = detect(processed)

    print(vitals, status)

    cursor.execute(
        "INSERT INTO vitals (patient_id,heart_rate,spo2,temperature,status) VALUES (?,?,?,?,?)",
        (
            vitals["patient_id"],
            vitals["heart_rate"],
            vitals["spo2"],
            vitals["temperature"],
            status
        )
    )

    conn.commit()

    time.sleep(2)
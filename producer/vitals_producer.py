from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    vitals = {
        "patient_id": random.randint(1,10),
        "heart_rate": random.randint(50,140),
        "spo2": random.randint(85,100),
        "temperature": round(random.uniform(36,39),2)
    }

    producer.send("patient_vitals", vitals)

    print("Sent:", vitals)

    time.sleep(1)
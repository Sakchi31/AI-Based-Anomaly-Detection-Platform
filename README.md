# AI-Based Anomaly Detection Platform

This project detects anomalies in patient vital signs using machine learning.

## Features
- Real-time patient vitals simulation
- Anomaly detection using Isolation Forest
- Data stored in SQLite database
- REST API using Flask
- Dashboard visualization

## Tech Stack
- Python
- Flask
- Scikit-learn
- SQLite
- Streamlit

## Run Project

Install dependencies:

pip install -r requirements.txt

Run API:

python api/app.py

Run consumer:

python -m consumer.vitals_consumer

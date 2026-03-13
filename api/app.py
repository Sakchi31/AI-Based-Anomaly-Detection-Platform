from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("vitals.db", check_same_thread=False)

cursor = conn.cursor()

@app.route("/vitals")
def get_vitals():

    cursor.execute("SELECT * FROM vitals")

    rows = cursor.fetchall()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Yemon over LAN!"})

@app.route("/data")
def get_data():
    with open("yaman.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
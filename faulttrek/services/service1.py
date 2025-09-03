from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/fast")
def fast():
    return jsonify({"message": "fast response"})

@app.route("/slow")
def slow():
    delay = random.randint(2,5)
    time.sleep(delay)
    return jsonify({"message": f"slow response {delay}s"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

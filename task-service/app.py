from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/tasks")
def tasks():
    return jsonify([{"id": 1, "title": "Write code"}, {"id": 2, "title": "Test app"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
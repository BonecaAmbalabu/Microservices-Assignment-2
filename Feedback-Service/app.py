from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

feedback_list = []
next_id = 1

@app.route("/feedback", methods=["GET"])
def get_feedback():
    return jsonify(feedback_list)

@app.route("/feedback", methods=["POST"])
def add_feedback():
    global next_id
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Feedback message is required"}), 400

    new_feedback = {
        "id": next_id,
        "message": data["message"]
    }
    feedback_list.append(new_feedback)
    next_id += 1
    return jsonify(new_feedback), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

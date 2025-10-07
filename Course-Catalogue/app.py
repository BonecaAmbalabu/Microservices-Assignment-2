from flask import Flask, jsonify

app = Flask(__name__)

# fake course data for demo
COURSES = [
    {"code": "CS101", "title": "Introduction to Programming", "credits": 15},
    {"code": "CS201", "title": "Data Structures", "credits": 20},
    {"code": "CS301", "title": "Databases", "credits": 20}
]

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(COURSES)

@app.route("/courses/<code>", methods=["GET"])
def get_course(code):
    course = next((c for c in COURSES if c["code"].lower() == code.lower()), None)
    if course:
        return jsonify(course)
    return {"error": "Course not found"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

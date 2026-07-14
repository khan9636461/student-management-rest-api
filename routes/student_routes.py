from flask import Blueprint, request, jsonify
from models import db, Student

# Create Blueprint
student_bp = Blueprint("student_bp", __name__)


# ==========================
# GET ALL STUDENTS
# ==========================
@student_bp.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    return jsonify([student.to_dict() for student in students]), 200


# ==========================
# GET STUDENT BY ID
# ==========================
@student_bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.to_dict()), 200


# ==========================
# CREATE STUDENT
# ==========================
@student_bp.route("/students", methods=["POST"])
def create_student():

    data = request.get_json()

    # Validate request body
    required_fields = ["name", "age", "email", "course"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    # Check duplicate email
    existing_student = Student.query.filter_by(email=data["email"]).first()

    if existing_student:
        return jsonify({"error": "Email already exists"}), 400

    student = Student(
        name=data["name"],
        age=data["age"],
        email=data["email"],
        course=data["course"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "message": "Student created successfully",
        "student": student.to_dict()
    }), 201


# ==========================
# UPDATE STUDENT
# ==========================
@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()

    student.name = data.get("name", student.name)
    student.age = data.get("age", student.age)
    student.email = data.get("email", student.email)
    student.course = data.get("course", student.course)

    db.session.commit()

    return jsonify({
        "message": "Student updated successfully",
        "student": student.to_dict()
    }), 200


# ==========================
# DELETE STUDENT
# ==========================
@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({
        "message": "Student deleted successfully"
    }), 200
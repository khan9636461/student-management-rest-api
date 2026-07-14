from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy object
db = SQLAlchemy()


class Student(db.Model):
    """
    Student Model
    Represents the students table in the SQLite database.
    """

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """
        Convert Student object into dictionary.
        Useful for returning JSON responses.
        """
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "course": self.course
        }

    def __repr__(self):
        return f"<Student {self.name}>"
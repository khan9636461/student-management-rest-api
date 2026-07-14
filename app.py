from flask import Flask, render_template
from flask_cors import CORS
from config import Config
from models import db
from routes.student_routes import student_bp


def create_app():

    app = Flask(
        __name__,
        template_folder="frontend",
        static_folder="frontend"
    )

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    app.register_blueprint(student_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.medicine import Medicine, MedicineRepository
from src.domain.user import User, UserRepository


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_by_id(body["user"])

        if user is None or (body["password"]) != user.password:
            return "", 401

        return user.to_dict(), 200

    @app.route("/api/medicines", methods=["GET"])
    def medicines_get_all():
        all_medicines = repositories["medicines"].get_all()
        return object_to_json(all_medicines)

    @app.route("/api/medicines", methods=["POST"])
    def medicines_post():
        body = request.json
        medicine = Medicine(**body)
        repositories["medicines"].save(medicine)
        return "", 200

    @app.route("/api/medicines/<id>", methods=["GET"])
    def medicines_get_by_id(id):
        one_medicine = repositories["medicines"].get_by_id(id)
        return object_to_json(one_medicine)

    @app.route("/api/medicines/<id>", methods=["PUT"])
    def medicines_put(id):
        body = request.json
        medicine = Medicine(**body)
        repositories["medicines"].save(medicine)
        return "", 200

    @app.route("/api/medicines/<id>", methods=["DELETE"])
    def medicine_delete_by_id(id):
        one_medicine = repositories["medicines"].delete_by_id(id)
        return "", 200

    @app.route("/api/medicines/by-date/<date>", methods=["GET"])
    def medicines_get_by_date(date):
        validated_medicines = repositories["medicines"].get_by_date(date)
        return object_to_json(validated_medicines)

    @app.route("/api/users", methods=["GET"])
    def get_all_users():
        all_users = repositories["users"].get_all()
        return object_to_json(all_users)

    return app

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
        user = repositories["users"].get_by_id(body["id_user"])

        if user is None or (body["password"]) != user.password:
            return "", 401

        return user.to_dict(), 200

    @app.route("/api/medicines", methods=["GET"])
    def medicines_get_all():
        id_user = request.headers.get("Authorization")
        all_medicines = repositories["medicines"].search_by_user_id(id_user)
        return object_to_json(all_medicines)

    @app.route("/api/medicines", methods=["POST"])
    def medicines_post():
        user_id = request.headers.get("Authorization")

        body = request.json
        medicine = Medicine(
            id_medicine=body["id_medicine"],
            id_user=user_id,
            name_medicine=body["name_medicine"],
            type_medicine=body["type_medicine"],
            description=body["description"],
            dosage={
                "dosages_times": body["dosage"]["dosages_times"],
                "hour_dosage": body["dosage"]["hour_dosage"],
                "days_dosage": body["dosage"]["days_dosage"],
            },
            start_date=body["start_date"],
            end_date=body["end_date"],
        )
        repositories["medicines"].save(medicine)
        return "", 200

    @app.route("/api/medicines/<id>", methods=["GET"])
    def medicines_get_by_id(id):
        id_user = request.headers.get("Authorization")
        medicine = repositories["medicines"].get_by_id(id)

        if id_user == medicine.id_user:
            return object_to_json(medicine), 200
        else:
            return "", 403

    @app.route("/api/medicines/<id>", methods=["PUT"])
    def medicines_put(id):
        user_id = request.headers.get("Authorization")
        body = request.json

        medicine = Medicine(
            id_medicine=body["id_medicine"],
            id_user=user_id,
            name_medicine=body["name_medicine"],
            type_medicine=body["type_medicine"],
            description=body["description"],
            dosage={
                "dosages_times": body["dosage"]["dosages_times"],
                "hour_dosage": body["dosage"]["hour_dosage"],
                "days_dosage": body["dosage"]["days_dosage"],
            },
            start_date=body["start_date"],
            end_date=body["end_date"],
        )
        repositories["medicines"].save(medicine)
        return "", 200

    @app.route("/api/medicines/<id>", methods=["DELETE"])
    def medicine_delete_by_id(id):
        one_medicine = repositories["medicines"].delete_by_id(id)
        return "", 200

    @app.route("/api/medicines/by-date/<date>", methods=["GET"])
    def medicines_get_by_date(date):
        id_user = request.headers.get("Authorization")
        print("webserver-------------->", date, id_user)
        validated_medicines = repositories["medicines"].get_by_date(date, id_user)
        return object_to_json(validated_medicines)

    @app.route("/api/users", methods=["GET"])
    def get_all_users():
        all_users = repositories["users"].get_all()
        return object_to_json(all_users)

    return app

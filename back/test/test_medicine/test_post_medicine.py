from src.lib.utils import temp_file
from flask import json

from src.webserver import create_app
from src.domain.medicine import MedicineRepository


def test_should_return_post_new_medicines():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

    body = {
        "id_medicine": "0050",
        "name_medicine": "Paracetamol",
        "type_medicine": "pill",
        "description": "Beber con agua fria",
        "dosage": {
            "dosages_times": "2 veces por semana",
            "hour_dosage": "08:00",
            "days_dosage": "['Mar', 'Vier']",
        },
        "start_date": "2022-03-01",
        "end_date": "2022-04-01",
    }

    response = client.post("/api/medicines", json=body)

    response_get = client.get("/api/medicines/0050")

    assert response.status_code == 200

    assert response_get.json == {
        "id_medicine": "0050",
        "name_medicine": "Paracetamol",
        "type_medicine": "pill",
        "description": "Beber con agua fria",
        "dosage": {
            "dosages_times": "2 veces por semana",
            "hour_dosage": "08:00",
            "days_dosage": "['Mar', 'Vier']",
        },
        "start_date": "2022-03-01",
        "end_date": "2022-04-01",
    }

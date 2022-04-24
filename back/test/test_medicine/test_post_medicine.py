from src.lib.utils import temp_file

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

    client.post("/api/medicines", json=body)

    response_get = client.get("/api/medicines/0050")

    assert response_get.status_code == 200
    save_medicine = response_get.json

    assert save_medicine["id_medicine"] == "0050"
    assert save_medicine["name_medicine"] == "Paracetamol"
    assert save_medicine["type_medicine"] == "pill"
    assert save_medicine["description"] == "Beber con agua fria"
    assert save_medicine["dosage"]["dosages_times"] == "2 veces por semana"
    assert save_medicine["dosage"]["hour_dosage"] == "08:00"
    assert save_medicine["dosage"]["days_dosage"] == "['Mar', 'Vier']"
    assert save_medicine["start_date"] == "2022-03-01"
    assert save_medicine["end_date"] == "2022-04-01"

from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.medicine import MedicineRepository, Medicine


def setup():
    return ""


def test_should_update_contact():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

    # save medicine
    medicine01 = Medicine(
        id_medicine="0050",
        name_medicine="Paracetamol",
        type_medicine="pill",
        description="Beber con agua fria",
        dosage={
            "dosages_times": "2 veces por semana",
            "hour_dosage": "08:00",
            "days_dosage": ["Mar", "Vier"],
        },
        start_date="2022-03-01",
        end_date="2022-04-01",
    )

    medicine_repository.save(medicine01)

    # send modified medicine
    body = {
        "id_medicine": "0050",
        "name_medicine": "Paracetamol",
        "type_medicine": "pill",
        "description": "Debes tomarlo por la noche",
        "dosage": {
            "dosages_times": "2 veces por semana",
            "hour_dosage": "08:00",
            "days_dosage": ["Mar", "Vier"],
        },
        "start_date": "2022-03-01",
        "end_date": "2022-04-01",
    }

    response = client.put("/api/medicines/0050")

    assert response.status_code == 200

    # get the modified medicine and verify this change
    response_get = client.get("/api/medicines/0050")
    medicine = response_get.json

    assert medicine["id_medicine"] == "0050"
    assert medicine["name_medicine"] == "Paracetamol"
    assert medicine["type_medicine"] == "pill"
    assert medicine["description"] == "Debes tomarlo por la noche"
    assert medicine["dosage"]["dosages_times"] == "2 veces por semana"
    assert medicine["dosage"]["hour_dosage"] == "08:00"
    assert medicine["dosage"]["days_dosage"] == ["Mar", "Vier"]
    assert medicine["start_date"] == "2022-03-01"
    assert medicine["end_date"] == "2022-04-01"

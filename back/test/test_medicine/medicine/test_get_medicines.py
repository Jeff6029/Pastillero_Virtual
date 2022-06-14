from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.medicine import MedicineRepository, Medicine


def test_should_return_empty_list():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

    response = client.get("/api/medicines")
    assert response.json == []


def test_should_return_all_complete_medicines():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

    medicine_01 = Medicine(
        id_medicine="0050",
        id_user="user-1",
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

    medicine_02 = Medicine(
        id_medicine="0051",
        id_user="user-1",
        name_medicine="Bepanthol",
        type_medicine="cream",
        description="Aplicarlo suavemente",
        dosage={
            "dosages_times": "2 veces por semana",
            "hour_dosage": "09:00",
            "days_dosage": ["Lun", "Juev"],
        },
        start_date="2022-04-01",
        end_date="2022-05-01",
    )

    medicine_repository.save(medicine_01)
    medicine_repository.save(medicine_02)

    response = client.get("/api/medicines")

    assert response.status_code == 200
    all_medicines = response.json
    assert len(all_medicines) == 2

    assert all_medicines[0]["id_medicine"] == "0050"
    assert all_medicines[0]["name_medicine"] == "Paracetamol"
    assert all_medicines[0]["type_medicine"] == "pill"
    assert all_medicines[0]["description"] == "Beber con agua fria"
    assert all_medicines[0]["dosage"]["dosages_times"] == "2 veces por semana"
    assert all_medicines[0]["dosage"]["hour_dosage"] == "08:00"
    assert all_medicines[0]["dosage"]["days_dosage"] == ["Mar", "Vier"]
    assert all_medicines[0]["start_date"] == "2022-03-01"
    assert all_medicines[0]["end_date"] == "2022-04-01"

    assert all_medicines[1]["id_medicine"] == "0051"
    assert all_medicines[1]["name_medicine"] == "Bepanthol"
    assert all_medicines[1]["type_medicine"] == "cream"
    assert all_medicines[1]["description"] == "Aplicarlo suavemente"
    assert all_medicines[1]["dosage"]["dosages_times"] == "2 veces por semana"
    assert all_medicines[1]["dosage"]["hour_dosage"] == "09:00"
    assert all_medicines[1]["dosage"]["days_dosage"] == ["Lun", "Juev"]
    assert all_medicines[1]["start_date"] == "2022-04-01"
    assert all_medicines[1]["end_date"] == "2022-05-01"

from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.medicine import MedicineRepository, Medicine


def test_should_return_empty_list_medicines():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

    medicine01 = Medicine(
        id_medicine="0050",
        name_medicine="Paracetamol",
        type_medicine="pill",
        description="Beber con agua fria",
        dosage={
            "dosages_times": "2 veces por semana",
            "hour_dosage": "08:00",
            "days_dosage": "['Mar', 'Vier']",
        },
        start_date="2022-03-01",
        end_date="2022-03-31",
    )

    medicine02 = Medicine(
        id_medicine="0051",
        name_medicine="Bepanthol",
        type_medicine="cream",
        description="Aplicarlo suavemente",
        dosage={
            "dosages_times": "2 veces por semana",
            "hour_dosage": "09:00",
            "days_dosage": "['Lun', 'Juev']",
        },
        start_date="2022-04-01",
        end_date="2022-04-30",
    )

    medicine_repository.save(medicine01)
    medicine_repository.save(medicine02)

    response = client.get("/api/medicines/by-date/2022-05-15")

    assert response.status_code == 200
    assert response.json == []


def test_should_return_list_medicines():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

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
        start_date="2022-03-15",
        end_date="2022-04-15",
    )

    medicine02 = Medicine(
        id_medicine="0051",
        name_medicine="Bepanthol",
        type_medicine="cream",
        description="Aplicarlo suavemente",
        dosage={
            "dosages_times": "2 veces por semana",
            "hour_dosage": "09:00",
            "days_dosage": ["Lun", "Juev"],
        },
        start_date="2022-04-15",
        end_date="2022-05-15",
    )

    medicine_repository.save(medicine01)
    medicine_repository.save(medicine02)

    response = client.get("/api/medicines/by-date/2022-04-15")

    assert response.status_code == 200
    list_medicines = response.json
    assert list_medicines[0]["id_medicine"] == "0051"
    assert list_medicines[0]["start_date"] == "2022-04-15"
    assert list_medicines[0]["end_date"] == "2022-05-15"
    assert list_medicines[1]["id_medicine"] == "0050"
    assert list_medicines[1]["start_date"] == "2022-03-15"
    assert list_medicines[1]["end_date"] == "2022-04-15"

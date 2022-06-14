from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.medicine import MedicineRepository, Medicine


def test_should_return_medicine_by_id():
    medicine_repository = MedicineRepository(temp_file())
    app = create_app(repositories={"medicines": medicine_repository})
    client = app.test_client()

    medicine01 = Medicine(
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

    medicine02 = Medicine(
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

    medicine_repository.save(medicine01)
    medicine_repository.save(medicine02)

    response_medicine01 = client.get("/api/medicines/0050")
    response_medicine02 = client.get("/api/medicines/0051")

    assert response_medicine01.status_code == 200
    medicine_01 = response_medicine01.json
    assert medicine_01["id_medicine"] == "0050"
    assert medicine_01["name_medicine"] == "Paracetamol"
    assert medicine_01["type_medicine"] == "pill"
    assert medicine_01["description"] == "Beber con agua fria"
    assert medicine_01["dosage"]["dosages_times"] == "2 veces por semana"
    assert medicine_01["dosage"]["hour_dosage"] == "08:00"
    assert medicine_01["dosage"]["days_dosage"] == ["Mar", "Vier"]
    assert medicine_01["start_date"] == "2022-03-01"
    assert medicine_01["end_date"] == "2022-04-01"

    assert response_medicine02.status_code == 200
    medicine_02 = response_medicine02.json
    assert medicine_02["id_medicine"] == "0051"
    assert medicine_02["name_medicine"] == "Bepanthol"
    assert medicine_02["type_medicine"] == "cream"
    assert medicine_02["description"] == "Aplicarlo suavemente"
    assert medicine_02["dosage"]["dosages_times"] == "2 veces por semana"
    assert medicine_02["dosage"]["hour_dosage"] == "09:00"
    assert medicine_02["dosage"]["days_dosage"] == ["Lun", "Juev"]
    assert medicine_02["start_date"] == "2022-04-01"
    assert medicine_02["end_date"] == "2022-05-01"

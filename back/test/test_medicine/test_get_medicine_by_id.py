from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.medicine import MedicineRepository, Medicine


def test_should_return_medicine_by_id():
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
        end_date="2022-04-01",
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
        start_date="2022-04-01",
        end_date="2022-05-01",
    )

    medicine_repository.save(medicine01)
    medicine_repository.save(medicine02)

    response_medicine01 = client.get("/api/medicines/0050")
    response_medicine02 = client.get("/api/medicines/0051")

    assert response_medicine01.json == {
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
    assert response_medicine02.json == {
        "id_medicine": "0051",
        "name_medicine": "Bepanthol",
        "type_medicine": "cream",
        "description": "Aplicarlo suavemente",
        "dosage": {
            "dosages_times": "2 veces por semana",
            "hour_dosage": "09:00",
            "days_dosage": ["Lun", "Juev"],
        },
        "start_date": "2022-04-01",
        "end_date": "2022-05-01",
    }

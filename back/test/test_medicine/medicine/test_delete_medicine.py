from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.medicine import MedicineRepository, Medicine


def setup():
    return ""


# def setup():
#     user_repository = UserRepository(temp_file())
#     app = create_app(repositories={"users": user_repository})
#     client = app.test_client()

#     tomas = User(id='user-tomas', name='Tomás', password='el mejor')
#     user_repository.save(tomas)

#     return client


def test_should_delete_medicine_and_return_empty_list():
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

    medicine_repository.save(medicine01)

    response_delete01 = client.delete(
        "/api/medicines/0050", headers={"Authorization": "user-1"}
    )
    response = client.get("/api/medicines", headers={"Authorization": "user-1"})

    assert response_delete01.status_code == 200
    delete_01 = response.json
    assert delete_01 == []


def test_should_delete_one_medicine_and_return_only_one_medicine():
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

    response_delete01 = client.delete(
        "/api/medicines/0050", headers={"Authorization": "user-1"}
    )

    response = client.get("/api/medicines", headers={"Authorization": "user-1"})

    assert response_delete01.status_code == 200
    list_medicines = response.json
    assert len(list_medicines) == 1
    assert list_medicines[0]["id_medicine"] == "0051"
    assert list_medicines[0]["start_date"] == "2022-04-01"
    assert list_medicines[0]["end_date"] == "2022-05-01"
    assert list_medicines[0]["dosage"]["days_dosage"] == ["Lun", "Juev"]

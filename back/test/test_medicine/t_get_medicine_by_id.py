# from src.lib.utils import temp_file

# from src.webserver import create_app
# from src.domain.medicine import MedicineRepository, Medicine


# def test_should_return_medicine_by_id():
#     medicine_repository = MedicineRepository(temp_file())
#     app = create_app(repositories={"medicine": medicine_repository})
#     client = app.test_client()

#     medicine_01 = Medicine(
#         id_medicine="0050",
#         name_medicine="Paracetamol",
#         type_medicine="pill",
#         dosage="2 veces por semana",
#         end_date="2022-04-01",
#     )

#     medicine_02 = Medicine(
#         id_medicine="0051",
#         name_medicine="Bepanthol",
#         type_medicine="cream",
#         dosage="2 veces por semana",
#         end_date="2022-05-01",
#     )

#     medicine_repository.save(medicine_01)
#     medicine_repository.save(medicine_02)

#     response_medicine_01 = client.get("/api/medicines/0050")
#     response_medicine_02 = client.get("/api/medicines/0051")

#     assert response_medicine_01.json == {
#         "id_medicine": "0050",
#         "name_medicine": "Paracetamol",
#         "type_medicine": "pill",
#         "dosage": "2 veces por semana",
#         "end_date": "2022-04-01",
#     }
#     assert response_medicine_02.json == {
#         "id_medicine": "0051",
#         "name_medicine": "Bepanthol",
#         "type_medicine": "cream",
#         "dosage": "2 veces por semana",
#         "end_date": "2022-05-01",
#     }


# @app.route("/api/medicines/<id>", methods=["GET"])
# def medicines_get_by_id(id_medicine):
#     one_medicine = repositories["medicines"].get_by_id(id_medicine)
#     return object_to_json(one_medicine)

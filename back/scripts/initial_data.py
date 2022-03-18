import sys

sys.path.insert(0, "")

from src.domain.info import Info, InfoRepository
from src.domain.medicine import Medicine, MedicineRepository

database_path = "data/database.db"

info_repository = InfoRepository(database_path)

info_repository.save(Info(app_name="pharminder-app"))

###### medicines

medicine_01 = Medicine(
    id_medicine="0050",
    name_medicine="Paracetamol",
    type_medicine="Pills",
    dosage="2 veces por semana",
    end_date="2022-04-01",
)
medicine_02 = Medicine(
    id_medicine="0051",
    name_medicine="Bepanthol",
    type_medicine="Cream",
    dosage="3 veces por semana",
    end_date="2022-05-01",
)
medicine_03 = Medicine(
    id_medicine="0052",
    name_medicine="Ibuprofeno",
    type_medicine="Pills",
    dosage="3 veces por semana",
    end_date="2022-06-01",
)
medicine_04 = Medicine(
    id_medicine="0053",
    name_medicine="Aquoral Monodosis",
    type_medicine="eye_drops",
    dosage="3 veces por semana",
    end_date="2022-05-02",
)

medicine_repository = MedicineRepository(database_path)

medicine_repository.save(medicine_01)
medicine_repository.save(medicine_02)
medicine_repository.save(medicine_03)
medicine_repository.save(medicine_04)

print("Base de datos inicializada en " + database_path)

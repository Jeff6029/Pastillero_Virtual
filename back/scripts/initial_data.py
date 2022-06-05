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
    description="Tomarlo con agua fria",
    dosage={
        "dosages_times": "2 veces por semana",
        "hour_dosage": "08:00",
        "days_dosage": [
            {"name": "Lun", "value": False},
            {"name": "Mar", "value": True},
            {"name": "Miér", "value": False},
            {"name": "Juev", "value": False},
            {"name": "Vier", "value": True},
            {"name": "Sáb", "value": False},
            {"name": "Dom", "value": False},
        ],
    },
    start_date="2022-06-01",
    end_date="2022-07-01",
)
medicine_02 = Medicine(
    id_medicine="0051",
    name_medicine="Bepanthol",
    type_medicine="Cream",
    description="Aplicarlo suavemente",
    dosage={
        "dosages_times": "3 veces por semana",
        "hour_dosage": "09:00",
        "days_dosage": [
            {"name": "Lun", "value": False},
            {"name": "Mar", "value": True},
            {"name": "Miér", "value": False},
            {"name": "Juev", "value": True},
            {"name": "Vier", "value": False},
            {"name": "Sáb", "value": True},
            {"name": "Dom", "value": False},
        ],
    },
    start_date="2022-05-15",
    end_date="2022-06-15",
)
medicine_03 = Medicine(
    id_medicine="0052",
    name_medicine="Ibuprofeno",
    type_medicine="Pills",
    description="Tomarlo con agua fria",
    dosage={
        "dosages_times": "3 veces por semana",
        "hour_dosage": "14:00",
        "days_dosage": [
            {"name": "Lun", "value": True},
            {"name": "Mar", "value": False},
            {"name": "Miér", "value": True},
            {"name": "Juev", "value": False},
            {"name": "Vier", "value": True},
            {"name": "Sáb", "value": False},
            {"name": "Dom", "value": False},
        ],
    },
    start_date="2022-06-10",
    end_date="2022-07-10",
)
medicine_04 = Medicine(
    id_medicine="0053",
    name_medicine="Aquoral Monodosis",
    type_medicine="eye_drops",
    description="Aplicar 3 gotas",
    dosage={
        "dosages_times": "2 veces por semana",
        "hour_dosage": "15:00",
        "days_dosage": [
            {"name": "Lun", "value": False},
            {"name": "Mar", "value": False},
            {"name": "Miér", "value": True},
            {"name": "Juev", "value": False},
            {"name": "Vier", "value": False},
            {"name": "Sáb", "value": False},
            {"name": "Dom", "value": True},
        ],
    },
    start_date="2022-06-16",
    end_date="2022-06-30",
)
medicine_05 = Medicine(
    id_medicine="0054",
    name_medicine="Eucerin",
    type_medicine="Cream",
    description="Aplicar antes salir",
    dosage={
        "dosages_times": "3 veces por semana",
        "hour_dosage": "15:00",
        "days_dosage": [
            {"name": "Lun", "value": False},
            {"name": "Mar", "value": True},
            {"name": "Miér", "value": True},
            {"name": "Juev", "value": False},
            {"name": "Vier", "value": False},
            {"name": "Sáb", "value": False},
            {"name": "Dom", "value": True},
        ],
    },
    start_date="2022-06-20",
    end_date="2022-07-20",
)
medicine_06 = Medicine(
    id_medicine="0055",
    name_medicine="Fisiocrem",
    type_medicine="Cream",
    description="Aplicar ante de cada cena",
    dosage={
        "dosages_times": "3 veces por semana",
        "hour_dosage": "15:00",
        "days_dosage": [
            {"name": "Lun", "value": True},
            {"name": "Mar", "value": False},
            {"name": "Miér", "value": False},
            {"name": "Juev", "value": True},
            {"name": "Vier", "value": False},
            {"name": "Sáb", "value": False},
            {"name": "Dom", "value": True},
        ],
    },
    start_date="2022-06-13",
    end_date="2022-07-13",
)


medicine_repository = MedicineRepository(database_path)

medicine_repository.save(medicine_01)
medicine_repository.save(medicine_02)
medicine_repository.save(medicine_03)
medicine_repository.save(medicine_04)
medicine_repository.save(medicine_05)
medicine_repository.save(medicine_06)

print("Base de datos inicializada en " + database_path)

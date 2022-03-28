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
        "days_dosage": "['Mar', 'Vier']",
    },
    start_date="2022-03-01",
    end_date="2022-04-01",
)
medicine_02 = Medicine(
    id_medicine="0051",
    name_medicine="Bepanthol",
    type_medicine="Cream",
    description="Aplicarlo suavemente",
    dosage={
        "dosages_times": "3 veces por semana",
        "hour_dosage": "09:00",
        "days_dosage": "['Mar', 'Vier']",
    },
    start_date="2022-03-02",
    end_date="2022-05-01",
)
medicine_03 = Medicine(
    id_medicine="0052",
    name_medicine="Ibuprofeno",
    type_medicine="Pills",
    description="Tomarlo con agua fria",
    dosage={
        "dosages_times": "3 veces por semana",
        "hour_dosage": "14:00",
        "days_dosage": "['Mar', 'Vier']",
    },
    start_date="2022-03-03",
    end_date="2022-06-01",
)
medicine_04 = Medicine(
    id_medicine="0053",
    name_medicine="Aquoral Monodosis",
    type_medicine="eye_drops",
    description="Aplicar 3 gotas",
    dosage={
        "dosages_times": "2 veces por semana",
        "hour_dosage": "15:00",
        "days_dosage": "['Mar', 'Vier']",
    },
    start_date="2022-03-04",
    end_date="2022-05-02",
)

medicine_repository = MedicineRepository(database_path)

medicine_repository.save(medicine_01)
medicine_repository.save(medicine_02)
medicine_repository.save(medicine_03)
medicine_repository.save(medicine_04)

print("Base de datos inicializada en " + database_path)

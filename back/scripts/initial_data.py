import sys

sys.path.insert(0, "")

from src.domain.info import Info, InfoRepository
from src.domain.medicine import Medicine, MedicineRepository
from src.domain.user import User, UserRepository

database_path = "data/database.db"

info_repository = InfoRepository(database_path)

info_repository.save(Info(app_name="pharminder-app"))

###### users:

user_repository = UserRepository(database_path)
user_repository.save(User(id_user="user-1", name="Jeff", password="user-1"))
user_repository.save(User(id_user="user-2", name="Johan", password="user-2"))


###### medicines:

medicine_01 = Medicine(
    id_medicine="0050",
    id_user="user-1",
    name_medicine="Paracetamol",
    type_medicine="Pills",
    description="Tomarlo con agua fria",
    dosage={
        "dosages_times": "2",
        "hour_dosage": "08:00",
        "days_dosage": ["Mar", "Vier"],
    },
    start_date="2022-06-15",
    end_date="2022-07-15",
)
medicine_02 = Medicine(
    id_medicine="0051",
    id_user="user-1",
    name_medicine="Bepanthol",
    type_medicine="Cream",
    description="Aplicarlo suavemente",
    dosage={
        "dosages_times": "3",
        "hour_dosage": "09:00",
        "days_dosage": ["Mar", "Juev", "Sáb"],
    },
    start_date="2022-06-01",
    end_date="2022-06-30",
)
medicine_03 = Medicine(
    id_medicine="0052",
    id_user="user-2",
    name_medicine="Ibuprofeno",
    type_medicine="Pills",
    description="Tomarlo con agua fria",
    dosage={
        "dosages_times": "3",
        "hour_dosage": "14:00",
        "days_dosage": ["Lun", "Miér", "Vier"],
    },
    start_date="2022-06-20",
    end_date="2022-07-20",
)
medicine_04 = Medicine(
    id_medicine="0053",
    id_user="user-2",
    name_medicine="Aquoral Monodosis",
    type_medicine="eye_drops",
    description="Aplicar 3 gotas",
    dosage={
        "dosages_times": "2",
        "hour_dosage": "15:00",
        "days_dosage": ["Miér", "Dom"],
    },
    start_date="2022-06-13",
    end_date="2022-06-26",
)

medicine_05 = Medicine(
    id_medicine="0054",
    id_user="user-2",
    name_medicine="Zaleplon",
    type_medicine="Pills",
    description="Ayuda a dormir, solo una pastilla",
    dosage={
        "dosages_times": "3",
        "hour_dosage": "15:00",
        "days_dosage": ["Lun", "Miér", "Vier"],
    },
    start_date="2022-06-13",
    end_date="2022-06-26",
)

medicine_repository = MedicineRepository(database_path)

medicine_repository.save(medicine_01)
medicine_repository.save(medicine_02)
medicine_repository.save(medicine_03)
medicine_repository.save(medicine_04)
medicine_repository.save(medicine_05)

print("Base de datos inicializada en " + database_path)

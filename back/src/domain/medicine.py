import sqlite3


class Medicine:
    def __init__(self, id_medicine, name_medicine, type_medicine, dosage, end_date):
        self.id_medicine = id_medicine
        self.name_medicine = name_medicine
        self.type_medicine = type_medicine
        self.dosage = dosage
        self.end_date = end_date

    def to_dict(self):
        return {
            "id_medicine": self.id_medicine,
            "name_medicine": self.name_medicine,
            "type_medicine": self.type_medicine,
            "dosage": self.dosage,
            "end_date": self.end_date,
        }


class MedicineRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE table if not exists medicines (
                id_medicine varchar PRIMARY KEY,
                name_medicine varchar,
                type_medicine varchar,
                dosage varchar,
                end_date varchar
            )"""

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """SELECT * FROM medicines"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        list_medicines = []
        for item in data:
            medicine = Medicine(
                id_medicine=item["id_medicine"],
                name_medicine=item["name_medicine"],
                type_medicine=item["type_medicine"],
                dosage=item["dosage"],
                end_date=item["end_date"],
            )
            # medicine = Medicine(**item)
            list_medicines.append(medicine)
        return list_medicines

    def get_by_id(self, id):
        sql = """SELECT * FROM medicines WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()

        medicine = Medicine(**data)
        print(medicine)
        return medicine

    def save(self, medicine):
        sql = """insert into medicines (id_medicine,name_medicine,type_medicine,dosage,end_date) 
        values(:id_medicine,:name_medicine,:type_medicine,:dosage,:end_date)
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            medicine.to_dict(),
        )
        conn.commit()

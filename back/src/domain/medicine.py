import sqlite3
import json


class Medicine:
    def __init__(
        self,
        id_medicine,
        id_user,
        name_medicine,
        type_medicine,
        description,
        dosage,
        start_date,
        end_date,
    ):
        self.id_medicine = id_medicine
        self.id_user = id_user
        self.name_medicine = name_medicine
        self.type_medicine = type_medicine
        self.description = description
        self.dosage = dosage
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self):
        return {
            "id_medicine": self.id_medicine,
            "id_user": self.id_user,
            "name_medicine": self.name_medicine,
            "type_medicine": self.type_medicine,
            "description": self.description,
            "dosage": self.dosage,
            "start_date": self.start_date,
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
                id_user varchar,
                name_medicine varchar,
                type_medicine varchar,
                description varchar,
                dosage varchar,
                start_date varchar,
                end_date varchar,
                FOREIGN KEY (id_user) REFERENCES users(id_user)
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
                id_user=item["id_user"],
                name_medicine=item["name_medicine"],
                type_medicine=item["type_medicine"],
                description=item["description"],
                dosage=json.loads(item["dosage"]),
                start_date=item["start_date"],
                end_date=item["end_date"],
            )
            # medicine = Medicine(**item)
            list_medicines.append(medicine)
        return list_medicines

    def get_by_id(self, id):
        sql = """SELECT * FROM medicines WHERE id_medicine=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        # medicine = Medicine(**data)
        medicine = Medicine(
            id_medicine=data["id_medicine"],
            id_user=data["id_user"],
            name_medicine=data["name_medicine"],
            type_medicine=data["type_medicine"],
            description=data["description"],
            dosage=json.loads(data["dosage"]),
            start_date=data["start_date"],
            end_date=data["end_date"],
        )

        return medicine

    def get_by_date(self, date):
        sql = """SELECT * FROM medicines WHERE start_date  <= :date AND :date <= end_date ORDER BY end_date DESC"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"date": date})

        data = cursor.fetchall()

        list_medicines = []
        for item in data:
            medicine = Medicine(
                id_medicine=item["id_medicine"],
                id_user=item["id_user"],
                name_medicine=item["name_medicine"],
                type_medicine=item["type_medicine"],
                description=item["description"],
                dosage=json.loads(item["dosage"]),
                start_date=item["start_date"],
                end_date=item["end_date"],
            )
            # medicine = Medicine(**item)
            list_medicines.append(medicine)
        return list_medicines

    def save(self, medicine):
        sql = """INSERT OR REPLACE INTO medicines (
            id_medicine,
            id_user,
            name_medicine,
            type_medicine,
            description,
            dosage,
            start_date,
            end_date) 
        values(
            :id_medicine,
            :id_user,
            :name_medicine,
            :type_medicine,
            :description,
            :dosage,
            :start_date,
            :end_date)
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            {
                "id_medicine": medicine.id_medicine,
                "id_user": medicine.id_user,
                "name_medicine": medicine.name_medicine,
                "type_medicine": medicine.type_medicine,
                "description": medicine.description,
                "dosage": json.dumps(medicine.dosage),
                "start_date": medicine.start_date,
                "end_date": medicine.end_date,
            },
        )
        conn.commit()

    def delete_by_id(self, id):
        sql = """DELETE FROM medicines WHERE id_medicine = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()

        cursor.execute(sql, {"id": id})

        conn.commit()
        cursor.close()

import sqlite3


class User:
    def __init__(self, id_user, name, password="NOT-PASSWORD"):
        self.id_user = id_user
        self.name = name
        self.password = password

    def to_dict(self):
        return {"id_user": self.id_user, "name": self.name}


class UserRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_table()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_table(self):
        sql = """
            create table if not exists users (
                id_user varchar primary key,
                name varchar,
                password varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        sql = """select * from users"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        users = [User(**item) for item in data]
        return users

    def get_by_id(self, id_user):
        sql = """SELECT * FROM users WHERE id_user=:id_user"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id_user": id_user})

        data = cursor.fetchone()
        if data is None:
            return None
        else:
            user = User(**data)

        return user

    def save(self, user):
        sql = """insert into users (id_user, name,password) values (
            :id_user, :name, :password
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql, {"id_user": user.id_user, "name": user.name, "password": user.password}
        )
        conn.commit()

import sqlite3

from src.webserver import create_app
from src.domain.info import InfoRepository
from src.domain.medicine import MedicineRepository


database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
    "medicines": MedicineRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")

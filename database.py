import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
DATABASE_PATH = BASE_DIR / "plants.db"
CSV_PATH = BASE_DIR / "plant_names_th.csv"


def get_connection() -> sqlite3.Connection:
    """เปิดการเชื่อมต่อ SQLite"""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    """สร้างตารางและนำเข้าข้อมูลเริ่มต้นจาก CSV หากฐานข้อมูลยังว่าง"""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_th TEXT NOT NULL UNIQUE
            )
            """
        )

        plant_count = connection.execute("SELECT COUNT(*) FROM plants").fetchone()[0]
        if plant_count == 0 and CSV_PATH.exists():
            plants = pd.read_csv(CSV_PATH)
            connection.executemany(
                "INSERT OR IGNORE INTO plants (name_th) VALUES (?)",
                [(name,) for name in plants["name_th"].dropna().astype(str)],
            )
        connection.commit()


def search_plants(keyword: str = "") -> pd.DataFrame:
    """ค้นหารายชื่อพืชด้วย parameterized query"""
    with get_connection() as connection:
        if keyword.strip():
            rows = connection.execute(
                "SELECT id, name_th FROM plants WHERE name_th LIKE ? ORDER BY name_th",
                (f"%{keyword.strip()}%",),
            ).fetchall()
        else:
            rows = connection.execute(
                "SELECT id, name_th FROM plants ORDER BY name_th"
            ).fetchall()

    return pd.DataFrame([dict(row) for row in rows])

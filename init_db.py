
from pathlib import Path
import sqlite3

BASE = Path(__file__).resolve().parent
DB_FILE = BASE / "capstone.db"
SCHEMA = BASE / "db" / "schema.sql"
SEED = BASE / "db" / "seed.sql"

def run_sql(path, conn):
    with open(path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    conn = sqlite3.connect(DB_FILE)
    try:
        run_sql(SCHEMA, conn)
        run_sql(SEED, conn)
        conn.commit()
        print("Database initialized and seeded →", DB_FILE)
    finally:
        conn.close()

if __name__ == "__main__":
    main()

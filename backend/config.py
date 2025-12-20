from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(f'La ruta base del proyecto es: {BASE_DIR}')

nombreBD = "rorro.db"
DATABASE_URL = f"sqlite:///{BASE_DIR}/{nombreBD}"
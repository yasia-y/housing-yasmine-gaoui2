from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData

app = FastAPI()

# Charger l'URL de la base de données à partir de l'environnement
import os
DATABASE_URL = os.getenv("DATABASE_URL")

# Configurer SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Housing API"}

@app.get("/houses")
def get_houses():
    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM houses")
        return [dict(row) for row in result]

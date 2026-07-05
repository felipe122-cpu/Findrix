from fastapi import FastAPI ,Depends
from typing import Annotated
from sqlmodel import SQLModel, create_engine, Session

nombre_bs = "bd_cliente.sqlite3"
DATABASE_URL = f"sqlite:///{nombre_bs}"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

def crear_bd():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
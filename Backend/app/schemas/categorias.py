from typing import Optional
from sqlmodel import SQLModel


class CategoriaCreate(SQLModel):
    nombre: str
    tipo: str


class CategoriaUpdate(SQLModel):
    nombre: Optional[str] = None
    tipo: Optional[str] = None


class CategoriaRead(SQLModel):
    id: int
    nombre: str
    tipo: str
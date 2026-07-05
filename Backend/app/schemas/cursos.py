from typing import Optional
from sqlmodel import SQLModel


class CursoCreate(SQLModel):
    titulo: str
    descripcion: str
    nivel: str


class CursoUpdate(SQLModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    nivel: Optional[str] = None


class CursoRead(SQLModel):
    id: int
    titulo: str
    descripcion: str
    nivel: str
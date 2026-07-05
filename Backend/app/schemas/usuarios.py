from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr


class UsuarioCreate(SQLModel):
    nombre: str
    apellido: str
    correo: EmailStr
    contraseña: str


class UsuarioUpdate(SQLModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    correo: Optional[EmailStr] = None
    contraseña: Optional[str] = None


class UsuarioRead(SQLModel):
    id: int
    nombre: str
    apellido: str
    correo: EmailStr
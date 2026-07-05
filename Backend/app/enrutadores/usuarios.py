from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from ..conexion_bd import get_session
from ..modelos.usuarios  import Usuario
from ..schemas.usuarios import (UsuarioCreate,UsuarioUpdate,UsuarioRead)


router_usuarios = APIRouter(prefix="/usuarios",tags=["Usuarios"])


@router_usuarios.get("/", response_model=list[UsuarioRead])
def listar_usuarios(session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios


@router_usuarios.get("/{id}", response_model=UsuarioRead)
def obtener_usuario(id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return usuario


@router_usuarios.post("/", response_model=UsuarioRead, status_code=status.HTTP_201_CREATED)
def crear_usuario(
    datos: UsuarioCreate,
    session: Session = Depends(get_session)
):
    correo = session.exec(
        select(Usuario).where(Usuario.correo == datos.correo)
    ).first()
    if correo:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El correo ya está registrado"
        )
    usuario = Usuario.model_validate(datos)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario



@router_usuarios.put("/{id}", response_model=UsuarioRead)
def actualizar_usuario( id: int, datos: UsuarioUpdate, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    if datos.correo:
        existe = session.exec(
            select(Usuario).where(Usuario.correo == datos.correo)
        ).first()
        if existe and existe.id != id:
            raise HTTPException( status_code=status.HTTP_409_CONFLICT, detail="Ese correo ya está registrado")
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(usuario, campo, valor)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@router_usuarios.delete("/{id}")
def eliminar_usuario(
    id: int,
    session: Session = Depends(get_session)):
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    session.delete(usuario)
    session.commit()
    return {
        "mensaje": "Usuario eliminado correctamente"
    }
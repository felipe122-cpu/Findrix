from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..conexion_bd import get_session
from ..modelos.metaAhorro import Meta
from ..modelos.usuarios import Usuario
from ..schemas.metaAhorro import (MetaCreate,MetaUpdate,MetaRead)

router_metasAhorro = APIRouter(prefix="/metas",tags=["Metas de ahorro"])


@router_metasAhorro.get("/", response_model=list[MetaRead])
def listar(session: Session = Depends(get_session)):
    return session.exec(select(Meta)).all()


@router_metasAhorro.get("/{id}", response_model=MetaRead)
def obtener(id: int, session: Session = Depends(get_session)):
    meta = session.get(Meta, id)
    if meta is None:
        raise HTTPException(404, "Meta no encontrada")
    return meta


@router_metasAhorro.post("/", response_model=MetaRead, status_code=status.HTTP_201_CREATED)
def crear(datos: MetaCreate,session: Session = Depends(get_session)):
    usuario = session.get(Usuario, datos.usuario_id)
    if usuario is None:
        raise HTTPException(404, "Usuario no encontrado")
    meta = Meta.model_validate(datos)
    session.add(meta)
    session.commit()
    session.refresh(meta)
    return meta


@router_metasAhorro.put("/{id}", response_model=MetaRead)
def actualizar(id: int,datos: MetaUpdate,session: Session = Depends(get_session)):
    meta = session.get(Meta, id)
    if meta is None:
        raise HTTPException(404, "Meta no encontrada")
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(meta, campo, valor)
    session.add(meta)
    session.commit()
    session.refresh(meta)
    return meta


@router_metasAhorro.delete("/{id}")
def eliminar(id: int,session: Session = Depends(get_session)):
    meta = session.get(Meta, id)
    if meta is None:
        raise HTTPException(404, "Meta no encontrada")
    session.delete(meta)
    session.commit()
    return {"mensaje": "Meta eliminada correctamente"}
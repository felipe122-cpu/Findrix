from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..conexion_bd import get_session
from ..modelos.categorias import Categoria
from ..schemas.categorias import (CategoriaCreate,CategoriaUpdate,CategoriaRead)

router_categorias = APIRouter(prefix="/categorias",tags=["Categorías"])


@router_categorias.get("/", response_model=list[CategoriaRead])
def listar_categorias(session: Session = Depends(get_session)):
    return session.exec(select(Categoria)).all()


@router_categorias.get("/{id}", response_model=CategoriaRead)
def obtener_categoria(id: int, session: Session = Depends(get_session)):
    categoria = session.get(Categoria, id)
    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )
    return categoria


@router_categorias.post("/", response_model=CategoriaRead, status_code=201)
def crear_categoria(
    datos: CategoriaCreate,
    session: Session = Depends(get_session)
):
    existe = session.exec(
        select(Categoria).where(Categoria.nombre == datos.nombre)
    ).first()
    if existe:
        raise HTTPException(
            status_code=409,
            detail="La categoría ya existe"
        )
    categoria = Categoria.model_validate(datos)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


@router_categorias.put("/{id}", response_model=CategoriaRead)
def actualizar_categoria(
    id: int,
    datos: CategoriaUpdate,
    session: Session = Depends(get_session)
):
    categoria = session.get(Categoria, id)
    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(categoria, campo, valor)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


@router_categorias.delete("/{id}")
def eliminar_categoria(id: int, session: Session = Depends(get_session)):
    categoria = session.get(Categoria, id)
    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )
    session.delete(categoria)
    session.commit()
    return {
        "mensaje": "Categoría eliminada correctamente"
    }
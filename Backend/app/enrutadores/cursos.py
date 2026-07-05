from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..conexion_bd import get_session
from ..modelos.cursos import Curso
from ..schemas.cursos import (CursoCreate,CursoUpdate,CursoRead)

router_cursos = APIRouter(prefix="/cursos",tags=["Cursos"])


@router_cursos.get("/", response_model=list[CursoRead])
def listar(session: Session = Depends(get_session)):
    return session.exec(select(Curso)).all()


@router_cursos.get("/{id}", response_model=CursoRead)
def obtener(id: int, session: Session = Depends(get_session)):
    curso = session.get(Curso, id)
    if curso is None:
        raise HTTPException(status_code=404,detail="Curso no encontrado")
    return curso


@router_cursos.post("/", response_model=CursoRead, status_code=status.HTTP_201_CREATED)
def crear(datos: CursoCreate,session: Session = Depends(get_session)):
    curso = Curso.model_validate(datos)
    session.add(curso)
    session.commit()
    session.refresh(curso)
    return curso


@router_cursos.put("/{id}", response_model=CursoRead)
def actualizar(id: int,datos: CursoUpdate,session: Session = Depends(get_session)):
    curso = session.get(Curso, id)
    if curso is None:
        raise HTTPException(status_code=404,detail="Curso no encontrado")
    cambios = datos.model_dump(exclude_unset=True)
    for campo, valor in cambios.items():
        setattr(curso, campo, valor)
    session.add(curso)
    session.commit()
    session.refresh(curso)
    return curso


@router_cursos.delete("/{id}")
def eliminar(id: int,session: Session = Depends(get_session)):
    curso = session.get(Curso, id)
    if curso is None:
        raise HTTPException(status_code=404,detail="Curso no encontrado")
    session.delete(curso)
    session.commit()
    return {"mensaje": "Curso eliminado correctamente"}
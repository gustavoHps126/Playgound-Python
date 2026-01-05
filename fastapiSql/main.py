from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

#Cria as tabelas no PostgresSql(Caso não existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/',response_model=schemas.EstudanteResponse)

def create_student(student: schemas.EstudanteCreate,db: Session = Depends(getDb)):
    db_student = models.Estudante(**student.model_dunp())
 #   Estudante(nome='Rodrigo', idade = 38)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get('/estudantes/', response_model= List(schemas.EstudanteResponse))
def readStudents(db: Session = Depends(getDb)):
    students = db.query(models.Estudante).all()
    return students

@app.post('/matriculas/',response_model=schemas.MatriculaBase)

def create_matriculas(student: schemas.MatriculaCreate,db: Session = Depends(getDb)):
    db_matriculas = models.Matricula(**matricula.model_dunp())
 #   Estudante(nome='Rodrigo', idade = 38)
    db.add(db_matriculas)
    db.commit()
    db.refresh(db_matriculas)
    return db_matriculas

@app.get('/matriculas/', response_model= List(schemas.MatriculaBase))
def readMatricula(db: Session = Depends(getDb)):
    matricula = db.query(models.Matricula).all()
    return matricula



from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Создаем сессию
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    database.init_db()

@app.get("/terms/", response_model=list[schemas.Term])
def get_terms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_terms(db, skip, limit)

@app.get("/terms/{term_name}", response_model=schemas.Term)
def get_term(term_name: str, db: Session = Depends(get_db)):
    db_term = crud.get_term(db, term_name)
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term

@app.post("/terms/", response_model=schemas.Term)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    return crud.create_term(db, term)

@app.put("/terms/{term_name}", response_model=schemas.Term)
def update_term(term_name: str, term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = crud.update_term(db, term_name, term)
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term

@app.delete("/terms/{term_name}", response_model=schemas.Term)
def delete_term(term_name: str, db: Session = Depends(get_db)):
    db_term = crud.delete_term(db, term_name)
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term

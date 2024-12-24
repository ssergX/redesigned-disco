from sqlalchemy.orm import Session
from . import models, schemas

def get_terms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Term).offset(skip).limit(limit).all()

def get_term(db: Session, term_name: str):
    return db.query(models.Term).filter(models.Term.term == term_name).first()

def create_term(db: Session, term: schemas.TermCreate):
    db_term = models.Term(term=term.term, description=term.description)
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

def update_term(db: Session, term_name: str, term: schemas.TermCreate):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term:
        db_term.term = term.term
        db_term.description = term.description
        db.commit()
        db.refresh(db_term)
        return db_term
    return None

def delete_term(db: Session, term_name: str):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term:
        db.delete(db_term)
        db.commit()
        return db_term
    return None

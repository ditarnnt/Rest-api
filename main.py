from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List 

from .import crud, models, schemas
from .database import SessionLocal, engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close ()

@app.post("/employee/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeBase, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee = employee)
    # if db_employee:
    #     raise HTTPException(status_code=400, detail="already registered")
    # return db_employee

@app.get("/employees/{employee_id}", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_employee = crud.get_employees(db, skip=skip, limit=limit)
    return db_employee

@app.get("/employee/{employee_id}", response_model=schemas.Employee)
def read_employee_id(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id = employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_employee


@app.put("/employee/{employee_id}", response_model=schemas.Employee)
def update_employee(employee: schemas.Employee, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee.employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_employee(db=db, employee=employee)
from sqlalchemy.orm import Session 
from . import models, schemas

def get_employee (db: Session, employee_id: int):
    return db.query(models.Employee). filter (models.Employee.employee_id == employee_id).first()

def get_employees (db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

# def get_employee_name(db: Session, name:schemas.EmployeeBase.name):
#     return db.query(models.Employee). filter (models.Employee.name == name)

# def get_employee_birthdate(db: Session, birthdate:str):
#     return db.query(models.Employee). filter (models.Employee.birthdate == birthdate)

# def get_employee_address(db: Session, address:str):
#     return db.query(models.Employee). filter (models.Employee.address == address)

# def create_employee (db: Session, employee:schemas.EmployeeBase):
#     db_employee = models.Employee(**employee.dict())
#     db.add(db_employee)
#     db.commit()
#     db.refresh(db_employee)
#     return db_employee


def create_employee(db: Session, employee: schemas.EmployeeBase):
    db_employee = models.Employee(name=employee.name, address=employee.address, birthdate=employee.birthdate)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee: schemas.Employee):
    update = {
        models.Employee.name: employee.name,
        models.Employee.address: employee.address,
        models.Employee.birthdate: employee.birthdate
    }
    db_employee = models.Employee(employee_id = employee.employee_id, name=employee.name, address=employee.address, birthdate=employee.birthdate)
    db.query(models.Employee).filter(models.Employee.employee_id == employee.employee_id).update(update)
    db.commit()
    # db.refresh(db_employee)
    return db_employee
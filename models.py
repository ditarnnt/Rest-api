from sqlalchemy import Column, Integer, String, Date
# from sqlalchemy.orm import relationship

from .database import Base

class Employee(Base): 
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable= False)
    birthdate= Column(Date, nullable= False)


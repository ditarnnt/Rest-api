from pydantic import BaseModel, Field
from datetime import date

class EmployeeBase(BaseModel):
    name : str = Field(min_length=1)
    address: str = Field(min_length=1)
    birthdate : date 

class Employee(EmployeeBase):
    employee_id : int
    class Config:
        orm_mode = True 
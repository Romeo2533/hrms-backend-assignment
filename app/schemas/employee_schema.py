from pydantic import BaseModel # type: ignore
from pydantic import EmailStr # type: ignore

from datetime import date

from typing import Optional


class EmployeeCreate(BaseModel):

    name: str

    email: EmailStr

    department: str

    designation: str

    joining_date: date

    base_salary: float

    salary_type: str


class EmployeeUpdate(BaseModel):

    name: Optional[str] = None

    department: Optional[str] = None

    designation: Optional[str] = None

    base_salary: Optional[float] = None

    salary_type: Optional[str] = None
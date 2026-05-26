from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import Boolean

from app.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        String,
        unique=True,
        nullable=False
    )

    name = Column(String, nullable=False)

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    department = Column(String)

    designation = Column(String)

    joining_date = Column(Date)

    base_salary = Column(Float)

    salary_type = Column(String)

    is_active = Column(
        Boolean,
        default=True
    )
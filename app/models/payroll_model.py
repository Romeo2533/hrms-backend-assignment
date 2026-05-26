from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database import Base


class Payroll(Base):

    __tablename__ = "payroll"

    id = Column(Integer, primary_key=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    month = Column(String)

    working_days = Column(Integer)

    present_days = Column(Integer)

    late_marks = Column(Integer)

    overtime_hours = Column(Float)

    bonuses = Column(Float, default=0)

    deductions = Column(Float, default=0)

    final_salary = Column(Float)
from sqlalchemy import Column # type: ignore
from sqlalchemy import Integer # type: ignore
from sqlalchemy import String # type: ignore
from sqlalchemy import Float # type: ignore
from sqlalchemy import ForeignKey # type: ignore

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
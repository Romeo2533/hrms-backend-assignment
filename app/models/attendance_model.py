from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from app.database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )

    attendance_date = Column(Date)

    check_in = Column(DateTime)

    check_out = Column(DateTime)

    working_hours = Column(Float, default=0)

    is_late = Column(Boolean, default=False)

    is_half_day = Column(Boolean, default=False)

    overtime_hours = Column(Float, default=0)
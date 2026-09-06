from sqlalchemy import Column # type: ignore
from sqlalchemy import Integer # type: ignore
from sqlalchemy import Date # type: ignore
from sqlalchemy import DateTime # type: ignore
from sqlalchemy import Float # type: ignore
from sqlalchemy import Boolean # type: ignore
from sqlalchemy import ForeignKey # type: ignore

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
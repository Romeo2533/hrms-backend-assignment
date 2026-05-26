from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from datetime import datetime
from datetime import date
from datetime import time

from app.dependencies import get_db

from app.models.attendance_model import Attendance
from app.models.employee_model import Employee

from app.auth.oauth2 import get_current_user
from app.auth.rbac import role_required


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.post("/check-in")
def check_in(
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(
            ["employee", "hr", "admin"]
        )
    )
):

    employee = db.query(Employee).filter(
        Employee.email == current_user.email
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee record not found"
        )

    today = date.today()

    current_time = datetime.now()

    existing_attendance = db.query(Attendance).filter(
        Attendance.employee_id == employee.id,
        Attendance.attendance_date == today
    ).first()

    if existing_attendance:

        raise HTTPException(
            status_code=400,
            detail="Already checked in today"
        )

    office_late_time = time(10, 15)

    is_late = current_time.time() > office_late_time

    new_attendance = Attendance(
        employee_id=employee.id,
        attendance_date=today,
        check_in=current_time,
        is_late=is_late
    )

    db.add(new_attendance)

    db.commit()

    return {
        "message": "Check-in successful",
        "late": is_late
    }

@router.post("/check-out")
def check_out(
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(
            ["employee", "hr", "admin"]
        )
    )
):

    employee = db.query(Employee).filter(
        Employee.email == current_user.email
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee record not found"
        )

    today = date.today()

    attendance = db.query(Attendance).filter(
        Attendance.employee_id == employee.id,
        Attendance.attendance_date == today
    ).first()

    if not attendance:

        raise HTTPException(
            status_code=400,
            detail="Check-in not found"
        )

    if attendance.check_out is not None:

        raise HTTPException(
            status_code=400,
            detail="Already checked out"
        )

    current_time = datetime.now()

    attendance.check_out = current_time

    total_seconds = (
        attendance.check_out -
        attendance.check_in
    ).total_seconds()

    working_hours = round(
        total_seconds / 3600,
        2
    )

    attendance.working_hours = working_hours

    attendance.is_half_day = (
        working_hours < 4
    )

    attendance.overtime_hours = max(
        0,
        working_hours - 8
    )

    db.commit()

    return {
        "message": "Check-out successful",
        "working_hours": working_hours,
        "half_day": attendance.is_half_day,
        "overtime_hours": attendance.overtime_hours
    }

@router.get("/my-history")
def my_attendance_history(
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(
            ["employee", "hr", "admin"]
        )
    )
):

    employee = db.query(Employee).filter(
        Employee.email == current_user.email
    ).first()

    attendance_records = db.query(Attendance).filter(
        Attendance.employee_id == employee.id
    ).all()

    return attendance_records

@router.get("/reports")
def attendance_reports(
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(["admin", "hr"])
    )
):

    reports = db.query(Attendance).all()

    return reports

@router.get("/monthly-summary")
def monthly_summary(
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(["admin", "hr"])
    )
):

    attendance = db.query(Attendance).all()

    total_present = len(attendance)

    total_late = len([
        a for a in attendance if a.is_late
    ])

    total_half_day = len([
        a for a in attendance if a.is_half_day
    ])

    total_overtime = sum([
        a.overtime_hours for a in attendance
    ])

    return {
        "total_present": total_present,
        "late_marks": total_late,
        "half_days": total_half_day,
        "overtime_hours": total_overtime
    }
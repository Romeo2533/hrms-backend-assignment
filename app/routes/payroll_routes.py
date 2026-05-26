from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.employee_model import Employee
from app.models.attendance_model import Attendance
from app.models.payroll_model import Payroll
from app.services.pdf_service import generate_payslip_pdf

from app.schemas.payroll_schema import PayrollGenerate

from app.auth.rbac import role_required


router = APIRouter(
    prefix="/payroll",
    tags=["Payroll"]
)

@router.post("/generate")
def generate_payroll(
    payroll_data: PayrollGenerate,
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(["admin", "hr"])
    )
):

    employee = db.query(Employee).filter(
        Employee.id == payroll_data.employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    existing_payroll = db.query(Payroll).filter(
        Payroll.employee_id == employee.id,
        Payroll.month == payroll_data.month
    ).first()

    if existing_payroll:

        raise HTTPException(
            status_code=400,
            detail="Payroll already generated"
        )

    attendance_records = db.query(Attendance).filter(
        Attendance.employee_id == employee.id
    ).all()

    present_days = len(attendance_records)

    late_marks = len([
        a for a in attendance_records
        if a.is_late
    ])

    overtime_hours = sum([
        a.overtime_hours
        for a in attendance_records
    ])

    working_days = 26

    leave_count = working_days - present_days

    late_deduction = late_marks * 100

    leave_deduction = leave_count * 500

    overtime_amount = overtime_hours * 200

    total_deductions = (
        late_deduction +
        leave_deduction
    )

    final_salary = (
        employee.base_salary
        - total_deductions
        + overtime_amount
        + payroll_data.bonuses
    )

    if final_salary < 0:

        raise HTTPException(
            status_code=400,
            detail="Negative salary invalid"
        )

    payroll = Payroll(
        employee_id=employee.id,
        month=payroll_data.month,
        working_days=working_days,
        present_days=present_days,
        late_marks=late_marks,
        overtime_hours=overtime_hours,
        bonuses=payroll_data.bonuses,
        deductions=total_deductions,
        final_salary=final_salary
    )

    db.add(payroll)

    db.commit()

    return {
        "employee": employee.name,
        "month": payroll.month,
        "working_days": payroll.working_days,
        "present_days": payroll.present_days,
        "late_marks": payroll.late_marks,
        "overtime_hours": payroll.overtime_hours,
        "deductions": payroll.deductions,
        "final_salary": payroll.final_salary
    }

@router.get("/history")
def payroll_history(
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(["admin", "hr"])
    )
):

    payrolls = db.query(Payroll).all()

    return payrolls

@router.get("/payslip/{payroll_id}")
def download_payslip(
    payroll_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(
        role_required(["admin", "hr"])
    )
):

    payroll = db.query(Payroll).filter(
        Payroll.id == payroll_id
    ).first()

    if not payroll:

        raise HTTPException(
            status_code=404,
            detail="Payroll not found"
        )

    employee = db.query(Employee).filter(
        Employee.id == payroll.employee_id
    ).first()

    file_path = (
        f"payslip_{payroll.id}.pdf"
    )

    generate_payslip_pdf(
        file_path,
        payroll,
        employee
    )

    return FileResponse(
        path=file_path,
        filename=file_path,
        media_type="application/pdf"
    )
from reportlab.pdfgen import canvas # type: ignore



def generate_payslip_pdf(
    file_path,
    payroll,
    employee
):

    pdf = canvas.Canvas(file_path)

    pdf.setTitle("Payslip")

    pdf.drawString(
        200,
        800,
        "HRMS PAYSLIP"
    )

    pdf.drawString(
        50,
        760,
        f"Employee: {employee.name}"
    )

    pdf.drawString(
        50,
        740,
        f"Department: {employee.department}"
    )

    pdf.drawString(
        50,
        720,
        f"Month: {payroll.month}"
    )

    pdf.drawString(
        50,
        700,
        f"Present Days: {payroll.present_days}"
    )

    pdf.drawString(
        50,
        680,
        f"Late Marks: {payroll.late_marks}"
    )

    pdf.drawString(
        50,
        660,
        f"Overtime Hours: {payroll.overtime_hours}"
    )

    pdf.drawString(
        50,
        640,
        f"Deductions: {payroll.deductions}"
    )

    pdf.drawString(
        50,
        620,
        f"Final Salary: {payroll.final_salary}"
    )

    pdf.save()
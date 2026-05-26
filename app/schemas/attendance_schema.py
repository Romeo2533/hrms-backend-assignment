from pydantic import BaseModel


class AttendanceCorrection(BaseModel):

    check_in: str

    check_out: str
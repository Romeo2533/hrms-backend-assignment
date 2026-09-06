from pydantic import BaseModel # type: ignore


class AttendanceCorrection(BaseModel):

    check_in: str

    check_out: str
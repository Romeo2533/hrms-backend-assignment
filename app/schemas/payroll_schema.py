from pydantic import BaseModel


class PayrollGenerate(BaseModel):

    employee_id: int

    month: str

    bonuses: float = 0
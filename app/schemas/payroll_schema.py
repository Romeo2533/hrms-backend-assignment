from pydantic import BaseModel # type: ignore


class PayrollGenerate(BaseModel):

    employee_id: int

    month: str

    bonuses: float = 0
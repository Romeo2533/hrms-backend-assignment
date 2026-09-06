from fastapi import APIRouter # type: ignore
from fastapi import Depends # type: ignore

from app.auth.rbac import role_required

router = APIRouter(
    prefix="/test",
    tags=["RBAC Testing"]
)


@router.get("/admin")
def admin_route(
    current_user = Depends(
        role_required(["admin"])
    )
):

    return {
        "message": "Welcome Admin"
    }


@router.get("/hr")
def hr_route(
    current_user = Depends(
        role_required(["admin", "hr"])
    )
):

    return {
        "message": "Welcome HR/Admin"
    }


@router.get("/employee")
def employee_route(
    current_user = Depends(
        role_required(
            ["admin", "hr", "employee"]
        )
    )
):

    return {
        "message": "Welcome Employee"
    }
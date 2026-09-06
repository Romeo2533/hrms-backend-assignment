from pydantic import BaseModel, EmailStr, Field # type: ignore


class UserRegister(BaseModel):

    name: str

    email: EmailStr

    password: str = Field(
    min_length=6
    )

    role: str


class UserLogin(BaseModel):

    username: EmailStr

    password: str = Field(
    min_length=6
    )
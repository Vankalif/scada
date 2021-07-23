from pydantic import BaseModel


class Param(BaseModel):
    table_name: str
    well_id: int
    value: float


class User(BaseModel):
    name: str
    surname: str
    patronymic: str
    login: str
    password: str

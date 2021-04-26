from pydantic import BaseModel


class Param(BaseModel):
    table_name: str
    well_id: int
    value: float

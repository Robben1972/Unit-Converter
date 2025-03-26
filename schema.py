from pydantic import BaseModel

class UnitRequest(BaseModel):
    from_unit: str
    value: float
    to_unit: str

class UnitResponse(BaseModel):
    value: float
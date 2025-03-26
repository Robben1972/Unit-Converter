from fastapi import APIRouter
from schema import UnitRequest, UnitResponse

router = APIRouter()

@router.post("/temperature/", response_model=UnitResponse)
async def temperature(request: UnitRequest):
    celsius: int = 0
    match request.from_unit:
        case "kelvin":
            celsius = request.value - 273.15
        case "fahrenheit":
            celsius = (request.value - 32) * 5 / 9
        case "celsius":
            celsius = request.value
        case _:
            return {"detail": f"Unsupported from unit: {request.from_unit}"}
    match request.to_unit:
        case "kelvin":
            return {"value": celsius + 273.15}
        case "fahrenheit":
            return {"value": celsius * 9 / 5 + 32}
        case "celsius":
            return {"value": celsius}
        case _:
            return {"detail": f"Unsupported to unit: {request.to_unit}"}
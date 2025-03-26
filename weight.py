from fastapi import APIRouter
from schema import UnitRequest, UnitResponse

router = APIRouter()

@router.post("/weight/", response_model=UnitResponse)
async def weight(request: UnitRequest):
    pound: int = 0
    match request.from_unit:
        case "milligram":
            pound = request.value / 453592
        case "kilogram":
            pound = request.value * 2.20462
        case "gram":
            pound = request.value / 453.592
        case "ounce":
            pound = request.value / 16
        case "pound":
            pound = request.value
        case _:
            return {"detail": f"Unsupported from unit: {request.from_unit}"}
    match request.to_unit:
        case "milligram":
            return {"value": pound * 453592}
        case "kilogram":
            return {"value": pound / 2.20462}
        case "gram":
            return {"value": pound * 453.592}
        case "ounce":
            return {"value": pound * 16}
        case "pound":
            return {"value": pound}
        case _:
            return {"detail": f"Unsupported to unit: {request.to_unit}"}
    
    
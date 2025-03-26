from fastapi import APIRouter
from schema import UnitRequest, UnitResponse

router = APIRouter()

@router.post("/length/", response_model=UnitResponse)
async def length(request: UnitRequest):
    mile: int = 0
    match request.from_unit:
        case "millimeter":
            mile = request.value / 1609344
        case "centimeter":
            mile = request.value / 160934.4
        case "meter":
            mile = request.value / 1609.344
        case "kilometer":
            mile = request.value / 1.609344
        case "inch":
            mile = request.value / 63360
        case "foot":
            mile = request.value / 5280
        case "yard":
            mile = request.value / 1760
        case "mile":
            mile = request.value
        case _:
            return {"detail": f"Unsupported from unit: {request.from_unit}"}
    match request.to_unit:
        case "millimeter":
            return {"value": mile * 1609344}
        case "centimeter":
            return {"value": mile * 160934.4}
        case "meter":
            return {"value": mile * 1609.344}
        case "kilometer":
            return {"value": mile * 1.609344}
        case "inch":
            return {"value": mile * 63360}
        case "foot":
            return {"value": mile * 5280}
        case "yard":
            return {"value": mile * 1760}
        case "mile":
            return {"value": mile}
        case _:
            return {"detail": f"Unsupported to unit: {request.to_unit}"}
    
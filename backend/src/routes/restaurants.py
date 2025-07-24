from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/restaurants")
def read_restaurants():
    return {"message": "Restaurants route"}
from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/auth")
def read_auth():
    return {"message": "Auth route"}
from pydantic import BaseModel, Field


class RestaurantSchema(BaseModel):
    id: int
    name: str
    address: str
    rating: float | None = Field(default=None, ge=0, le=5)
    description: str | None
    location: str | None

    class Config:
        orm_mode = True


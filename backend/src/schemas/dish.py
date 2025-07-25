from pydantic import BaseModel, Field

class DishSchema(BaseModel):
    id: int
    name: str
    price: float
    rating: float | None = Field(default=None, ge=0, le=5)
    description: str | None
    restaurant_id: int
    

    class Config:
        orm_mode = True

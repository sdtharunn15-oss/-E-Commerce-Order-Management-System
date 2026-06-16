from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str
    category: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float
    stock: int
    is_active: bool

    class Config:
        from_attributes = True
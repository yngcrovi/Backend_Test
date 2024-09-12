from pydantic import BaseModel

class ProductGetDTO(BaseModel):
    name_product: str
    type_product: str
    calories: int
    protein: float
    fat: float
    carbohydrates: float
    price: int
    
class ProductIdDTO(BaseModel):
    id: int

class ProductGetWithIdDTO(ProductGetDTO):
    id: int
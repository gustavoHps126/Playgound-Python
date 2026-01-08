from pydantic import BaseModel

class Category(BaseModel):
    nome: str
    idcategory: int
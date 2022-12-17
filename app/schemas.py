from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True

class  Item(BaseModel):
    id: int
    title: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        orm_mode = True


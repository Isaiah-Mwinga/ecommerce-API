from pydantic import BaseModel

class User(BaseModel):
    username: str
    hashed_password: str
    is_active: bool = True

    class Config:
        orm_mode = True

class  Item(BaseModel):
    title: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        orm_mode = True

from pydantic import BaseModel



class User(BaseModel):
    id: int
    username: str
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    price: float

    class Config:
        orm_mode = True


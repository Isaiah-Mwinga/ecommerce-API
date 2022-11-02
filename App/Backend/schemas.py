from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    hashed_password: str
    is_active: bool

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    price: float

    
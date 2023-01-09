from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True


class categories(BaseModel):
    id: int
    name: str
    description: str = None

    class Config:
        orm_mode = True

class Computing(BaseModel):
            id: int
            name: str
            description: str = None

            class Config:
                orm_mode = True

class Laptops(BaseModel):
                id: int
                name: str
                description: str = None

                class Config:
                    orm_mode = True

class Computers(BaseModel):
                id: int
                name: str
                description: str = None

                class Config:
                    orm_mode = True


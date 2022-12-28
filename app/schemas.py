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

class categories(BaseModel):
    id: int
    name: str
    description: str = None

    class Config:
        orm_mode = True

        class Computing(categories):
            id: int
            name: str
            description: str = None

            class Config:
                orm_mode = True

            class Laptops(Computing):
                id: int
                name: str
                description: str = None

                class Config:
                    orm_mode = True

            class Computers(Computing):
                id: int
                name: str
                description: str = None

                class Config:
                    orm_mode = True

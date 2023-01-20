from pydantic import BaseModel

class Computing(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Laptops(Computing):
    brand: str
    model: str
    price: int
    quantity: int
    description: str
    image: str

class Desktops(Computing):
    brand: str
    model: str
    price: int
    quantity: int
    description: str
    image: str

class Datastorage(Computing):
    brand: str
    model: str
    price: int
    quantity: int
    description: str
    image: str

class Monitors(Computing):
    brand: str
    model: str
    price: int
    quantity: int
    description: str
    image: str

class Printers(Computing):
    brand: str
    model: str
    price: int
    quantity: int
    description: str
    image: str


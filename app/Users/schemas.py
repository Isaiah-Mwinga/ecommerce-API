from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str

class UserInDB(User):
    hashed_password: str
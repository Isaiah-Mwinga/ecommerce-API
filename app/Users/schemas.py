from pydantic import BaseModel


class User(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None

class UserInDB(User):
    hashed_password: str
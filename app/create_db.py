from app.database import Base, engine
from app.models import User, Item


Base.metadata.create_all(bind=engine)
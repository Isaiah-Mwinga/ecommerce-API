from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    price = Column(float)

    owner = relationship("User", back_populates="items")    

class categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Item", back_populates="categories")

class computing(categories):
    __tablename__ = "computing"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(float)

    owner = relationship("Item", back_populates="computing")

    class Laptops(computing):
        __tablename__ = "Laptops"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        price = Column(float)

        owner = relationship("Item", back_populates="Laptops")

        class Macbook(Laptops):
            __tablename__ = "Macbook"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            price = Column(float)

            owner = relationship("Item", back_populates="Macbook")

        class Windows(Laptops):
            __tablename__ = "Windows"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            price = Column(float)

            owner = relationship("Item", back_populates="Windows")

    class Desktops(computing):
        __tablename__ = "Desktops"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        price = Column(float)

        owner = relationship("Item", back_populates="Desktops")

        class Macbook(Desktops):
            __tablename__ = "Macbook"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            price = Column(float)

            owner = relationship("Item", back_populates="Macbook")

        class Windows(Desktops):
            __tablename__ = "Windows"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            price = Column(float)

            owner = relationship("Item", back_populates="Windows")

    class Tablets(computing):
        __tablename__ = "Tablets"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        price = Column(float)

        owner = relationship("Item", back_populates="Tablets")

        class Apple(Tablets):
            __tablename__ = "Apple"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            price = Column(float)

            owner = relationship("Item", back_populates="Apple")

        class Android(Tablets):
            __tablename__ = "Android"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            price = Column(float)

            owner = relationship("Item", back_populates="Android")

    class Phones(computing):
        __tablename__ = "Phones"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Phones")

        class Apple(Phones):
            __tablename__ = "Apple"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Apple")

        class Android(Phones):
            __tablename__ = "Android"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Android")

    class Accessories(computing):
        __tablename__ = "Accessories"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Accessories")

        class Apple(Accessories):
            __tablename__ = "Apple"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Apple")

        class Android(Accessories):
            __tablename__ = "Android"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Android")

    class Software(computing):
        __tablename__ = "Software"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Software")

        class Apple(Software):
            __tablename__ = "Apple"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Apple")

        class Android(Software):
            __tablename__ = "Android"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Android")


class electronics(categories):
    __tablename__ = "electronics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Item", back_populates="electronics")

    class Cameras(electronics):
        __tablename__ = "Cameras"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Cameras")

        class Digital(Cameras):
            __tablename__ = "Digital"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Digital")

        class Film(Cameras):
            __tablename__ = "Film"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Film")

    class Audio(electronics):
        __tablename__ = "Audio"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Audio")

        class Headphones(Audio):
            __tablename__ = "Headphones"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Headphones")

        class Speakers(Audio):
            __tablename__ = "Speakers"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Speakers")

        class Microphones(Audio):
            __tablename__ = "Microphones"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Microphones")

    class Video(electronics):
        __tablename__ = "Video"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Video")

        class Televisions(Video):
            __tablename__ = "Televisions"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Televisions")

        class Projectors(Video):
            __tablename__ = "Projectors"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Projectors")

        class Monitors(Video):
            __tablename__ = "Monitors"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Monitors")

    class Accessories (electronics):
        __tablename__ = "Accessories"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="Accessories")

        class Apple(Accessories):
            __tablename__ = "Apple"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Apple")

        class Android(Accessories):
            __tablename__ = "Android"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Android")



    class Gaming(categories):
        __tablename__ = "gaming"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="gaming")

        class Consoles(Gaming):
            __tablename__ = "Consoles"
            id = Column(Integer, primary_key=True, index=True)
            name = Column(String, index=True)
            description = Column(String, index=True)
            owner_id = Column(Integer, ForeignKey("users.id"))

            owner = relationship("Item", back_populates="Consoles")

            class Nintendo(Consoles):
                __tablename__ = "Nintendo"
                id = Column(Integer, primary_key=True, index=True)
                name = Column(String, index=True)
                description = Column(String, index=True)
                owner_id = Column(Integer, ForeignKey("users.id"))

                owner = relationship("Item", back_populates="Nintendo")

            class Sony(Consoles):
                __tablename__ = "Sony"
                id = Column(Integer, primary_key=True, index=True)
                name = Column(String, index=True)
                description = Column(String, index=True)
                owner_id = Column(Integer, ForeignKey("users.id"))

                owner = relationship("Item", back_populates="Sony")

            class Microsoft(Consoles):
                __tablename__ = "Microsoft"
                id = Column(Integer, primary_key=True, index=True)
                name = Column(String, index=True)
                description = Column(String, index=True)
                owner_id = Column(Integer, ForeignKey("users.id"))

                owner = relationship("Item", back_populates="Microsoft")

    class Mobile(categories):
        __tablename__ = "mobile"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String, index=True)
        owner_id = Column(Integer, ForeignKey("users.id"))

        owner = relationship("Item", back_populates="mobile")

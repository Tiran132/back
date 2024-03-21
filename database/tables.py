from sqlalchemy import (ForeignKey)
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
     pass

class Photo(Base):
    __tablename__ = 'photo'

    id: Mapped[int] = mapped_column(primary_key=True)
    photo_name: Mapped[str] = mapped_column(unique=True)
    photo_url: Mapped[str] = mapped_column(unique=True)
    encodings: Mapped[bytes] = mapped_column(unique=True)

# class EncodePhoto(Base):
#     __tablename__ = 'encoded_photo'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     photo_id: Mapped[int] = mapped_column(ForeignKey("photo.id"))
#     encodings: Mapped[bytes] = mapped_column(unique=True)

class Person(Base):
    __tablename__ = 'person'

    id: Mapped[int] = mapped_column(primary_key=True)
    fio: Mapped[str] = mapped_column(unique=True)
    photo_url: Mapped[str] = mapped_column(unique=True)
    encodings: Mapped[bytes] = mapped_column(unique=True)

# class EncodedPerson(Base):
#     __tablename__ = 'encoded_person'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
#     encodings: Mapped[bytes] = mapped_column(unique=True)
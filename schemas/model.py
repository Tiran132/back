from pydantic import BaseModel


class PhotoModel(BaseModel):
    id: int
    photo_name: str
    photo_url: str

class PersonModel(BaseModel):
    id: int
    fio: str
    photo_url: str

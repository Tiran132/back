from fastapi import APIRouter, UploadFile, Depends
from typing import List
from schemas.model import PhotoModel, PersonModel
from services.logic import PersonService

router = APIRouter(
    tags=['PersonAPI'],
    )

@router.get('/person', response_model=List[PhotoModel])
def get_photos_by_fio(
    fio: str,
    person_service: PersonService = Depends()
):
    return person_service.get_photos_by_fio(fio)

@router.get('/persons', response_model=List[PersonModel])
def get_persons(
    person_service: PersonService = Depends()
):
    return person_service.get_persons()

@router.post('/person', status_code=201)
def add_person(
    fio: str,
    file: List[UploadFile],
    photo_service: PersonService = Depends()
):
    return photo_service.add_person(fio, file)

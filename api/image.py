from fastapi import APIRouter, UploadFile, Depends
from typing import List
from schemas.model import PhotoModel
from services.logic import PhotoService

router = APIRouter(
    tags=['GalleryAPI'],
    )


@router.get('/', response_model=List[PhotoModel])
def get_photos(
    photo_service: PhotoService = Depends()
):
    return photo_service.get_photos()

@router.post('/photos', status_code=201)
def add_photos(
    file: List[UploadFile],
    photo_service: PhotoService = Depends()
):
    return photo_service.add_photo(file)

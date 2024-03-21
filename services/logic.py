from fastapi import Depends, UploadFile, HTTPException
from database import tables
from database.db import get_session
from typing import List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
from .face_recognize import encoded_faces, encoded_face, compare_faces

from sqlalchemy.orm import Session

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-2a224-default-rtdb.firebaseio.com/",
    'storageBucket': "face-2a224.appspot.com"
})

class PhotoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_photos(self) -> List[tables.Photo]:
        query = (
            self.session
            .query(tables.Photo)
        )
        photos = query.all()
        return photos

    def add_photo(self, files: List[UploadFile]):
        folderPath = 'gallery'
        for file in files:
            if file.content_type not in ['image/jpeg', 'image/png']:
                raise HTTPException(status_code=400, 
                                    detail="Invalid file type. Only JPEG and PNG images are allowed.")
    
            fileName = f'{folderPath}/{file.filename}'
            bucket = storage.bucket()
            blob = bucket.blob(fileName)
            blob.upload_from_file(file.file, content_type=file.content_type)
            # uploaded_file_url = f"https://firebasestorage.googleapis.com/v0/b/face-2a224.appspot.com/o/dataset%2F{file.filename}?alt=media&token=084aec27-c56e-4af9-9c82-6d31dd73e27b"
            uploaded_file_url = blob.public_url
            binary = encoded_face(file)
            photo = tables.Photo(
                photo_name = file.filename,
                photo_url = uploaded_file_url,
                encodings = binary
                )
            self.session.add(photo)
            self.session.commit()

class PersonService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        
    def get_photos_by_fio(self, fio: str) -> List[tables.Photo]:
        query_gallery  = (
            self.session
            .query(tables.Photo)
        )
        person = (
            self.session
            .query(tables.Person)
            .filter_by(fio = fio)
            .first()
        )
        photos = query_gallery.all()
        list_of_photos = []
        for photo in photos:
            if compare_faces(person.encodings, photo.encodings)[0]:
                list_of_photos.append(photo)
        return list_of_photos
    
    def get_persons(self) -> List[tables.Photo]:
        query = (
            self.session
            .query(tables.Person)
        )
        persons = query.all()
        return persons

    def add_person(self, fio: str, files: List[UploadFile]):
        folderPath = 'dataset'
        for file in files:
            if file.content_type not in ['image/jpeg', 'image/png']:
                raise HTTPException(status_code=400,
                                    detail="Invalid file type. Only JPEG and PNG images are allowed.")
        fileName = f'{folderPath}/{file.filename}'
        bucket = storage.bucket()
        blob = bucket.blob(fileName)
        blob.upload_from_file(file.file, content_type=file.content_type)
        binary = encoded_face(file)
        uploaded_file_url = blob.public_url
        person = tables.Person(
            fio = fio,
            photo_url = uploaded_file_url,
            encodings = binary
            )
        self.session.add(person)
        self.session.commit()

class ProcessService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def process_imgages(self):
        pass

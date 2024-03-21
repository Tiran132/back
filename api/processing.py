from fastapi import APIRouter, Depends
from services.logic import ProcessService

router = APIRouter(
    tags=['ProcessAPI'],
    )

@router.post('/process', status_code=201)
def process_imgages(
    process_service: ProcessService = Depends()
):
    return process_service.process_imgages()

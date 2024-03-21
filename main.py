from fastapi import FastAPI
from fastapi.middleware import cors
import uvicorn
from fastapi.responses import ORJSONResponse

from api.image import router as image
from api.person import router as person
from api.processing import router as process

app = FastAPI(
    title = "СЕРВИС ПО РАСПРОЗНАВАНИЮ ЛИЦ",
    description= 'Веб-приложение, позволяющее определить участников мероприятия и подтвердить их нахождение на нем.',
)
# ab = "khjhsf"
# d = 4
# @app.get("/",)
# def main():
#     return ORJSONResponse([{ab: d}])
app.include_router(image)
app.include_router(person)
app.include_router(process)

# app.add_middleware(cors,
#                    allow_origins=["*"],
#                    allow_credentials=True,
#                    allow_methods=["*"],
#                    allow_headers=["*"],
#                    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host= '127.0.0.1',
        port= 8000,
        reload = True,
    )

from fastapi import FastAPI

from app.bisection import bisection_service
from app.history import history_service

app = FastAPI()


@app.get("/")
def description():
    return {
        "auther": "mohammed zeidan",
        "description": "This api solves math problems with approximate solutions using different numerical methods",
        "technologies_used": ["Python", "FastAPI", "Kafka"]
        }


app.include_router(bisection_service.router)
app.include_router(history_service.router)


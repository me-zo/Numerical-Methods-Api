import datetime

import sympy as sp
from fastapi import APIRouter

from app.history.models import HistoryModel

router = APIRouter(prefix="/history")

x, y, z = sp.symbols('x y z')


@router.get("/get_all", response_model=HistoryModel)
async def get_all():
    """
    gets a history of all methods called

    """

    # parse from a kafka consumer
    history = HistoryModel(method_used="some method", date=datetime.datetime.now(), info="")

    return history


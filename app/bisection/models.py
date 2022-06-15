from typing import List, Optional

from pydantic import BaseModel


class BisectionIterationModel(BaseModel):
    id: int
    x_lower: float
    x_upper: float
    x_m: float
    f_of_xl: float
    f_of_xu: float
    f_of_xm: float
    error_percentage: float


class ResultBisectionModel(BaseModel):
    Count: int
    Iterations: List[BisectionIterationModel]


class RequestBisectionModel(BaseModel):
    count: int
    x_lower: int
    x_upper: int
    f_of_x: str
    round_to: Optional[int]

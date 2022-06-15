from datetime import datetime

from pydantic import BaseModel


class HistoryModel(BaseModel):
    method_used: str
    date: datetime
    info: str

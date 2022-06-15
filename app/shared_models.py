from typing import List

from pydantic import BaseModel


class DescriptionModel(BaseModel):
    description: str
    tested_symbols: List[str]

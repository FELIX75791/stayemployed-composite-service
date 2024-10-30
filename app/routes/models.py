from pydantic import BaseModel
from typing import List

class Link(BaseModel):
    rel: str
    href: str

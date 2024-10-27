from pydantic import BaseModel
from typing import List

class Infer(BaseModel):
    img: str


class InferTest(BaseModel):
    img: str
from pydantic import BaseModel
from typing import List, Optional

class Competitor(BaseModel):
    name: str
    strengths: Optional[List[str]] = []
    weaknesses: Optional[List[str]] = []
    products: Optional[List[str]] = []

class CompetitorInput(BaseModel):
    competitors: List[Competitor]

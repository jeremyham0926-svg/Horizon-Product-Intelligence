from pydantic import BaseModel
from typing import Dict, Any

class DecisionResult(BaseModel):
    summary: str
    scores: Dict[str, Any]

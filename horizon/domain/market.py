from pydantic import BaseModel
from typing import List, Optional

class MarketInput(BaseModel):
    target_segments: List[str]
    trends: Optional[List[str]] = []
    pain_points: Optional[List[str]] = []
    growth_rate: Optional[float] = None

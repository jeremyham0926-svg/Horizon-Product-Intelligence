from pydantic import BaseModel
from typing import List, Optional

class CompanyProfile(BaseModel):
    name: str
    industry: str
    segments: List[str]
    current_products: Optional[List[str]] = []
    capabilities: Optional[List[str]] = []
    regions: Optional[List[str]] = []
    strategic_goals: Optional[List[str]] = []

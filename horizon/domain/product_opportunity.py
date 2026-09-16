from pydantic import BaseModel
from typing import List, Optional

class ProductOpportunity(BaseModel):
    name: str
    value_proposition: str
    features: Optional[List[str]] = []
    target_customers: Optional[List[str]] = []
    pricing_model: Optional[str] = None
    distribution_channels: Optional[List[str]] = []

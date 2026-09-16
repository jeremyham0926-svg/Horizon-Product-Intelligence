from pydantic import BaseModel
from typing import List, Optional

class Constraints(BaseModel):
    regulatory: Optional[List[str]] = []
    technical: Optional[List[str]] = []
    platform: Optional[List[str]] = []
    operational: Optional[List[str]] = []
    integration_requirements: Optional[List[str]] = []

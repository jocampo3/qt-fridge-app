from app.models import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    type: str
    quantity: int
    store: str
    discarded_at: Optional[str] = None

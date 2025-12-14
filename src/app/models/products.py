from app.models import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    type: str
    quantity: int
    store: str
    stored_at: str
    discarded_at: Optional[str] = None

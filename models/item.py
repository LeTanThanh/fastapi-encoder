from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel):
  title: str
  timestamp: datetime
  description: str | None = None

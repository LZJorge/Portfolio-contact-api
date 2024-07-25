from typing import Optional
from pydantic import BaseModel
import uuid


class ListMessagesParams(BaseModel):
    id: Optional[uuid.UUID] = None
    name: Optional[str] = None
    email: Optional[str] = None
    message: Optional[str] = None

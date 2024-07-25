from typing import List, Optional
from pydantic import BaseModel
from app.domain.entity import Message


class ListMessagesResponse(BaseModel):
    success: bool
    status_code: int
    content: List[Message] = []
    msg: Optional[str] = None

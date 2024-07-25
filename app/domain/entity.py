from dataclasses import dataclass
import uuid


@dataclass
class Message:
    id: uuid.UUID
    name: str
    email: str
    message: str

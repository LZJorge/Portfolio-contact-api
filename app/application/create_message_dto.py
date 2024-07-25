from pydantic import BaseModel, Field, EmailStr


class CreateMessageDTO(BaseModel):
    name: str = Field(min_length=3, max_length=128)
    email: EmailStr = Field(min_length=3, max_length=128)
    message: str = Field(min_length=3, max_length=1024)

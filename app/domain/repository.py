from typing import List
from abc import ABC, abstractmethod
from app.domain.entity import Message


class GenericRepository(ABC):

    @abstractmethod
    async def get(self, id_: str) -> Message:
        raise NotImplementedError

    @abstractmethod
    async def list(self, **filters) -> List[Message]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, record: Message) -> Message:
        raise NotImplementedError

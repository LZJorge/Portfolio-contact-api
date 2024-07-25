from sqlalchemy import select, Select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repository import GenericRepository
from app.domain.entity import Message
from app.infrastructure.model.model import MessageModel


class SQLRepository(GenericRepository):

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._model_cls = MessageModel

    # Constructing SQL statements
    def _construct_get_stmt(self, id_: str):
        return select(self._model_cls).where(self._model_cls.id == id_)

    def _construct_list_stmt(self, **filters) -> Select:
        stmt = select(self._model_cls)
        where_clauses = []

        for column, value in filters.items():
            if not hasattr(self._model_cls, column):
                raise ValueError(f"Invalid column name {column}")

            where_clauses.append(getattr(self._model_cls, column).ilike(f"%{value}%"))

        if len(where_clauses) > 0:
            stmt = stmt.where(*where_clauses)

        return stmt

    # CRUD
    async def add(self, record: Message) -> Message:
        self._session.add(record)
        await self._session.flush()
        return record

    async def get(self, id_: str) -> Message:
        stmt = self._construct_get_stmt(id_)
        r = await self._session.execute(stmt)
        return r.scalars().first()

    async def list(self, **filters) -> list[Message]:
        stmt = self._construct_list_stmt(**filters)
        r = await self._session.execute(stmt)
        return r.scalars().all()

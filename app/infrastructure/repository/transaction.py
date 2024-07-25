from app.config.database import session_factory
from app.domain.transaction import GenericTransaction
from app.infrastructure.repository.sql_repository import SQLRepository


class Transaction(GenericTransaction):

    def __init__(self) -> None:
        self._session_factory = session_factory

    async def __aenter__(self):
        self._session = self._session_factory()
        self.message = SQLRepository(self._session)
        return await super().__aenter__()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()


def get_transaction() -> GenericTransaction:
    return Transaction

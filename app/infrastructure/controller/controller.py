from fastapi import Depends
from app.domain.transaction import GenericTransaction
from app.domain.entity import Message
from app.application.create_message_dto import CreateMessageDTO
from app.application.list_messages_response import ListMessagesResponse
from app.infrastructure.repository.transaction import get_transaction
from app.infrastructure.mapper.mapper import Mapper
import uuid


class Controller:
    _mapper = Mapper()

    def __init__(
        self, transaction: GenericTransaction = Depends(get_transaction)
    ) -> None:
        self._transaction = transaction

    async def add(self, record: CreateMessageDTO) -> ListMessagesResponse:
        m = Message(
            id=uuid.uuid4(),
            name=record.name,
            email=record.email,
            message=record.message,
        )

        try:
            async with self._transaction() as t:
                message = await t.message.add(self._mapper.to_model(m))
                await t.commit()
        except Exception:
            return ListMessagesResponse(success=False, status_code=500, content=[])

        return ListMessagesResponse(
            success=True,
            status_code=201,
            content=[self._mapper.to_entity(message)],
            msg="Message added",
        )

    async def list(self) -> ListMessagesResponse:
        try:
            async with self._transaction() as t:
                messages = await t.message.list()
                await t.commit()
        except Exception:
            return ListMessagesResponse(success=False, status_code=500, content=[])

        messages = [self._mapper.to_entity(m) for m in messages]
        return ListMessagesResponse(success=True, status_code=200, content=messages)


def get_controller(
    transaction: GenericTransaction = Depends(get_transaction),
) -> Controller:
    return Controller(transaction)

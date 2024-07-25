from app.domain.entity import Message
from app.infrastructure.model.model import MessageModel


class Mapper:
    def to_entity(self, model: MessageModel) -> Message:
        return Message(
            id=model.id, name=model.name, email=model.email, message=model.message
        )

    def to_model(self, entity: Message) -> MessageModel:
        return MessageModel(
            id=entity.id, name=entity.name, email=entity.email, message=entity.message
        )

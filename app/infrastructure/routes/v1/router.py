from typing import Annotated
from fastapi import APIRouter, Depends, Response, Header
from app.config.settings import settings
from app.application.create_message_dto import CreateMessageDTO
from app.application.list_messages_params import ListMessagesParams
from app.application.list_messages_response import ListMessagesResponse
from app.infrastructure.controller.controller import Controller, get_controller
from app.infrastructure.utils.handle_result import handle_result


router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=ListMessagesResponse)
async def list(
    x_key: Annotated[str | str, Header()],
    params: ListMessagesParams = Depends(),
    controller: Controller = Depends(get_controller),
    response: Response = Response(),
) -> ListMessagesResponse:
    if not x_key == settings.x_list_key:
        return ListMessagesResponse(
            success=False, status_code=401, content=[], msg="Invalid key"
        )

    query_params: dict = {key: value for key, value in params if value is not None}

    result = await controller.list(**query_params)
    handle_result(result, response)

    return result


@router.post("/", response_model=ListMessagesResponse)
async def add(
    x_key: Annotated[str | None, Header()],
    record: CreateMessageDTO,
    controller: Controller = Depends(get_controller),
    response: Response = Response(),
) -> ListMessagesResponse:
    if x_key != settings.x_add_key:
        return ListMessagesResponse(
            success=False, status_code=401, content=[], msg="Invalid key"
        )

    result = await controller.add(record)
    handle_result(result, response)

    return result

from fastapi import Response
from app.application.list_messages_response import ListMessagesResponse


def handle_result(result: ListMessagesResponse, response: Response) -> Response:
    if not result or not result.success:
        response.status_code = result.status_code

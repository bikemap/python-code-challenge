from datetime import datetime, timezone
from http import HTTPStatus

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from apischema.encoder import encode_to_json_response, encode_error_to_json_response
from apischema.validator import validate_todo_entry
from entities import TodoEntry
from persistance.mapper.memory import MemoryTodoEntryMapper
from persistance.repository import TodoEntryRepository

from usecases import get_todo_entry, create_todo_entry, UseCaseError, NotFoundError

_MAPPER_IN_MEMORY_STORAGE = {
    1: TodoEntry(id=1, summary="Lorem Ipsum", created_at=datetime.now(tz=timezone.utc))
}


async def get_todo(request: Request) -> Response:
    try:
        identifier = request.path_params["id"]  # TODO: add validation

        mapper = MemoryTodoEntryMapper(storage=_MAPPER_IN_MEMORY_STORAGE)
        repository = TodoEntryRepository(mapper=mapper)

        entity = await get_todo_entry(identifier=identifier, repository=repository)
        content = encode_to_json_response(entity=entity)

    except NotFoundError:
        return Response(
            content=None,
            status_code=HTTPStatus.NOT_FOUND,
            media_type="application/json",
        )

    return Response(content=content, media_type="application/json")


async def create_new_todo_entry(request: Request) -> Response:
    data = await request.json()
    errors = validate_todo_entry(raw_data=data)
    if errors:
        return Response(
            content=encode_error_to_json_response(error=errors),
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            media_type="application/json",
        )

    mapper = MemoryTodoEntryMapper(storage=_MAPPER_IN_MEMORY_STORAGE)
    repository = TodoEntryRepository(mapper=mapper)

    try:
        entity = TodoEntry(**data)
        entity = await create_todo_entry(entity=entity, repository=repository)
        content = encode_to_json_response(entity=entity)
    except UseCaseError:
        return Response(
            content=None,
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            media_type="application/json",
        )

    return Response(
        content=content, status_code=HTTPStatus.CREATED, media_type="application/json"
    )


app = Starlette(
    debug=True,
    routes=[
        Route("/todo/", create_new_todo_entry, methods=["POST"]),
        Route("/todo/{id:int}/", get_todo, methods=["GET"]),
    ],
)

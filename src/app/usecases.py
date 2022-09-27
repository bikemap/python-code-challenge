from entities import TodoEntry
from persistence.errors import CreateError, EntityNotFoundError
from persistence.repository import TodoEntryRepository


class UseCaseError(Exception):
    pass


class NotFoundError(UseCaseError):
    pass


async def get_todo_entry(identifier: int, repository: TodoEntryRepository) -> TodoEntry:
    try:
        return await repository.get(identifier=identifier)
    except EntityNotFoundError as err:
        raise NotFoundError(err)


async def create_todo_entry(
    entity: TodoEntry, repository: TodoEntryRepository
) -> TodoEntry:
    try:
        return await repository.create(entity=entity)
    except CreateError as error:
        raise UseCaseError(error)

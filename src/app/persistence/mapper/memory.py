from random import randint

from entities import TodoEntry
from persistence.mapper.errors import EntityNotFoundMapperError, CreateMapperError
from persistence.mapper.interfaces import TodoEntryMapperInterface


class MemoryTodoEntryMapper(TodoEntryMapperInterface):
    _storage: dict

    def __init__(self, storage: dict) -> None:
        self._storage = storage

    async def get(self, identifier: int) -> TodoEntry:
        try:
            return self._storage[identifier]
        except KeyError:
            raise EntityNotFoundMapperError(f"Entity `id:{identifier}` was not found.")

    async def create(self, entity: TodoEntry) -> TodoEntry:
        try:
            entity.id = self._generate_unique_id()
            self._storage[entity.id] = entity
            return entity
        except TypeError as error:
            raise CreateMapperError(error)

    def _generate_unique_id(self) -> int:
        identifier = randint(1, 10_000)
        while identifier in self._storage:
            identifier = randint(1, 10_000)

        return identifier

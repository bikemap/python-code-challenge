from entities import TodoEntry
from persistence.errors import EntityNotFoundError, CreateError
from persistence.mapper.errors import EntityNotFoundMapperError, CreateMapperError
from persistence.mapper.interfaces import TodoEntryMapperInterface


class TodoEntryRepository:
    _mapper: TodoEntryMapperInterface

    def __init__(self, mapper: TodoEntryMapperInterface) -> None:
        self._mapper = mapper

    async def get(self, identifier: int) -> TodoEntry:
        try:
            return await self._mapper.get(identifier=identifier)
        except EntityNotFoundMapperError as error:
            raise EntityNotFoundError(error)

    async def create(self, entity: TodoEntry) -> TodoEntry:
        try:
            return await self._mapper.create(entity=entity)
        except CreateMapperError as error:
            raise CreateError(error)

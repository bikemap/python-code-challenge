from datetime import datetime, timezone

import pytest

from entities import TodoEntry
from persistence.errors import EntityNotFoundError, CreateError
from persistence.mapper.memory import MemoryTodoEntryMapper
from persistence.repository import TodoEntryRepository

_memory_storage = {
    1: TodoEntry(id=1, summary="Lorem Ipsum", created_at=datetime.now(tz=timezone.utc))
}


@pytest.mark.asyncio
async def test_get_todo_entry() -> None:
    mapper = MemoryTodoEntryMapper(storage=_memory_storage)
    repository = TodoEntryRepository(mapper=mapper)

    entity = await repository.get(identifier=1)
    assert isinstance(entity, TodoEntry)


@pytest.mark.asyncio
async def test_todo_entry_not_found_error() -> None:
    mapper = MemoryTodoEntryMapper(storage=_memory_storage)
    repository = TodoEntryRepository(mapper=mapper)

    with pytest.raises(EntityNotFoundError):
        await repository.get(identifier=42)


@pytest.mark.asyncio
async def test_save_todo_entry() -> None:
    mapper = MemoryTodoEntryMapper(storage=_memory_storage)
    repository = TodoEntryRepository(mapper=mapper)

    data = TodoEntry(
        summary="Buy flowers to my wife",
        detail="We have marriage anniversary",
        created_at=datetime.now(tz=timezone.utc),
    )

    entity = await repository.create(entity=data)
    assert isinstance(entity, TodoEntry)
    assert entity.id > 1


@pytest.mark.asyncio
async def test_todo_entry_create_error() -> None:
    mapper = MemoryTodoEntryMapper(storage=None)
    repository = TodoEntryRepository(mapper=mapper)

    data = TodoEntry(
        summary="Lorem Ipsum",
        detail=None,
        created_at=datetime.now(tz=timezone.utc),
    )

    with pytest.raises(CreateError):
        await repository.create(entity=data)

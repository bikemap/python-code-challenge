from abc import ABCMeta, abstractmethod

from entities import TodoEntry


class TodoEntryMapperInterface(metaclass=ABCMeta):
    @abstractmethod
    async def get(self, identifier: int) -> TodoEntry:
        """Return TodoEntry entity from persistence layer"""

    @abstractmethod
    async def create(self, entity: TodoEntry) -> TodoEntry:
        """Creates new TodoEntry in persistence layer"""

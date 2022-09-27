class RepositoryError(Exception):
    pass


class EntityNotFoundError(RepositoryError):
    pass


class CreateError(RepositoryError):
    pass

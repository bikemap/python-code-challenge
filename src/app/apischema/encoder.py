from json import dumps

from pydantic.json import pydantic_encoder

from apischema.validator import SchemaError
from entities import AbstractEntity


def error_to_json(error: SchemaError) -> str:
    return dumps(
        {
            "type": error.type,
            "message": error.message,
            "validation_schema": error.validation_schema,
            "path": error.path,
        },
        ensure_ascii=False,
        allow_nan=False,
        indent=None,
        separators=(",", ":"),
    )


def entity_to_json(data: AbstractEntity) -> str:
    return dumps(data, indent=4, default=pydantic_encoder)


def encode_to_json_response(entity: AbstractEntity) -> bytes:
    return entity_to_json(entity).encode("utf-8")


def encode_error_to_json_response(error: SchemaError) -> bytes:
    return error_to_json(error).encode("utf-8")

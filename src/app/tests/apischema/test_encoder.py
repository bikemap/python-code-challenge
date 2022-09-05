from json import loads

from apischema.encoder import (
    error_to_json,
    entity_to_json,
    encode_to_json_response,
    encode_error_to_json_response,
)
from apischema.validator import SchemaError
from entities import AbstractEntity


def test_error_to_json() -> None:
    error = SchemaError(
        type="Validation Error",
        message="Something is wrong",
        validation_schema={"maxlength": 16, "type": "string"},
        path="some.path.in.json",
    )
    json = error_to_json(error=error)
    assert isinstance(json, str)

    data = loads(json)

    assert "type" in data
    assert "message" in data
    assert "validation_schema" in data
    assert "path" in data


def test_entity_to_json() -> None:
    entity = AbstractEntity(id=1)

    json = entity_to_json(data=entity)
    assert isinstance(json, str)

    data = loads(json)

    assert "id" in data


def test_encode_to_json_response() -> None:
    entity = AbstractEntity(id=42)
    data = encode_to_json_response(entity=entity)

    assert isinstance(data, bytes)


def test_encode_error_to_json_response() -> None:
    error = SchemaError(
        type="Error",
        message="Something is wrong",
        validation_schema={"type": "string"},
        path="property",
    )
    data = encode_error_to_json_response(error=error)

    assert isinstance(data, bytes)

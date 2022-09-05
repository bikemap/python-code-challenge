from apischema.validator import validate_todo_entry


def test_short_summary_in_todo_entry() -> None:
    data = {
        "summary": "Lo",
        "detail": "",
        "created_at": "2022-09-05T18:07:19.280040+00:00",
    }

    error = validate_todo_entry(raw_data=data)
    assert error.path == "summary"
    assert "maxLength" in error.validation_schema
    assert "minLength" in error.validation_schema
    assert "type" in error.validation_schema

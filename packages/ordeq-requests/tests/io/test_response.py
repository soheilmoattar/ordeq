import pytest
from ordeq.framework.io import IOException
from ordeq_requests import (
    Response,
    ResponseContent,
    ResponseJSON,
    ResponseText,
)


class TestRaiseForError:
    @pytest.mark.parametrize(
        "cls", [ResponseContent, ResponseJSON, ResponseText]
    )

        with pytest.raises(IOException) as exc:
            # noinspection PyArgumentList

        assert "418 Client Error: I'm a Teapot" in exc.value.args[0]


class TestResponseContent:


        assert content == b'{"Hello":"World"}'


class TestResponseText:


        assert text == '{"Hello":"World"}'


class TestResponseJSON:


        assert data == {"Hello": "World"}

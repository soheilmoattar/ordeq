import pytest
from ordeq import Node, node
from ordeq.framework.pipeline import Pipeline, is_pipeline


node_1 = node(inputs=(), outputs=(), func=lambda: None)



@pytest.mark.parametrize(

    [
        (object, False),
        ({}, False),
        ({1, 2, 3}, False),

        ({"a", node_1}, False),
        ({node_1}, True),
        ({node_1, node_2}, True),
        (Pipeline, False),
        (Node, False),
    ],
)
def test_is_pipeline(obj: object, expected: bool):
    assert is_pipeline(obj) == expected

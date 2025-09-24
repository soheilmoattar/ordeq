from ordeq import node
from resources.gather.example.catalog_1 import a
from resources.gather.example.catalog_1 import b as B
from resources.gather.example.catalog_2 import f


@node(
    inputs=[a, B],
    outputs=f
)
def func(a_val: str, b_val: str) -> str:
    return a_val + b_val

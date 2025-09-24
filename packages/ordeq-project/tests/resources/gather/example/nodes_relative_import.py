from ordeq import node
from resources.gather.example import catalog_1, catalog_2


@node(
    inputs=[catalog_1.a, catalog_1.b],
    outputs=catalog_2.f
)
def func(a_val: str, b_val: str) -> str:
    return a_val + b_val





from ordeq.framework.io import IO



class PydanticJSON(IO[pydantic.BaseModel]):
    """IO to load and save Pydantic models to JSON



    ```python
    >>> from pathlib import Path
    >>> from ordeq_pydantic import PydanticJSON
    >>> from pydantic import BaseModel

    >>> class MyModel(BaseModel):
    ...     hello: str
    ...     world: str

    >>> dataset = PydanticJSON(
    ...     path=Path("path/to.json"),
    ...     model_type=MyModel
    ... )

    ```














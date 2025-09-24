

from ordeq import IO




class Text(IO[str]):
    """IO representing a plain-text file.



    ```python
    >>> from ordeq_files import Text
    >>> from pathlib import Path
    >>> MyText = Text(
    ...     path=Path("path/to.txt")
    ... )

    ```













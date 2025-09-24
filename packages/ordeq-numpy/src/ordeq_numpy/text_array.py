


from ordeq.framework.io import IO




class NumpyText(IO[np.ndarray]):
    """IO to load from and save plain text numpy arrays.



    ```python
    >>> from pathlib import Path
    >>> from ordeq_numpy import NumpyText
    >>> MyArray = NumpyText(
    ...     path=Path("path/to.txt")
    ... )

    ```













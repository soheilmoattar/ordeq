


from ordeq.framework.io import IO




class NumpyBinary(IO[np.ndarray]):
    """IO to load from and save binary numpy arrays.



    ```python
    >>> from pathlib import Path
    >>> from ordeq_numpy import NumpyBinary
    >>> MyArray = NumpyBinary(
    ...     path=Path("path/to.npy")
    ... )

    ```













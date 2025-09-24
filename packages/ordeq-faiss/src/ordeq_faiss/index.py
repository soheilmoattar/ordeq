



from ordeq.framework.io import IO



class FaissIndex(IO[faiss.Index]):
    """IO to load from and save index data using Faiss. Calls




    ```python
    >>> from pathlib import Path
    >>> from ordeq_faiss import FaissIndex
    >>> MyIndex = FaissIndex(
    ...     path=Path("path/to.index")
    ... )

    ```











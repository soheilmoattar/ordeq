







class PymupdfFile(IO[pymupdf.Document]):
    """IO to load from and save PDF files using Pymupdf.



    ```python
    >>> from pathlib import Path
    >>> from ordeq_pymupdf import PymupdfFile
    >>> MyPDF = PymupdfFile(
    ...     path=Path("path/to.index")
    ... )

    ```





















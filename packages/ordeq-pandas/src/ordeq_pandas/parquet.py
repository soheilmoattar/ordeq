


from ordeq.framework.io import IO




class PandasParquet(IO[pd.DataFrame]):
    """IO to load from and save to PARQUET data using Pandas. Calls




    ```python
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasParquet
    >>> MyParquet = PandasParquet(
    ...     path=Path("path/to.parquet")
    ... )

    ```



    path: PathLike







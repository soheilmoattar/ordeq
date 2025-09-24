








    """IO for loading and saving Parquet using Polars.

    Example:

    ```python
    >>> from ordeq_polars import PolarsEagerParquet
    >>> from pathlib import Path
    >>> csv = PolarsEagerParquet(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     n_rows=1_000
    ... )

    ```

    """










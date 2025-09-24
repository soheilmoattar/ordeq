from dataclasses import dataclass

import polars as pl




@dataclass(frozen=True, kw_only=True)

    """IO for loading and saving Excel using Polars.

    Example:

    ```python
    >>> from ordeq_polars import PolarsEagerExcel
    >>> from pathlib import Path
    >>> xlsx = PolarsEagerExcel(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     has_header=True
    ... )

    ```

    """

    path: PathLike


        with self.path.open(mode="rb") as fh:



        with self.path.open(mode="wb") as fh:


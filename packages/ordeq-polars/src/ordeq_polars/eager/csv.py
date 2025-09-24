from dataclasses import dataclass

import polars as pl




@dataclass(frozen=True, kw_only=True)

    """IO for loading and saving CSV using Polars.

    Example:

    ```python
    >>> from ordeq_polars import PolarsEagerCSV
    >>> from pathlib import Path
    >>> csv = PolarsEagerCSV(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     has_header=True
    ... )

    ```

    """

    path: PathLike





        with self.path.open(mode="wb") as fh:


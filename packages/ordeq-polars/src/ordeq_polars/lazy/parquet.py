from dataclasses import dataclass
from pathlib import Path

import polars as pl



@dataclass(frozen=True, kw_only=True)

    """IO for loading and saving Parquet lazily using Polars.

    Example:

    ```python
    >>> from ordeq_polars import PolarsLazyParquet
    >>> from pathlib import Path
    >>> csv = PolarsLazyParquet(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     n_rows=1_000
    ... )

    ```

    """

    path: Path







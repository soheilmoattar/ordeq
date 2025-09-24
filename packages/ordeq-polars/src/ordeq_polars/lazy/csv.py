from dataclasses import dataclass
from pathlib import Path

import polars as pl



@dataclass(frozen=True, kw_only=True)

    """IO for loading and saving CSV lazily using Polars.

    Example:

    ```python
    >>> from ordeq_polars import PolarsLazyCSV
    >>> from pathlib import Path
    >>> csv = PolarsLazyCSV(
    ...     path=Path("to.csv")
    ... ).with_load_options(
    ...     has_header=True
    ... )

    ```

    """

    path: Path







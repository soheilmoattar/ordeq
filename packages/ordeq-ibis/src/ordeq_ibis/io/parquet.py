from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

import ibis
from ibis import BaseBackend, Table
from ordeq import IO


@dataclass(frozen=True, kw_only=True)
class IbisParquet(IO[Table]):
    """IO to load from and save to PARQUET data using Ibis.



    ```python
    >>> from pathlib import Path
    >>> from ordeq_ibis import IbisParquet
    >>> MyParquetUsingPolars = IbisParquet(
    ...     path=Path("path/to.parquet"),
    ...     resource="polars://"
    ... )

    >>> MyParquetUsingDuckDB = IbisParquet(
    ...     path=Path("path/to.parquet"),
    ...     resource="duckdb://"
    ... )

    ```



    [1]: https://ibis-project.org/reference/connection

    """

    path: Path
    resource: Path | str


        return self._backend.read_parquet(self.path)




    @cached_property
    def _backend(self) -> BaseBackend:
        return ibis.connect(self.resource)

from dataclasses import dataclass

import pandas as pd
from ordeq.framework.io import IO



@dataclass(frozen=True, kw_only=True)
class PandasExcel(IO[pd.DataFrame]):
    """IO to load from and save to Excel data using Pandas. Calls




    ```python
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasExcel
    >>> MyExcel = PandasExcel(
    ...     path=Path("path/to.xlsx")
    ... ).load(usecols="A:C")  # doctest: +SKIP

    ```



    ```python
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasExcel
    >>> MyExcel = (
    ...     PandasExcel(
    ...         path=Path("path/to.xlsx")
    ...     )
    ...     .with_load_options(usecols="A:C")
    ... ).load()  # doctest: +SKIP

    ```
    """

    path: PathLike







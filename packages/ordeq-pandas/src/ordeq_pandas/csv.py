from dataclasses import dataclass

import pandas as pd
from ordeq.framework.io import IO



@dataclass(frozen=True, kw_only=True)
class PandasCSV(IO[pd.DataFrame]):
    """IO to load from and save to CSV data using Pandas. Calls


    Example:

    ```python
    >>> import pandas as pd
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasCSV
    >>> MyCSV = PandasCSV(
    ...     path=Path("path/to.csv")
    ... ).load(header="infer")  # doctest: +SKIP

    ```



    ```python
    >>> import pandas as pd
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasCSV
    >>> MyCSV = (
    ...     PandasCSV(
    ...         path=Path("path/to.csv")
    ...     )
    ...     .with_load_options(header="infer")
    ... ).load()  # doctest: +SKIP

    ```



    ```python
    >>> import pandas as pd
    >>> from pathlib import Path
    >>> from ordeq_pandas import PandasCSV
    >>> MyCSV = (
    ...     PandasCSV(
    ...         path=Path("path/to.csv"),
    ...     )
    ...     .with_save_options(header=True)
    ... ).save()  # doctest: +SKIP

    ```

    """

    path: PathLike







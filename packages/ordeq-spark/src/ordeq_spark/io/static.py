from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from ordeq.framework.io import Input

from pyspark.sql.types import StructType




@dataclass(frozen=True, kw_only=True, eq=False)
class SparkStatic(Input[DataFrame]):
    """Allows a Spark DataFrame to be hard-coded in python. This is suitable
    for small tables such as very simple dimension tables that are unlikely to
    change. It may also be useful in unit testing.

    Example usage:

    ```python
    >>> from pyspark.sql.types import *
    >>> from ordeq_spark import SparkStatic
    >>> DF = SparkStatic(
    ...     schema=StructType([
    ...         StructField("year", IntegerType()),
    ...         StructField("datafile", StringType()),
    ...     ]),
    ...     data=(
    ...         (2022, "file_2022.xlsx"),
    ...         (2023, "file_2023.xlsx"),
    ...         (2024, "file_2023.xlsx"),
    ...     )
    ... )

    ```

    """

    data: Iterable[tuple[Any, ...]]
    schema: StructType | None = None





        )

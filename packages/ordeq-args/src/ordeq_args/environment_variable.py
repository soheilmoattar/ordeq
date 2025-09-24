import os
from dataclasses import KW_ONLY, dataclass

from ordeq.framework.io import IO


@dataclass(frozen=True)
class EnvironmentVariable(IO[str]):
    """IO used to load and save environment variables. Use:
        - as input, to parameterize the node logic
        - as output, to set an environment variable based on node logic


    information.

    [1] https://docs.python.org/3/library/os.html#os.environ

    Example in a node:

    ```python
    >>> from ordeq import node
    >>> from ordeq_spark import SparkHiveTable
    >>> import pyspark.sql.functions as F
    >>> from pyspark.sql import DataFrame

    >>> @node(
    ...    inputs=[
    ...         SparkHiveTable(table="my.table"),
    ...         EnvironmentVariable("KEY", default="DEFAULT")
    ...    ],
    ...    outputs=SparkHiveTable(table="my.output"),
    ... )
    ... def transform(df: DataFrame, value: str) -> DataFrame:
    ...     return df.where(F.col("col") == value)

    ```



    ```shell
    export KEY=MyValue
    python {your-entrypoint} run --node transform
    ```



    """

    key: str
    _: KW_ONLY
    default: str | None = None


        if self.default:
            return os.environ.get(self.key, self.default)
        return os.environ[self.key]


        os.environ[self.key] = value

import argparse


from ordeq.framework.io import Input

T = TypeVar("T")


class CommandLineArg(Input[T]):
    """Dataset that represents a command line argument as node input. Useful
    for parameterization of node logic based on arguments in the run command.


    [argparse](https://docs.python.org/3/library/argparse.html) for more
    information.

    Example:

    ```python
    >>> from ordeq import node
    >>> from ordeq_spark import SparkHiveTable
    >>> import pyspark.sql.functions as F
    >>> from pyspark.sql import DataFrame

    >>> @node(
    ...    inputs=[
    ...         SparkHiveTable(table="my.table"),
    ...         CommandLineArg("--value")
    ...    ],
    ...    outputs=SparkHiveTable(table="my.output"),
    ... )
    ... def transform(df: DataFrame, value: str) -> DataFrame:
    ...     return df.where(F.col("col") == value)

    ```

    When you run `transform` through the CLI as follows:

    ```shell
    python {your-entrypoint} run --node transform --value MyValue
    ```



    By default, the command line arguments are parsed as string. You can
    parse as different type using built-in type converters, for instance:

    ```python
    >>> K = CommandLineArg("--k", type=int)
    >>> Threshold = CommandLineArg("--threshold", type=float)
    >>> Address = CommandLineArg("--address", type=ascii)
    >>> import pathlib
    >>> Path = CommandLineArg("--path", type=pathlib.Path)
    >>> import datetime
    >>> DateTime = CommandLineArg("--date", type=datetime.date.fromisoformat)

    ```

    Alternatively, you can parse using a user-defined function, e.g.:

        >>> def hyphenated(string: str) -> str:
        ...     return '-'.join([w[:4] for w in string.casefold().split()])
        >>> parser = argparse.ArgumentParser()
        >>> Title = CommandLineArg("--title", type=hyphenated)


    [it has been deprecated](https://docs.python.org/3.14/whatsnew/3.14.html#deprecated)
    from Python 3.14.

    More info on parsing types [here](https://docs.python.org/3/library/argparse.html#type)
    """

    arg: str














        ns, _ = self.parser.parse_known_args()

        return val




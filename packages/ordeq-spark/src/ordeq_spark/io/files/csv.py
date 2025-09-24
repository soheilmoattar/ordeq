from dataclasses import dataclass









@dataclass(frozen=True, kw_only=True)

    """IO for loading and saving CSV using Spark.

    Example:

    ```python
    >>> from ordeq_spark import SparkCSV
    >>> csv = SparkCSV(
    ...     path="to.csv"
    ... ).with_load_options(
    ...     infer_schema=True
    ... )

    ```

    By default, Spark creates a directory on save.
    Use `single_file` if you want to write to a file instead:

    ```python
    >>> from ordeq_spark import SparkJSON
    >>> csv = SparkJSON(
    ...     path="to.json"
    ... ).with_load_options(single_file=True)

    ```

    """


























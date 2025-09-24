











    """IO for loading and saving JSON using Spark.

    Example:

    ```python
    >>> from ordeq_spark import SparkJSON
    >>> csv = SparkJSON(
    ...     path="to.json"
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




















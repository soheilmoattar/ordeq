from dataclasses import dataclass












@dataclass(frozen=True, kw_only=True)

    """IO for reading from and writing to Hive tables in Spark.

    Examples:

    Save a DataFrame to a Hive table:

    ```python
    >>> from ordeq_spark import SparkHiveTable
    >>> from pyspark.sql import SparkSession
    >>> spark = SparkSession.builder.enableHiveSupport().getOrCreate()  # doctest: +SKIP
    >>> table = SparkHiveTable(table="my_hive_table")
    >>> df = spark.createDataFrame(
    ...     [(1, "Alice"), (2, "Bob")], ["id", "name"]
    ... )  # doctest: +SKIP
    >>> table.save(df, format="parquet", mode="overwrite")  # doctest: +SKIP

    ```

    If `schema` is provided, it will be applied before save and after load.

    """  # noqa: E501 (line too long)













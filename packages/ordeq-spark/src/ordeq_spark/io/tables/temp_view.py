










    """IO for reading from and writing to Spark temporary views.

    Examples:

    Create and save a DataFrame to a temp view:

    ```python
    >>> from ordeq_spark import SparkTempView
    >>> from pyspark.sql import SparkSession
    >>> spark = SparkSession.builder.getOrCreate()  # doctest: +SKIP
    >>> view = SparkTempView(table="my_temp_view")
    >>> df = spark.createDataFrame(
    ...     [(1, "Alice"), (2, "Bob")], ["id", "name"]
    ... )  # doctest: +SKIP
    >>> view.save(df, mode="createOrReplace")  # doctest: +SKIP

    ```

    Load the DataFrame from the temp view:

    ```python
    >>> loaded_df = view.load()  # doctest: +SKIP
    >>> loaded_df.show()  # doctest: +SKIP

    ```

    """
















from dataclasses import dataclass

from ordeq.framework.io import IO, Input

from pyspark.sql.types import StructType




@dataclass(frozen=True, kw_only=True)
class SparkJDBC:
    """IO for loading from and saving to a database with Spark and JDBC.

    The JDBC driver need to be added to your Spark application. For
    instance, to connect to Microsoft SQL Server, pass


    When saving, the types of the DataFrame should be compatible with the
    target table. More info [1].

    [1] https://spark.apache.org/docs/4.0.0-preview1/sql-data-sources-jdbc.html

    Example:

    ```python
    >>> from ordeq_spark import SparkJDBCTable
    >>> SparkJDBCTable(
    ...     table="schema.table",
    ...     driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
    ...     url=(
    ...         "jdbc:sqlserver://host:52840"
    ...         "databaseName=tempdb;"
    ...         "user=SA;"
    ...         "password=1Secure*Password1;"
    ...     )
    ...  ).load()  # doctest: +SKIP

    ```

    Use `SparkJDBCQuery` to execute a custom query on load:

    ```python
    >>> from ordeq_spark import SparkJDBCQuery
    >>> SparkJDBCQuery(
    ...     query="SELECT 1;",
    ...     driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
    ...     url=(
    ...         "jdbc:sqlserver://host:52840"
    ...         "databaseName=tempdb;"
    ...         "user=SA;"
    ...         "password=1Secure*Password1;"
    ...     )
    ...  ).load()  # doctest: +SKIP

    ```
    """

    url: str
    driver: str
    schema: StructType | None = None


        return (

            .read.format("jdbc")
            .options(url=self.url, driver=self.driver, **kwargs)
        )


        return df.write.format("jdbc").options(
            url=self.url, driver=self.driver, **kwargs
        )


@dataclass(frozen=True, kw_only=True)
class SparkJDBCTable(IO[DataFrame], SparkJDBC):
    table: str



        return apply_schema(df, self.schema) if self.schema else df




        df = apply_schema(df, self.schema) if self.schema else df



@dataclass(frozen=True, kw_only=True)
class SparkJDBCQuery(Input[DataFrame], SparkJDBC):
    query: str



        return apply_schema(df, self.schema) if self.schema else df

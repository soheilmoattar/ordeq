
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

import pyspark.sql.functions as F

from pyspark.sql import Column, DataFrame
from pyspark.sql.utils import CapturedException

if TYPE_CHECKING:







from pyspark.sql.utils import AnalysisException

from ordeq_spark.io.tables.table import SparkTable
from ordeq_spark.utils import apply_schema

SparkIcebergWriteMode = Literal[

]


@dataclass(frozen=True, kw_only=True)

    """IO used to load & save Iceberg tables using Spark.

    Example usage:

    ```python
    >>> from ordeq_spark import (
    ...     SparkIcebergTable
    ... )
    >>> from pyspark.sql.types import StructType, StructField, IntegerType
    >>> MyTable = SparkIcebergTable(
    ...     table="my.iceberg.table",
    ...     schema=StructType(
    ...         fields=[
    ...             StructField("id", IntegerType()),
    ...             StructField("amount", IntegerType()),
    ...         ]
    ...     )
    ... )

    >>> import pyspark.sql.functions as F
    >>> MyPartitionedTable = (
    ...     SparkIcebergTable(
    ...         table="my.iceberg.table"
    ...     ).with_save_options(
    ...         mode="overwritePartitions",
    ...         partition_by=(
    ...             ("colour",),
    ...             (F.years, "dt"),
    ...         )
    ...     )
    ... )

    ```



    Saving is idempotent: if the target table does not exist, it is
    created with the configuration set in the save options.

    Table properties can be specified on the `properties` attribute.
    Currently, the properties will be taken into account on write only.

    ```python
    >>> TableWithProperties = SparkIcebergTable(
    ...     table="my.iceberg.table",
    ...     properties=(
    ...         ('read.split.target-size', '268435456'),
    ...         ('write.parquet.row-group-size-bytes', '268435456'),
    ...     )
    ... )

    ```

    Currently only supports a subset of Iceberg writes. More info [1]:

    [1]: https://iceberg.apache.org/docs/nightly/spark-writes/

    """

    properties: tuple[tuple[str, str], ...] = ()





























        df = apply_schema(df, self.schema) if self.schema else df




















        try:




                case "overwritePartitions":
                    return writer.overwritePartitions()
                case "append":
                    return writer.append()
                case "create" | "createOrReplace":
                    return writer.createOrReplace()
                case _:

        # pyspark errors are captured here as CapturedException. A
        # better, more granular exception seems
        # 'pyspark.errors.AnalysisException', but it is only available in more
        # recent versions of PySpark
        except CapturedException as exc:










            if exc.getErrorClass() == "TABLE_OR_VIEW_NOT_FOUND" or (

                and isinstance(exc, AnalysisException)
            ):
                return writer.createOrReplace()
            raise








        """Returns a Spark DataFrame writer configured by save options.










        """

        writer = df.writeTo(self.table).using("iceberg")
        for k, v in self.properties:
            writer = writer.tableProperty(k, v)




















        return writer

from dataclasses import dataclass


from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType




@dataclass(frozen=True, kw_only=True)

    table: str
    schema: StructType | None = None


        df = SparkSession.builder.getOrCreate().table(self.table)
        return apply_schema(df, self.schema) if self.schema else df

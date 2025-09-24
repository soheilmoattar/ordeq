

import pyspark.sql.functions as F

from pyspark.sql.types import DataType, StructField, StructType





    """Utility method that creates a Spark StructType (or, schema) from tuple
    inputs, without need to import and write StructType & StructField






    """




def apply_schema(df: DataFrame, schema: StructType) -> DataFrame:
    """Applies a schema to the DataFrame, meaning:
    - select only those columns in the schema from the DataFrame
    - cast these to the types specified in the schema

    Note that this method does **not** check for nullability in the schema.







    """























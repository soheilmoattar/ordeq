
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    IntegerType,
    Row,
    StringType,
    StructField,
    StructType,
)




        schema=StructType(
            fields=[
                StructField("village", StringType()),
                StructField("hobbit_count", IntegerType()),
            ]
        ),
        data=(("Appleford", 6), ("Brothbridge", 19), ("Cheeseshire", 14)),






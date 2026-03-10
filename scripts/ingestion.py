from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DecimalType,
    IntegerType,
    DateType
)


def get_sales_schema():

    schema = StructType([
        StructField("Order_ID", StringType(), True),
        StructField("Customer_ID", StringType(), True),
        StructField("Customer_Type", StringType(), True),
        StructField("Product", StringType(), True),
        StructField("Category", StringType(), True),
        StructField("Unit_Price", DecimalType(10, 2), True),
        StructField("Quantity", IntegerType(), True),
        StructField("Discount", DecimalType(5, 2), True),
        StructField("Total_Price", DecimalType(12, 2), True),
        StructField("Region", StringType(), True),
        StructField("Order_Date", DateType(), True)
    ])

    return schema


def load_sales_data(spark, path: str):

    schema = get_sales_schema()

    df = (
        spark.read
        .format("csv")
        .option("header", True)
        .option("delimiter", ",")
        .option("mode", "FAILFAST")
        .option("dateFormat", "yyyy-MM-dd")
        .schema(schema)
        .load(path)
    )

    return df
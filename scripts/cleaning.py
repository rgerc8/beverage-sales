from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_sales_data(df: DataFrame) -> DataFrame:
    df_clean = (
        df
        .dropDuplicates()
        .filter(F.col("Order_ID").isNotNull())
        .filter(F.col("Customer_ID").isNotNull())
        .filter(F.col("Product").isNotNull())
        .filter(F.col("Quantity").isNotNull())
        .filter(F.col("Unit_Price").isNotNull())
        .filter(F.col("Total_Price").isNotNull())
        .filter(F.col("Quantity") > 0)
        .filter(F.col("Unit_Price") >= 0)
        .filter(F.col("Discount") >= 0)
        .filter(F.col("Total_Price") >= 0)
        .withColumn("Customer_Type", F.trim(F.col("Customer_Type")))
        .withColumn("Product", F.trim(F.col("Product")))
        .withColumn("Category", F.trim(F.col("Category")))
        .withColumn("Region", F.trim(F.col("Region")))
    )

    return df_clean
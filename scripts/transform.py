from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def transform_sales_data(df: DataFrame) -> DataFrame:
    df_transformed = (
        df
        .withColumn("Year", F.year("Order_Date"))
        .withColumn("Month", F.month("Order_Date"))
        .withColumn("Gross_Sales", F.col("Unit_Price") * F.col("Quantity"))
        .withColumn("Discount_Value", F.col("Gross_Sales") * F.col("Discount"))
    )

    return df_transformed
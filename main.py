import logging
from scripts.spark_session import get_spark
from scripts.ingestion import load_sales_data
from scripts.cleaning import clean_sales_data
from scripts.transform import transform_sales_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

RAW_PATH = "data/raw/synthetic_beverage_sales_data.csv"
STAGED_PATH = "data/silver/sales_transformed.parquet"


def main():

    logging.info("Starting pipeline")

    spark = get_spark()

    df_raw = load_sales_data(spark, RAW_PATH)
    logging.info(f"Raw rows: {df_raw.count()}")

    df_clean = clean_sales_data(df_raw)
    logging.info(f"Clean rows: {df_clean.count()}")

    df_transformed = transform_sales_data(df_clean)
    logging.info(f"Transformed rows: {df_transformed.count()}")

    (
        df_transformed.write
        .mode("overwrite")
        .parquet(STAGED_PATH)
    )

    logging.info(f"Data written to: {STAGED_PATH}")


if __name__ == "__main__":
    main()
import os

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["PATH"] = r"C:\hadoop\bin;" + os.environ["PATH"]

print(os.environ["HADOOP_HOME"])
print(os.environ["PATH"].split(";")[:5])

from pyspark.sql import SparkSession

def get_spark(app_name: str = "beverage-sales") -> SparkSession:
    
    spark = (
        SparkSession
        .builder
        .appName(app_name)
        .config("spark.driver.memory", "4g")
        .getOrCreate()
    )
    
    return spark
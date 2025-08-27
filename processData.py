from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("CSV_to_HDFS") \
        .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
        .getOrCreate()

    # Path to your input CSV file (local path)
    local_csv_path = "file:///Users/piyush.dixit/Desktop/AdPulse/advertisement.csv"

    # Read CSV into DataFrame
    # set "false" if no header row
    df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(local_csv_path)

    print("DataFrame Schema:")
    df.printSchema()

    # Output path in HDFS
    hdfs_output_path = "hdfs://localhost:9000/Users/piyush.dixit/Desktop/processed_hadoop_output"

    # Save DataFrame back as CSV in HDFS
    df.write \
        .mode("overwrite") \
        .option("header", "true") \
        .csv(hdfs_output_path)

    print(f"CSV successfully written to {hdfs_output_path}")

    spark.stop()

if __name__ == "__main__":
    main()

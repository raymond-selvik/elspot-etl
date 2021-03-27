import os

from spark_utils import spark_session_factory

if __name__ == "__main__":
    path = os.path.abspath(os.path.dirname(__file__))
    config_file_path = os.path.join(path, 'spark-config.json')

    spark = spark_session_factory.createSparkSession(config_file_path)

    print(spark.version)



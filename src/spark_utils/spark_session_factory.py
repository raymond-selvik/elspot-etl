import pyspark
from pyspark import SparkConf
from pyspark.sql import SparkSession

import json


def createSparkSession(sparkConfigFile):
    def createSparkConfig(json):
        spark_conf = SparkConf()

        for key in json:
            spark_conf.set(key, json[key])
        
        return spark_conf

    with open(sparkConfigFile) as file:
        config = json.load(file)

    spark_conf = createSparkConfig(config['config'])
    packages = ','.join(config['packages'])

    return (SparkSession.builder       
        .config(conf = spark_conf)
        .config("spark.jars.packages", packages)
        .getOrCreate())


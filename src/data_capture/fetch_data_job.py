from pyspark.sql import SparkSession

spark = (SparkSession.builder
            .appName("test")
            .master("local")
            .config('spark.jars.packages', 'io.delta:delta-core_2.12:0.8.0')
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
            .getOrCreate())

import pandas as pd
from delta.tables import *




pandas_df = pd.read_html("/mnt/d/programmering/spark/elspot-etl/data/daily.xls", header=2,encoding = 'utf-8', decimal=',', thousands='.')[0]

print(pandas_df)

df = spark.createDataFrame(pandas_df)
df = df.withColumnRenamed('Unnamed: 0', 'Date')

DeltaTable.
delta_table = DeltaTable.forPath(spark, "/home/raysel/delta/elspot" )

#df.write.format('delta').mode('append').save("/home/raysel/delta/elspot")


#delta_df = spark.read.format('delta').load("/home/raysel/delta/elspot").count()

#print(delta_df)
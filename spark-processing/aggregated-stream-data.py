from pyspark import SparkConf,SparkContext 
from pyspark.sql import SparkSession,SQLContext 
from pyspark.sql.functions import *
from pyspark.sql.types import * 

import time 
import datetime 

conf = SparkConf(). \
setAppName("Streaming Data"). \
setMaster("yarn-client")


sc = SparkContext(conf=conf)

sqlcontext = SQLContext(sc)

spark = SparkSession \
        .builder \
        .appName("user-streaming-logs-analysis") \
        .getOrCreate()



streaming_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","spark-rtp-w-1:9092") \
    .option("subscribe","user_browsing_logs") \
    .load() \
    .selectExpr("CAST(value as STRING)")

#Define a schema for the structured data to be used in a dataframe
schema = StructType(
  [
      StructField('category',StringType(),True),
      StructField('date_time',TimestampType(),True),
      StructField('type',StringType(),True),
      StructField('pid',IntegerType(),True),
      StructField('state',StringType(),True),
      StructField('sub_cat',StringType(),True),
      StructField('ip_address',StringType(),True)
  ]
)


df_parsed = streaming_df.select("value")
#Enforcing the schema on the streaming dataframe
df_streaming_visits = df_parsed.withColumn("data",from_json("value",schema)).select(col('data.*'))
#Aggregating the data output
df_aggregated = df_streaming_visits \
          .groupBy(
            df_streaming_visits.category,
            df_streaming_visits.state,
            df_streaming_visits.type) \
          .count()

query = df_aggregated.writeStream \
          .outputMode("complete") \
          .format("console") \
          .start()

query.awaitTermination()

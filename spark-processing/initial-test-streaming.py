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


#Dataframe configuration for kafka
streaming_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","spark-rtp-w-1:9092") \
    .option("subscribe","user_browsing_logs") \
    .load() \
    .selectExpr("CAST(value as STRING)")

#Create an output to console
query = streaming_df.writeStream \
          .outputMode("append") \
          .format("console") \
          .start()

query.awaitTermination()

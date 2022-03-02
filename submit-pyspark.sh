gcloud dataproc jobs submit pyspark \
./initial-test-streaming.py \
--cluster=spark-rtp \
--region=us-east1 \
--jars=jar-files/spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,jar-files/spark-sql-kafka-0-10_2.11-2.4.2.jar 


gcloud dataproc jobs submit pyspark \
./aggregated-stream-data.py \
--cluster=spark-rtp \
--region=us-east1 \
--jars=jar-files/spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,jar-files/spark-sql-kafka-0-10_2.11-2.4.2.jar 


gcloud dataproc jobs submit pyspark ./time-segment-window.py \
--cluster=spark-rtp --region=us-east1 \
--jars=jar-files/spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,jar-files/spark-sql-kafka-0-10_2.11-2.4.2.jar \
--properties spark.jars.packages=org.apache.spark:spark-avro_2.11:2.4.2


gcloud dataproc jobs submit pyspark spark-rtp/most_visited_categories.py \
--cluster=spark-rtp --region=us-east1 \
--jars=jar-files/spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,jar-files/spark-sql-kafka-0-10_2.11-2.4.2.jar \
--properties spark.jars.packages=org.apache.spark:spark-avro_2.11:2.4.2


gcloud dataproc jobs submit pyspark spark-rtp/raw_data_streaming.py \
--cluster=sparksql-rtp --region=asia-northeast1 \
--jars=jar-files/spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,jar-files/spark-sql-kafka-0-10_2.11-2.4.2.jar 


# gcloud dataproc jobs submit pyspark streaming_aggregates.py \
# --cluster=spark-rtp --region=us-east1 \
# --jars=spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,spark-sql-kafka-0-10_2.11-2.4.2.jar

# gcloud dataproc jobs submit pyspark stream-logs.py \
# --cluster=spark-rtp --region=us-east1 \
# --jars=spark-streaming-kafka-0-10-assembly_2.11-2.4.2.jar,spark-sql-kafka-0-10_2.11-2.4.2.jar
"""Import avro file into BigQuery."""

import os 

from google.cloud import bigquery

def upload_user_cart(data,context) :

    client = bigquery.Client()

    bucketname = data['bucket']

    filename = data['name']

    timeCreated = data['timeCreated']

    dataset_id = "website_data_streams"

    dataset_ref = client.dataset(dataset_id)

    job_config = bigquery.LoadJobConfig()

    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

    job_config.autodetect = True 

    job_config.ignore_unknown_values = True

    job_config.source_format = bigquery.SourceFormat.AVRO


    uri = 'gs://%s/%s' % (bucketname,filename)

    load_job = client.load_table_from_uri(uri,dataset_ref.table('cart_products'),job_config=job_config)

    print("Starting Job {}".format(load_job.job_id))

    load_job.result()

    print("Job Finished")

    destination_table = client.get_table(dataset_ref.table('cart_products'))
    print('Loaded {} rows.' .format(destination_table.num_rows))


def update_visits_by_categories(data,context) :

    client = bigquery.Client()

    bucketname = data['bucket']

    filename = data['name']

    timeCreated = data['timeCreated']

    dataset_id = "website_data_streams"

    dataset_ref = client.dataset(dataset_id)

    job_config = bigquery.LoadJobConfig()

    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

    job_config.autodetect = True 

    job_config.ignore_unknown_values = True

    job_config.source_format = bigquery.SourceFormat.AVRO


    uri = 'gs://%s/%s' % (bucketname,filename)

    load_job = client.load_table_from_uri(uri,dataset_ref.table('visits_by_categories'),job_config=job_config)

    print("Starting Job {}".format(load_job.job_id))

    load_job.result()

    print("Job Finished")

    destination_table = client.get_table(dataset_ref.table('visits_by_categories'))
    print('Loaded {} rows.' .format(destination_table.num_rows))
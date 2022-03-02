#!/bin/sh

FUNCTION="upload_user_cart"
BUCKET="gs://website-data-streams"

gcloud functions deploy ${FUNCTION} \
    --runtime python37 \
    --trigger-resource ${BUCKET} \
    --trigger-event google.storage.object.finalize

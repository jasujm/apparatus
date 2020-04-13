#!/bin/bash

bucket=$APPARATUS_BACKUP_S3_BUCKET

if [ ! $bucket ]; then
    echo 'APPARATUS_BACKUP_S3_BUCKET not set.'
fi

scripts/mysqldump.sh | gzip | aws s3 cp - s3://${bucket}/mysqldump-$(date --iso-8601=seconds).gz --storage-class=ONEZONE_IA

#!/bin/bash

bucket=$APPARATUS_BACKUP_S3_BUCKET

if [ ! $bucket ]; then
    echo 'APPARATUS_BACKUP_S3_BUCKET not set.'
fi

scripts/mediadump.sh | gzip | aws s3 cp - s3://${bucket}/mediadump-$(date --iso-8601=seconds).tgz --storage-class=ONEZONE_IA

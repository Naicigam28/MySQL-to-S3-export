import subprocess
import os
import time
import json

S3_BUCKET = os.environ['S3_BUCKET']

timestamp = time.strftime('%Y-%m-%d-%I:%M')


def handler(event, context):
    print("Function started")

    DB_HOST = event['DB_HOST']
    DB_NAME = event['DB_NAME']
    DB_USER = event['DB_USER']
    DB_PASS = event['DB_PASS']

    print("%s %s ".format(DB_HOST, DB_NAME))

    command = "mysqldump -h %s -u %s -p%s %s | gzip -c | aws s3 cp - s3://%s/%s.gz" % (
        DB_HOST, DB_USER, DB_PASS, DB_NAME, S3_BUCKET, DB_NAME + "_" + timestamp)
    subprocess.Popen(command, shell=True).wait()
    print("MySQL backup finished")
    return "backup finished"
import base64
import json
import boto3
import os

def lambda_handler(event, context):
    bucket_name =os.environ['S3_BUCKET_NAME']
    s3_client = boto3.client('s3')
    if 'Records' in event:
        for record in event['Records']:
            data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            
            data_dict = json.loads(data)
            file_key = f'{data_dict["user_id"]}/{data_dict["timestamp"]}.json'
            print(f"Processed: {data_dict}")

            data_json = json.dumps(data_dict)
            try:
                s3_client.put_object(
                    Bucket=bucket_name,
                    Key=file_key,
                    Body=data_json,
                    ContentType='application/json'
                )
            except Exception as e:
                print("Error",e)

            
        return 'Processed all records'
    else:
        print("No records found in the event")
        return 'No records to process'
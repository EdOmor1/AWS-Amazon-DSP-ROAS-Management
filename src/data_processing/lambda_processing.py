import boto3
import json

def lambda_handler(event, context):
    # Initialize AWS services
    s3 = boto3.client('s3')
    
    # Retrieve data from S3 trigger event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Read data from S3 object
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    data = response['Body'].read().decode('utf-8')
    
    # Process data (example: convert to uppercase)
    processed_data = data.upper()
    
    # Upload processed data to another S3 bucket or store in database
    processed_bucket_name = 'processed-data-bucket'
    processed_object_key = 'processed_' + object_key
    s3.put_object(Bucket=processed_bucket_name, Key=processed_object_key, Body=processed_data)
    
    # Return status
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed and stored successfully!')
    }

import boto3
import json
import time

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='your_region')

# Kinesis stream name
stream_name = 'your_kinesis_stream_name'

def put_record_to_kinesis(data):
    try:
        # Put a single record to the Kinesis stream
        response = kinesis.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey='partition_key'
        )
        print("Record sent to Kinesis: {}".format(response['SequenceNumber']))
    except Exception as e:
        print("Error putting record to Kinesis: {}".format(str(e)))

# Example usage
if __name__ == "__main__":
    while True:
        data = {
            'timestamp': int(time.time()),
            'ad_platform': 'platform_name',
            'metric': 'metric_name',
            'value': 123
        }
        put_record_to_kinesis(data)
        time.sleep(1)  # Send data every 1 second (for demonstration purposes)


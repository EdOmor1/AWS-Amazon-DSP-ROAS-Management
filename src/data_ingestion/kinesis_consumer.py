import boto3
import json

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='your_region')

# Kinesis stream name
stream_name = 'your_kinesis_stream_name'

def process_records(records):
    for record in records:
        data = json.loads(record['Data'])
        # Process the data as needed
        print("Received record from Kinesis:", data)

def get_records_from_kinesis():
    try:
        # Get records from Kinesis stream
        response = kinesis.get_records(
            ShardIterator=your_shard_iterator,
            Limit=100  # Maximum number of records to retrieve per call
        )
        records = response['Records']
        if records:
            process_records(records)
    except Exception as e:
        print("Error getting records from Kinesis: {}".format(str(e)))

# Example usage
if __name__ == "__main__":
    while True:
        get_records_from_kinesis()


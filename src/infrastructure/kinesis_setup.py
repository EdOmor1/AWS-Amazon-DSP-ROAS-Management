import boto3

# Initialize Kinesis client
kinesis = boto3.client('kinesis')

def create_kinesis_stream(stream_name, shard_count):
    # Create Kinesis stream
    kinesis.create_stream(StreamName=stream_name, ShardCount=shard_count)
    
    print("Kinesis stream created:", stream_name)

if __name__ == "__main__":
    stream_name = 'my-kinesis-stream'
    shard_count = 1
    create_kinesis_stream(stream_name, shard_count)

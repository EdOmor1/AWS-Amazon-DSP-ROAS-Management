import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def create_s3_bucket(bucket_name):
    # Create S3 bucket
    s3.create_bucket(Bucket=bucket_name)
    
    print("S3 bucket created:", bucket_name)

if __name__ == "__main__":
    bucket_name = 'my-unique-bucket-name'
    create_s3_bucket(bucket_name)

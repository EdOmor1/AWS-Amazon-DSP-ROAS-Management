import boto3

# Initialize Glue client
glue = boto3.client('glue')

def create_glue_crawler(crawler_name, role_arn, database_name, s3_targets):
    # Create Glue crawler
    response = glue.create_crawler(
        Name=crawler_name,
        Role=role_arn,
        DatabaseName=database_name,
        Targets={'S3Targets': s3_targets}
    )
    
    print("Glue crawler created:", response['Crawler']['Name'])

if __name__ == "__main__":
    crawler_name = 'my-glue-crawler'
    role_arn = 'arn:aws:iam::123456789012:role/glue-crawler-role'
    database_name = 'my-glue-database'
    s3_targets = [{'Path': 's3://my-input-data-bucket'}]
    create_glue_crawler(crawler_name, role_arn, database_name, s3_targets)

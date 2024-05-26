import boto3

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

def create_dynamodb_table(table_name):
    # Create DynamoDB table
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'N'}
        ],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    
    print("DynamoDB table created:", table_name)

if __name__ == "__main__":
    table_name = 'my-dynamodb-table'
    create_dynamodb_table(table_name)

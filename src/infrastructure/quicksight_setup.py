import boto3

# Initialize QuickSight client
quicksight = boto3.client('quicksight')

def create_quicksight_dataset(dataset_name, data_source_arn, aws_account_id):
    # Create QuickSight dataset
    response = quicksight.create_dataset(
        AwsAccountId=aws_account_id,
        DataSetId=dataset_name,
        Name=dataset_name,
        PhysicalTableMap={
            'PrimaryDataSource': {
                'S3Source': {
                    'DataSourceArn': data_source_arn,
                    'InputColumns': [
                        {
                            'Name': 'column_name',
                            'Type': 'STRING'
                        }
                    ]
                }
            }
        },
        ImportMode='SPICE',
        Permissions=[
            {
                'Principal': 'arn:aws:iam::123456789012:root',
                'Actions': ['quicksight:DescribeDataSet', 'quicksight:DescribeDataSetPermissions', 'quicksight:PassDataSet', 'quicksight:DescribeIngestion', 'quicksight:ListIngestions', 'quicksight:UpdateDataSet', 'quicksight:DeleteDataSet']
            }
        ]
    )
    
    print("QuickSight dataset created:", response['Arn'])

if __name__ == "__main__":
    dataset_name = 'my-quicksight-dataset'
    data_source_arn = 'arn:aws:quicksight:us-east-1:123456789012:datasource/my-data-source'
    aws_account_id = '123456789012'
    create_quicksight_dataset(dataset_name, data_source_arn, aws_account_id)

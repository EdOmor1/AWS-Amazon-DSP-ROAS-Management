import boto3

# Initialize RDS client
rds = boto3.client('rds')

def create_rds_instance(instance_name):
    # Create RDS instance
    response = rds.create_db_instance(
        DBInstanceIdentifier=instance_name,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword='password',
        AllocatedStorage=20
    )
    
    print("RDS instance created with ID:", response['DBInstance']['DBInstanceIdentifier'])

if __name__ == "__main__":
    instance_name = 'my-rds-instance'
    create_rds_instance(instance_name)

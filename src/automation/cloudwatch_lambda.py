import boto3

def lambda_handler(event, context):
    # Initialize AWS services
    ec2 = boto3.client('ec2')
    
    # Retrieve instance IDs from event
    instance_ids = [instance['instanceId'] for instance in event['detail']['instances']]
    
    # Stop instances
    ec2.stop_instances(InstanceIds=instance_ids)
    
    return {
        'statusCode': 200,
        'body': 'Instances stopped successfully!'
    }

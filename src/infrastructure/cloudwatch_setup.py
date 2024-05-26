import boto3

# Initialize CloudWatch client
cloudwatch = boto3.client('cloudwatch')

def create_cloudwatch_alarm(instance_id):
    # Create CloudWatch alarm
    cloudwatch.put_metric_alarm(
        AlarmName='CPUUtilizationAlarm',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=60,
        Statistic='Average',
        Threshold=90.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when CPU utilization exceeds 90%',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        Unit='Percent'
    )
    
    print("CloudWatch alarm created for instance:", instance_id)

if __name__ == "__main__":
    instance_id = 'your-instance-id'
    create_cloudwatch_alarm(instance_id)

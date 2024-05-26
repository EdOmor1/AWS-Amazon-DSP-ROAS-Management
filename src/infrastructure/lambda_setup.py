import boto3

# Initialize Lambda client
lambda_client = boto3.client('lambda')

def create_lambda_function(function_name, handler, role_arn, runtime, code_bucket, code_key):
    # Create Lambda function
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler,
        Code={'S3Bucket': code_bucket, 'S3Key': code_key}
    )
    
    print("Lambda function created:", response['FunctionArn'])

if __name__ == "__main__":
    function_name = 'my-lambda-function'
    handler = 'lambda_function.lambda_handler'
    role_arn = 'arn:aws:iam::123456789012:role/lambda-execution-role'
    runtime = 'python3.8'
    code_bucket = 'my-lambda-code-bucket'
    code_key = 'lambda_function.zip'
    create_lambda_function(function_name, handler, role_arn, runtime, code_bucket, code_key)

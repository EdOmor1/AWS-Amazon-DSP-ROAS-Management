import boto3

# Initialize VPC client
ec2 = boto3.client('ec2')

def create_vpc():
    # Create VPC
    response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = response['Vpc']['VpcId']
    
    # Add name tag to VPC
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': 'MyVPC'}])
    
    print("VPC created with ID:", vpc_id)
    return vpc_id

if __name__ == "__main__":
    create_vpc()

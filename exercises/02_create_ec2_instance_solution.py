"""
Solution 2: Create a New EC2 Instance

This solution demonstrates how to create a new EC2 instance using boto3.
"""

import boto3


def create_ec2_instance(ami_id, instance_type, key_name=None):
    """
    Create a new EC2 instance.
    
    Args:
        ami_id (str): The ID of the AMI to use
        instance_type (str): The instance type (e.g., 't2.micro', 't2.small')
        key_name (str, optional): The name of the key pair to use
    
    Returns:
        str: The instance ID of the newly created instance
    """
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    # Prepare parameters for instance creation
    params = {
        'ImageId': ami_id,
        'InstanceType': instance_type,
        'MinCount': 1,
        'MaxCount': 1
    }
    
    # Add key name if provided
    if key_name:
        params['KeyName'] = key_name
    
    # Create the instance
    response = ec2_client.run_instances(**params)
    
    # Extract and return the instance ID
    instance_id = response['Instances'][0]['InstanceId']
    
    return instance_id


def create_ec2_instance_with_tags(ami_id, instance_type, key_name=None, tags=None):
    """
    Create a new EC2 instance with tags.
    
    Args:
        ami_id (str): The ID of the AMI to use
        instance_type (str): The instance type (e.g., 't2.micro', 't2.small')
        key_name (str, optional): The name of the key pair to use
        tags (dict, optional): Dictionary of tags to apply to the instance
    
    Returns:
        str: The instance ID of the newly created instance
    """
    ec2_client = boto3.client('ec2')
    
    # Prepare parameters
    params = {
        'ImageId': ami_id,
        'InstanceType': instance_type,
        'MinCount': 1,
        'MaxCount': 1
    }
    
    if key_name:
        params['KeyName'] = key_name
    
    # Add tags if provided
    if tags:
        tag_specifications = [{
            'ResourceType': 'instance',
            'Tags': [{'Key': k, 'Value': v} for k, v in tags.items()]
        }]
        params['TagSpecifications'] = tag_specifications
    
    # Create the instance
    response = ec2_client.run_instances(**params)
    instance_id = response['Instances'][0]['InstanceId']
    
    return instance_id


def wait_for_instance_running(instance_id):
    """
    Wait for an EC2 instance to reach the running state.
    
    Args:
        instance_id (str): The ID of the instance to wait for
    """
    ec2_client = boto3.client('ec2')
    
    # Use waiter to wait for instance to be running
    waiter = ec2_client.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    
    print(f"Instance {instance_id} is now running")


if __name__ == "__main__":
    # Example usage (commented out to avoid accidental instance creation)
    
    # Basic instance creation
    # Note: AMI IDs are region-specific. Use a valid AMI ID for your region.
    # ami_id = "ami-0c55b159cbfafe1f0"  # Example AMI ID - replace with your own
    # instance_type = "t2.micro"
    # key_name = "my-key-pair"
    # instance_id = create_ec2_instance(ami_id, instance_type, key_name)
    # print(f"Created instance: {instance_id}")
    
    # Instance creation with tags
    # tags = {
    #     'Name': 'My Test Instance',
    #     'Environment': 'Development',
    #     'Project': 'Boto3 Learning'
    # }
    # instance_id = create_ec2_instance_with_tags(ami_id, instance_type, key_name, tags)
    # print(f"Created instance with tags: {instance_id}")
    
    # Wait for instance to be running
    # wait_for_instance_running(instance_id)
    
    print("Solution demonstrates three approaches:")
    print("1. Basic instance creation")
    print("2. Instance creation with tags")
    print("3. Waiting for instance to reach running state")

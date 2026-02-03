"""
Exercise 2: Create a New EC2 Instance

Task:
Write a function that creates a new EC2 instance with specified parameters.

Instructions:
1. Use the boto3 library to interact with AWS EC2
2. Create a function called `create_ec2_instance()` that:
   - Accepts parameters: ami_id, instance_type, key_name (optional)
   - Creates a new EC2 instance with the specified configuration
   - Returns the instance ID of the newly created instance

Example:
    >>> instance_id = create_ec2_instance('ami-0c55b159cbfafe1f0', 't2.micro', 'my-key-pair')
    >>> print(instance_id)
    'i-1234567890abcdef0'

Hints:
- Use boto3.client('ec2') to create an EC2 client
- Use the run_instances() method
- The method returns a response with instance information
- Extract the InstanceId from the response

Important:
- In a real scenario, you need proper AWS credentials and permissions
- This exercise is for learning purposes - test with mock data or a sandbox environment
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
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your function (replace with your own values)
    # Note: AMI IDs are region-specific. Use a valid AMI ID for your region.
    ami_id = "ami-0c55b159cbfafe1f0"  # Example AMI ID - replace with your own
    instance_type = "t2.micro"
    key_name = "my-key-pair"
    
    # Note: This will actually create an instance if you have AWS credentials configured
    # Comment out the following lines to avoid accidental charges
    # instance_id = create_ec2_instance(ami_id, instance_type, key_name)
    # print(f"Created instance: {instance_id}")
    
    print("Remember to uncomment the test code when you're ready to test with real AWS credentials")

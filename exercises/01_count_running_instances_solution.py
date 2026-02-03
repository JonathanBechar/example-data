"""
Solution 1: Count Running EC2 Instances

This solution demonstrates how to count EC2 instances in the "running" state.
"""

import boto3


def count_running_instances():
    """
    Count the number of EC2 instances in running state.
    
    Returns:
        int: The number of running EC2 instances
    """
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    # Describe all instances
    response = ec2_client.describe_instances()
    
    # Count running instances
    running_count = 0
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                running_count += 1
    
    return running_count


def count_running_instances_with_filter():
    """
    Alternative solution: Use filters to get only running instances.
    This is more efficient as filtering happens on the AWS side.
    
    Returns:
        int: The number of running EC2 instances
    """
    ec2_client = boto3.client('ec2')
    
    # Use filters to get only running instances
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )
    
    # Count instances
    running_count = 0
    for reservation in response['Reservations']:
        running_count += len(reservation['Instances'])
    
    return running_count


if __name__ == "__main__":
    # Test both solutions
    count1 = count_running_instances()
    print(f"Number of running instances (method 1): {count1}")
    
    count2 = count_running_instances_with_filter()
    print(f"Number of running instances (method 2): {count2}")

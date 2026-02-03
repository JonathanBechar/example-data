"""
Exercise 1: Count Running EC2 Instances

Task:
Write a function that counts how many EC2 instances are currently in the "running" state.

Instructions:
1. Use the boto3 library to interact with AWS EC2
2. Create a function called `count_running_instances()` that:
   - Uses boto3 to describe all EC2 instances
   - Filters for instances in the "running" state
   - Returns the total count of running instances

Example:
    >>> count_running_instances()
    3

Hints:
- Use boto3.client('ec2') to create an EC2 client
- Use the describe_instances() method
- Check the 'State' -> 'Name' field for each instance
- The state should be 'running' (code 16)

Test your solution with the example data in ../boto3_ec2_describe_instances.json
"""

import boto3


def count_running_instances():
    """
    Count the number of EC2 instances in running state.
    
    Returns:
        int: The number of running EC2 instances
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your function
    count = count_running_instances()
    print(f"Number of running instances: {count}")

"""
Exercise 3: Get External IP Addresses of EC2 Instances

Task:
Write a function that retrieves the external (public) IP addresses of all EC2 instances.

Instructions:
1. Use the boto3 library to interact with AWS EC2
2. Create a function called `get_external_ips()` that:
   - Uses boto3 to describe all EC2 instances
   - Extracts the public IP address for each instance
   - Returns a dictionary mapping instance IDs to their public IP addresses
   - Excludes instances that don't have a public IP address

Example:
    >>> ips = get_external_ips()
    >>> print(ips)
    {
        'i-0123456789abcdef0': '54.123.45.67',
        'i-0abcdef123456789a': '54.234.56.78',
        'i-0fedcba987654321b': '54.345.67.89'
    }

Hints:
- Use boto3.client('ec2') to create an EC2 client
- Use the describe_instances() method
- Look for the 'PublicIpAddress' field in each instance
- Some instances might not have a public IP (e.g., instances in private subnets)
- Use the 'InstanceId' as the key and 'PublicIpAddress' as the value

Test your solution with the example data in ../boto3_ec2_describe_instances.json
"""

import boto3


def get_external_ips():
    """
    Get the external (public) IP addresses of all EC2 instances.
    
    Returns:
        dict: A dictionary mapping instance IDs to public IP addresses
              Format: {'instance-id': 'public-ip', ...}
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your function
    ips = get_external_ips()
    print("External IP addresses:")
    for instance_id, ip_address in ips.items():
        print(f"  {instance_id}: {ip_address}")

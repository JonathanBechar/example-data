"""
Solution 3: Get External IP Addresses of EC2 Instances

This solution demonstrates how to retrieve public IP addresses from EC2 instances.
"""

import boto3


def get_external_ips():
    """
    Get the external (public) IP addresses of all EC2 instances.
    
    Returns:
        dict: A dictionary mapping instance IDs to public IP addresses
              Format: {'instance-id': 'public-ip', ...}
    """
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    # Describe all instances
    response = ec2_client.describe_instances()
    
    # Extract public IPs
    ip_mapping = {}
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            # Check if the instance has a public IP address
            if 'PublicIpAddress' in instance:
                ip_mapping[instance_id] = instance['PublicIpAddress']
    
    return ip_mapping


def get_external_ips_with_state(state_filter=None):
    """
    Get external IP addresses of EC2 instances with optional state filtering.
    
    Args:
        state_filter (str, optional): Filter by instance state (e.g., 'running', 'stopped')
    
    Returns:
        dict: A dictionary mapping instance IDs to public IP addresses
    """
    ec2_client = boto3.client('ec2')
    
    # Prepare parameters with optional filter
    params = {}
    if state_filter:
        params['Filters'] = [
            {
                'Name': 'instance-state-name',
                'Values': [state_filter]
            }
        ]
    
    response = ec2_client.describe_instances(**params)
    
    ip_mapping = {}
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if 'PublicIpAddress' in instance:
                ip_mapping[instance['InstanceId']] = instance['PublicIpAddress']
    
    return ip_mapping


def get_detailed_instance_info():
    """
    Get detailed information about instances including both public and private IPs.
    
    Returns:
        list: A list of dictionaries with instance details
    """
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    
    instances_info = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                'PublicDnsName': instance.get('PublicDnsName', 'N/A')
            }
            instances_info.append(info)
    
    return instances_info


if __name__ == "__main__":
    # Test basic solution
    print("=== All instances with public IPs ===")
    ips = get_external_ips()
    for instance_id, ip_address in ips.items():
        print(f"  {instance_id}: {ip_address}")
    
    # Test with state filter
    print("\n=== Running instances with public IPs ===")
    running_ips = get_external_ips_with_state('running')
    for instance_id, ip_address in running_ips.items():
        print(f"  {instance_id}: {ip_address}")
    
    # Test detailed info
    print("\n=== Detailed instance information ===")
    details = get_detailed_instance_info()
    for info in details:
        print(f"  {info['InstanceId']} ({info['State']}):")
        print(f"    Type: {info['InstanceType']}")
        print(f"    Private IP: {info['PrivateIpAddress']}")
        print(f"    Public IP: {info['PublicIpAddress']}")
        print(f"    Public DNS: {info['PublicDnsName']}")

# Boto3 EC2 Exercises

This directory contains Python exercises for learning AWS EC2 management using the boto3 library.

## Prerequisites

Before starting these exercises, you should:
1. Install boto3: `pip install boto3`
2. Have basic Python knowledge
3. Understand basic AWS EC2 concepts
4. (Optional) Have AWS credentials configured for testing with real AWS resources

## Exercises

### Exercise 1: Count Running EC2 Instances
**File:** `01_count_running_instances.py`  
**Solution:** `01_count_running_instances_solution.py`

Learn how to:
- Connect to AWS EC2 using boto3
- Describe EC2 instances
- Filter instances by state
- Count running instances

### Exercise 2: Create a New EC2 Instance
**File:** `02_create_ec2_instance.py`  
**Solution:** `02_create_ec2_instance_solution.py`

Learn how to:
- Create EC2 instances programmatically
- Specify instance parameters (AMI, instance type, key pair)
- Add tags to instances
- Wait for instances to reach running state

**Warning:** This exercise can create real AWS resources and incur charges. Test carefully!

### Exercise 3: Get External IP Addresses
**File:** `03_get_external_ips.py`  
**Solution:** `03_get_external_ips_solution.py`

Learn how to:
- Retrieve instance details
- Extract public IP addresses
- Handle instances without public IPs
- Filter instances by state
- Get comprehensive instance information

## How to Use

1. **Start with the exercise file** (e.g., `01_count_running_instances.py`)
2. **Read the instructions** carefully in the docstring
3. **Implement the function** replacing the `pass` statement
4. **Test your implementation** using the `if __name__ == "__main__"` block
5. **Compare with the solution** file when you're done or stuck

## Testing with Example Data

This repository includes example EC2 API responses in the parent directory:
- `../boto3_ec2_describe_instances.json` - Sample describe_instances() response

You can use these files to understand the structure of AWS API responses without making actual API calls.

## AWS Credentials

To run these exercises against real AWS resources, you need to configure AWS credentials:

```bash
# Option 1: Using AWS CLI
aws configure

# Option 2: Environment variables
export AWS_ACCESS_KEY_ID='your-access-key'
export AWS_SECRET_ACCESS_KEY='your-secret-key'
export AWS_DEFAULT_REGION='us-east-1'

# Option 3: Credentials file
# Create ~/.aws/credentials with:
# [default]
# aws_access_key_id = your-access-key
# aws_secret_access_key = your-secret-key
```

## Learning Path

Recommended order:
1. Start with Exercise 1 (read operations, safe to test)
2. Move to Exercise 3 (more complex read operations)
3. Finish with Exercise 2 (write operations, requires caution)

## Additional Resources

- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)
- [Boto3 EC2 Examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-examples.html)

## Tips

- Always test with read-only operations first (describe, list, get)
- Be careful with operations that create resources (they may incur costs)
- Use filters in API calls to reduce data transfer and improve performance
- Always clean up resources you create during testing
- Consider using AWS Free Tier eligible instance types (t2.micro) for testing

import boto3
from dotenv import load_dotenv
import argparse

load_dotenv()

client = boto3.client("ec2", region_name="us-east-1")

# response = client.create_vpc(
#     CidrBlock = "10.0.0.0/16",
# )

# vpc_id = response["Vpc"]["VpcId"]

# response = client.create_subnet(
#     CidrBlock="10.0.1.0/24",
#     VpcId=vpc_id,
# )

# response = client.delete_subnet(
    # SubnetId="02e105184e1285a86",
# )

# We need 3 computers (instances) - t2.microm t2.small, t2.medium
# t2.medium is expensive, so we want it shut down! The rest should be running

def create_default_instance(instance_type: str):
    return client.run_instances(
        ImageId="ami-0c1fe732b5494dc14",
        InstanceType=instance_type,
        MaxCount=1,
        MinCount=1,
        SubnetId="subnet-02e105184e1285a86",
    )

def solve_homework():
    for instance_type in ["t2.micro", "t2.small", "t2.medium"]:
        response = create_default_instance(instance_type)
    last_id = response["Instances"][0]["InstanceId"]
    client.get_waiter("instance_running").wait(InstanceIds=[last_id])
    client.stop_instances(InstanceIds=[last_id])

def terminate_all_ec2():
    response = client.describe_instances()
    ids = []
    for res in response["Reservations"]:
        for instance in res["Instances"]:
            ids.append(instance["InstanceId"])
    client.terminate_instances(InstanceIds=ids)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--terminate", action="store_true")
    args = parser.parse_args()
    if args.terminate:
        terminate_all_ec2()
    else:
        solve_homework()

# stop_ids = []
# while len(stop_ids) == 0:
#     response = client.describe_instances()
#     for res in response["Reservations"]:
#         for instance in res['Instances']:
#             if instance["InstanceType"] == "t2.medium" and instance["State"]["Name"] == "running":
#                 instance_id = instance["InstanceId"]
#                 stop_ids.append(instance_id)

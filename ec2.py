from dotenv import load_dotenv
import boto3
from time import sleep 

load_dotenv()


def get_ec2_instances(ec2) -> list[dict]:
    response = ec2.describe_instances()
    instances = []
    for res in response["Reservations"]:
        for instance in res["Instances"]:
            instances.append(instance)
    return instances
    # with open("boto3_ec2_describe_instances.json") as f:
    # response = json.load(f)
    # instances = response["Reservations"][0]["Instances"]
    # return instances


def stop_instances(ec2, ids: list[str]):
    response = ec2.stop_instances(InstanceIds=ids)
    print(response)


def start_instances(ec2, ids: list[str]):
    response = ec2.start_instances(InstanceIds=ids)
    print(response)


def is_instance_running(instance: dict) -> bool:
    return instance["State"]["Name"] == "running"    


def get_running_instances(instances: list[dict]) -> dict:
    result =  {
        "total": len(instances),
        "running": 0
    }
    running = filter(is_instance_running, instances)
    result["running"] = len(list(running))
    # for instance in instances:
    #     if instance["State"]["Name"] == "running":
    #         result["running"] += 1
    return result


if __name__ == "__main__":
    ec2 = boto3.client("ec2")
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket="jb-yonatanb-devops-example-1")
    s3.upload_file(Filename="1.txt", Key="folder1/uploads/file.txt", Bucket="jb-yonatanb-devops-example-1")
    s3.upload_file(Body=b"This file is cool", Key="folder1/uploads/file.txt", Bucket="jb-yonatanb-devops-example-1")
    s3.download_file(Filename="new.txt", Key="folder1/uploads/file.txt", Bucket="jb-yonatanb-devops-example-1")
    s3.list_objects_v2(Bucket="jb-yonatanb-devops-example-1")
    s3.list_objects_v2(Bucket="jb-yonatanb-devops-example-1", Prefix="uploads/")

    # Example - use resources instead of the low-level client
    # ec2 = boto3.resource("ec2")
    # instances = ec2.instances.all()
    # for instance in instances:
    #     print(instance.state)


    # Homework:
    # python3 ec2.py
    # List all the ec2 computer ids and their state
    # Example:
    # 1. t2.micro(i-05a725e4503ec17b0) - Running
    # 2. t2.micro(i-0a46993c077680f08) - Stopped
    # Choose a machine to change state(from running to stopped, or from stopped to running): 1
    # 
    # python ec2.py list
    # Only print the list of stats, without waiting for user input, and exit
    # 
    # python ec2.py --stop i-0a46993c077680f08 i-05a725e4503ec17b0
    # python ec2.py --start i-0a46993c077680f08 i-05a725e4503ec17b0


    instances = get_ec2_instances(ec2)
    result = get_running_instances(instances)
    print(result)
    stop_instances(ec2, ["i-0a46993c077680f08"])
    start_instances(ec2, ["i-05a725e4503ec17b0"])
    sleep(10)
    result = get_running_instances(instances)
    print(result)

from dotenv import load_dotenv
import boto3
from argparse import ArgumentParser
import json
from pydantic import BaseModel
import logging


load_dotenv()


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


def is_instance_running(instance: dict) -> bool:
    return instance["State"]["Name"] == "running"    


def get_ec2_instances(ec2) -> list[dict]:
    if ec2 is None:
        with open("ec2.json") as f:
            response = json.load(f)
            instances = response["Reservations"][0]["Instances"]
    else:
        response = ec2.describe_instances()
    return instances


def print_all_instances(instances: list[dict]):
    for number, instance in enumerate(instances):
        instance_type = instance["InstanceType"]
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"].capitalize()
        entry = f"{number + 1}. {instance_type} ({instance_id}) - {state}"
        print(entry)


def flip_instance_state(instance: dict):
    if instance["State"]["Name"] == "running":
        print("Stopping instance")
    else:
        print("Starting instance")


def stop_instances(ec2, ids: list[str]):
    response = ec2.stop_instances(InstanceIds=ids)
    print(response)


def start_instances(ec2, ids: list[str]):
    response = ec2.start_instances(InstanceIds=ids)
    print(response)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--list", help="Lists the existing instances without waiting for action", action="store_true")
    parser.add_argument("--stop", help="Stops the given instance id", nargs="+", default=[])
    parser.add_argument("--start", help="Starts the given instance id", nargs="+", default=[])
    args = parser.parse_args()
    
# Homework 03.02.2026:
# python3 ec2.py
# List all the ec2 computer ids and their state
# Example:
# 1. t2.micro(i-05a725e4503ec17b0) - Running
# 2. t2.micro(i-0a46993c077680f08) - Stopped
# Choose a machine to change state(from running to stopped, or from stopped to running): 1
    ec2 = boto3.client("ec2")
    instances = get_ec2_instances(None)
    running = get_running_instances(instances)
    print(running)
    print_all_instances(instances)
    
    # python ec2.py --list
    # Only print the list of stats, without waiting for user input, and exit
    if not args.list:
        while True:
            user_choice = input("Choose a machine to change state (running=>stopped,stopped=>running): ")
            try:
                user_choice = int(user_choice)
                if user_choice > len(instances) or user_choice <= 0:
                    print("The number you selected out of range")
                else:
                    break
            except ValueError:
                print("Please enter only numbers")
        flip_instance_state(instances[user_choice - 1])

    # python ec2.py --stop i-0a46993c077680f08 i-05a725e4503ec17b0
    # python ec2.py --start i-0a46993c077680f08 i-05a725e4503ec17b0
    if args.start:
        start_instances(ec2, args.start)
    if args.stop:
        stop_instances(ec2, args.stop)
 

# Homework 08.02.2026:
# add a logging system to the program
# add pydantic classes to the program







# Example - use resources instead of the low-level client
    # ec2 = boto3.resource("ec2")
    # instances = ec2.instances.all()
    # for instance in instances:
    #     print(instance.state)
    # s3 = boto3.client("s3")
    # s3.create_bucket(Bucket="jb-yonatanb-devops-example-1")
    # s3.upload_file(Filename="1.txt", Key="folder1/uploads/file.txt", Bucket="jb-yonatanb-devops-example-1")
    # s3.upload_file(Body=b"This file is cool", Key="folder1/uploads/file.txt", Bucket="jb-yonatanb-devops-example-1")
    # s3.download_file(Filename="new.txt", Key="folder1/uploads/file.txt", Bucket="jb-yonatanb-devops-example-1")
    # s3.list_objects_v2(Bucket="jb-yonatanb-devops-example-1")
    # s3.list_objects_v2(Bucket="jb-yonatanb-devops-example-1", Prefix="uploads/")
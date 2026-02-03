import json


def get_ec2_instances() -> list[dict]:
    try:
        with open("boto3_ec2_describe_instances.json") as f:
            response = json.load(f)
        instances = response["Reservations"][0]["Instances"]
    except json.JSONDecodeError as e:
        print(e)
    return instances


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


instances = get_ec2_instances()
result = get_running_instances(instances)
print(result)

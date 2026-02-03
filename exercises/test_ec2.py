from ec2 import get_ec2_instances, get_running_instances

def test_get_running():
    instances = get_ec2_instances()
    result = get_running_instances(instances)
    assert result["total"] == 2
    assert result["running"] == 2

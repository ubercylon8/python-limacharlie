import os
import argparse
import limacharlie
import getpass

def get_api_key():
    return os.environ['LIMACHARLIE_API_KEY']

def get_oid():
    return os.environ['LIMACHARLIE_OID']

def list_sensors(manager):
    for sensor in manager.sensors():
        hostname = sensor.hostname()
        print(f"Sensor ID: {sensor.sid}, Hostname: {hostname}")

def execute_task(manager, sensor_id, task, investigation_id=None):
    sensor = manager.sensor(sensor_id)
    response = sensor.task([task], inv_id=investigation_id)
    print(response)

def main():
    parser = argparse.ArgumentParser(description='Interact with LimaCharlie sensors.')
    parser.add_argument('--list', action='store_true', help='List all online sensors')
    parser.add_argument('--execute', metavar='SENSOR_ID,TASK', help='Execute a task on a given sensor')
    parser.add_argument('--inv_id', metavar='INVESTIGATION_ID', help='Specify an investigation ID')
    args = parser.parse_args()

    api_key = get_api_key()
    oid = get_oid()
    manager = limacharlie.Manager(oid=oid, secret_api_key=api_key)

    if args.list:
        list_sensors(manager)
    elif args.execute:
        sensor_id, task = args.execute.split(',')
        execute_task(manager, sensor_id, task, args.inv_id)

if __name__ == '__main__':
    main()
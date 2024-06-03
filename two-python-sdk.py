import os
import argparse
import limacharlie

def get_api_key():
    return os.environ['LIMACHARLIE_API_KEY']

def list_sensors(manager):
    for sensor in manager.sensors():
        print(sensor)

def execute_task(manager, sensor_id, task):
    sensor = manager.sensor(sensor_id)
    response = sensor.task(task)
    print(response)

def main():
    parser = argparse.ArgumentParser(description='Interact with LimaCharlie sensors.')
    parser.add_argument('--list', action='store_true', help='List all online sensors')
    parser.add_argument('--execute', metavar='SENSOR_ID,TASK', help='Execute a task on a given sensor')
    args = parser.parse_args()

    api_key = get_api_key()
    manager = limacharlie.Manager(api_key)

    if args.list:
        list_sensors(manager)
    elif args.execute:
        sensor_id, task = args.execute.split(',')
        execute_task(manager, sensor_id, task)

if __name__ == '__main__':
    main()
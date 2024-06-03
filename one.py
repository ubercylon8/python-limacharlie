import os
import json
import requests
import argparse

BASE_URL = 'https://api.limacharlie.io'

def get_api_key():
    return os.environ['LIMACHARLIE_API_KEY']

def list_sensors(api_key):
    response = requests.get(f'{BASE_URL}/sensors/online', headers={'Authorization': api_key})
    sensors = response.json()
    for sensor in sensors:
        print(sensor)

def execute_task(api_key, sensor_id, task):
    response = requests.post(f'{BASE_URL}/sensor/{sensor_id}/task', headers={'Authorization': api_key}, json={'task': task})
    print(response.json())

def main():
    parser = argparse.ArgumentParser(description='Interact with LimaCharlie sensors.')
    parser.add_argument('--list', action='store_true', help='List all online sensors')
    parser.add_argument('--execute', metavar='SENSOR_ID,TASK', help='Execute a task on a given sensor')
    args = parser.parse_args()

    api_key = get_api_key()

    if args.list:
        list_sensors(api_key)
    elif args.execute:
        sensor_id, task = args.execute.split(',')
        execute_task(api_key, sensor_id, task)

if __name__ == '__main__':
    main()
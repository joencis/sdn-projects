
import requests
import json
import csv
import time


def devices_func():
    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    try:
        response = requests.request('GET', url, headers=headers, data=payload)
        response.raise_for_status()
        resultado = response.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    print(resultado)

    url2 = "https://api.meraki.com/api/v1/organizations/681155/devices"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    try:
        response_devices = requests.request(
            'GET', url2, headers=headers, data=payload)
        response_devices.raise_for_status()
        resultado_devices = json.loads(response_devices.text)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    parsed_devices = []
    counter = 0
    for device in resultado_devices:
        if device['productType'] == 'wireless' or device['productType'] == 'appliance':
            parsed_devices.append(device)

    with open('devices.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for device in parsed_devices:
            for key, value in device.items():
                if key == "name" or key == "model" or key == "serial" or key == "mac" or key == "lanIp":
                    writer.writerow([key, value])
                    print([key, value])


if __name__ == '__main__':
    # call devices_func every 5 minutes
    while(True):
        devices_func()
        time.sleep(5)

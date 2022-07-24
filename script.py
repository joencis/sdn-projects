
import requests
import json
import csv
url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response_orgs = requests.request('GET', url, headers=headers, data=payload)
resultado_org = json.loads(response_orgs.text)
# print(resultado_orgs)


url2 = "https://api.meraki.com/api/v1/organizations/681155/devices"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response_devices = requests.request('GET', url2, headers=headers, data=payload)
resultado_devices = json.loads(response_devices.text)
# print(resultado_devices)
parsed_devices = []
counter = 0
for device in resultado_devices:
    if device['productType'] == 'wireless' or device['productType'] == 'appliance':
        parsed_devices.append(device)
        counter = counter+1
print(counter)
print(parsed_devices)

with open('devices.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for device in parsed_devices:
        for key, value in device.items():
            if key == "name" or key == "model" or key == "serial" or key == "mac" or key == "lanIp":
                writer.writerow([key, value])
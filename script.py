
import requests
import json
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

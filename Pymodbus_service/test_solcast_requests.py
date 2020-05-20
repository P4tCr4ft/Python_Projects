# Test code to send scada readings to Solcast using requests library
# Using the authorization for Beryl Solar Farm, and using
# a measurement obtained from Beryl as well.

import requests

# Json payload can be a python dictionary using requests library
payload = {"measurement":{
    "network_constraint": False, "total_power": 63.9, "availability": 100,
    "period_end": "2020-04-12T01:10:00Z", "period": "PT15S", "mean_ghi": 810
}}

auth_token = 'LVz_qx3bo9YczaTCAjwB5P0IbvJRllRO'
head_info = {'Authorization': 'Bearer ' + auth_token}

url = 'https://api.solcast.com.au/utility_scale_sites/0a7b-bb8c-f2ed-d983/measurements'

response = requests.post(url, json=payload, headers=head_info)

print(response)
print(response.json())

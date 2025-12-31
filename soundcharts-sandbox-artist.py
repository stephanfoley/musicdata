import requests

headers = {
    "x-app-id": "soundcharts",
    "x-api-key": "soundcharts"
}

# The UUID for Billie Eilish
uuid = '11e81bcc-9c1c-ce38-b96b-a0369fe50396'

url = 'https://customer.api.soundcharts.com/api/v2/artist/' + uuid

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data.get('object'))
else:
    print('Error ' + response.status_code + ':' + response.text)

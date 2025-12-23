import requests

url = "http://127.0.0.1:5000/moisture"

data = {
    "sensor_id": 1,
    "moisture_level": 25
}

response = requests.post(url, json=data)
print(response.text)

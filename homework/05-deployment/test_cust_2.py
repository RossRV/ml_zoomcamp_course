import requests


url = "http://localhost:9696/predict"

client = customer  = {
    "job": "management", 
    "duration": 400, 
    "poutcome": "success"
}
response = requests.post(url, json=client).json()

print(response)
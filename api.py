import requests

r = requests.get("https://api.sampleapis.com/futurama/info")

if r.status_code != 200:
    print("Error")

data = r.json()

print(data[0]["synopsis"].split()[-1])
import requests
import json

print(
    json.loads(requests.get("http://127.0.0.1:5000/interseccion/1").json())[0]
    )

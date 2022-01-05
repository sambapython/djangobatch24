import requests 

url = "http://localhost:8000/api/category/"
username="admin"
password="admin"
resp = requests.post(url, json={"name":"apicatauth8","discount":25}, auth=(username,password))
resp = requests.get(url)
print(resp.json())
#from rest_framework import authtoken
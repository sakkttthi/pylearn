import requests
import json

get_users_url = 'https://reqres.in/api/users'
post_users_url = 'https://reqres.in/api/users'

mydict = {
    "name": "morpheus",
    "job": "leader"
}

# Json & data are same with key:value pairs
x = requests.post(post_users_url, json=mydict, timeout=1) 
y = requests.post(post_users_url, data=mydict)
print(x.status_code)
print(x.text)
print(y.text)

# Validation
response_body = x.json()
name = response_body["name"]
assert name == mydict["name"]


# Pass files as body
payload_file = open('thisnewfile.txt', "r")
json_file = json.load(payload_file) #json.load loads the file
z = requests.post(post_users_url, files=json_file) 
print(z.status_code)


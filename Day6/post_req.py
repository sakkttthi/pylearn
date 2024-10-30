import requests

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

# Pass files as body
# z = requests.post(post_users_url, files="location of file") 



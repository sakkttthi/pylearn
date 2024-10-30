# Install request - pip install requests 
# Check insallation - pip list 

import requests

url = 'https://reqres.in/api'
uri = '/users?page=2'
print(url+uri)
# Get 
x = requests.get(url+uri)
print(x.status_code)

assert x.status_code == 200 #to compare & validate the response

id={
"id":7
}
y = requests.get(url+uri, params=id) #to pass parameters
print(y.text)

z = requests.get(url+uri, timeout=2)
print(z.text)



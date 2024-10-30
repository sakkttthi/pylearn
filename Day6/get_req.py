# Install request - pip install requests 
# Check insallation - pip list 

import requests

url = 'https://reqres.in/api/users?page=2'

# Get 
x = requests.get(url)
print(x.status_code)

y = requests.get(url, params={"id":7})
print(y.text)

z = requests.get(url, timeout=2)
print(z.text)



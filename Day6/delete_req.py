import requests

delete_url = 'https://reqres.in/api/users/2'

x = requests.delete(delete_url, timeout=1)
print(x.status_code)

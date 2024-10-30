import requests

url = 'https://gorest.co.in/public/v2/users'
token = '6d1d337323aa159d3ccd9aa6903ef955ea2576ad74778c46799dc29778d4d022'

bearer_auth={
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
print(bearer_auth["Authorization"])

req_body = {
"id": 99789,
"name": "Varma khala",
"email": "shah_akshainie_re2@kozey-schroeder.example",
"gender": "female",
"status": "active"
}

x = requests.post(url, headers=bearer_auth, json=req_body)
print(x.status_code)
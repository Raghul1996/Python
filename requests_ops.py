import requests

def requests_operations():
    r=requests.get('https://api.github.com/users/naveenkrnl')
    print(r)
    print(r.content)

requests_operations()
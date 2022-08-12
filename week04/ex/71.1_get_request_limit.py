import requests

fakeURL = 'https://fakestoreapi.com'

queryToCheck = {
    "limit": 3
}

response = requests.get(f"{fakeURL}/products", params = queryToCheck)
print(response.json())
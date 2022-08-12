import requests

fakeURL = 'https://fakestoreapi.com'


response = requests.delete(f"{fakeURL}/products/21")
print(response.json())
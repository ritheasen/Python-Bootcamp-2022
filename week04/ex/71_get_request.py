import requests

fakeURL = 'https://fakestoreapi.com'

response = requests.get(f"{fakeURL}/products") 
# response = requests.get(f"{fakeURL}/carts")
# response = requests.get(f"{fakeURL}/users")#carts #users #
print(response.json())
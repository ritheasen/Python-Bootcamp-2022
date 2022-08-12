import requests

fakeURL = 'https://fakestoreapi.com'

updatedProduct = {
    "category": 'electronic'
}

response = requests.patch(f"{fakeURL}/products/21", json = updatedProduct)
print(response.json())
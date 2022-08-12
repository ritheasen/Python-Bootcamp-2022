import requests

fakeURL = 'https://fakestoreapi.com'

updatedProduct = {
    "title": 'updated_product',
    "category": 'clothing'
}

response = requests.put(f"{fakeURL}/products/21", json = updatedProduct)
print(response.json())
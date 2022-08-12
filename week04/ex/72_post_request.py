import requests

fakeURL = 'https://fakestoreapi.com'

newProduct = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.post(f"{fakeURL}/products", json = newProduct)
print(response.json())
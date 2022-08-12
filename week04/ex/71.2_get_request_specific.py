#get request specific id 

import requests

fakeURL = 'https://fakestoreapi.com'

response = requests.get(f"{fakeURL}/products/18")
print(response)
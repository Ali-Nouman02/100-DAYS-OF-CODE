import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "asdfghjnbvcx"
USERNAME = "ali7564"
GRAPHID = "graph1"

user_params= {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json = user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url= graph_endpoint, json = graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_creation_config = {
    "date": "20241126",
    "quantity": "2",
}

response = requests.post(url = pixel_creation_endpoint, json= pixel_creation_config, headers=headers)
print(response.text)


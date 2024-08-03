import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "token"
GRAPHID = "graph name"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)  # -> once account got created this is no longer needed


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Graph",
    "unit": "h",
    "type": "float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)  # -> once graph got created this is no longer needed


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


# TO UPDATE A CELL
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"
# updated_pixel_data = {
#     "quantity": "1.5",
# }
# response = requests.put(url=pixel_update_endpoint, json=updated_pixel_data, headers=headers)
# print(response.text)


# TO DELETE A CELL
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"
# response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(response.text)

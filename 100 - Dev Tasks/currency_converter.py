import requests
import json

URL = "https://jsonplaceholder.typicode.com/users"


input_id = input("Search by id >>")
response_url = URL + f"?id={input_id}"
print(response_url)

response = requests.get(response_url)
userdata = json.loads(response.text)[0]

name = userdata["name"]
email = userdata["email"]
phone = userdata["phone"]

print(name)
print(email)
print(phone)


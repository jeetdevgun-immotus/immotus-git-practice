import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "New enquiry",
    "body": "Customer asked about a green suit",
    "userId": 1
}

response = requests.post(url, json=new_post, timeout=10)
print("Status code:", response.status_code)
if response.status_code ==201:
    print("Enquiry submitted succesfully")
else:
    print("Something went wrong")
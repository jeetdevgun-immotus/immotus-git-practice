import json

client = {
    "name": "Rahul",
    "business": "Clothing store",
    "monthly_leads": 55
}

client_json = json.dumps(client)

print(client)
print(client_json)

print(type(client))
print(type(client_json))

converted_client = json.loads(client_json)

print(converted_client)
print(type(converted_client))

api_response = '{"customer_name": "Aman", "quantity": 5000}'

enquiry = json.loads(api_response)

print(enquiry)
print(type(enquiry))

print(enquiry["customer_name"])
print(enquiry["quantity"])

with open("client_data.json", "w") as file:
    json.dump(client, file, indent=4)

with open("client_data.json", "r") as file:
    loaded_client = json.load(file)

print(loaded_client)
print(type(loaded_client))

print(loaded_client["name"])
print(loaded_client["monthly_leads"])

with open("enquiry_data.json", "w") as file:
    json.dump(enquiry, file, indent=4)

order = {
    "product": "Cotton suit",
    "quantity": 3,
    "paid": True
}

with open("order_data.json", "w") as file:
    json.dump(order, file, indent=4)

with open("order_data.json", "r") as file:
    loaded_order = json.load(file)

print(loaded_order)
print(type(loaded_order))
print(loaded_order["paid"])
print(type(loaded_order["paid"]))
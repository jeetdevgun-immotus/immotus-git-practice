client = {
    "name": "Rahul",
    "business": "Clothing store",
    "monthly_leads": 25,
    "email": "Rahul@example.com"
}

if client["monthly_leads"] >= 30:
    print(client["name"], "needs a ;ead follow up")
else:
    print(client["name"], "doesnt not have enough leads")
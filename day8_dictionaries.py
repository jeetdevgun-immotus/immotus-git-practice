clients = [
    {
        "name": "DS",
        "business": "tyres",
        "monthly_leads": 22
    },

    {
        "name": "Rahul",
        "business": "clothing",
        "monthly_leads": 45
    },

    {
        "name": "Aman",
        "business": "restaurant",
        "monthly_leads": 55
    }

]

for client in clients:
    print("Client:", client["name"])
    print("Business:", client["business"])
    print("Monthly leads:", client["monthly_leads"])

    if client["monthly_leads"] >= 50:
        client["lead_status"] = "Excellent"
    elif client["monthly_leads"] >= 30:
        client["lead_status"] = "Good"
    else:
        client["lead_status"] = "Needs improvement"

    print("Lead status:", client["lead_status"])

print(clients)
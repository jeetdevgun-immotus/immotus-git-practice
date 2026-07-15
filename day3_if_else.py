monthly_loss = int(input("Monthly loss in business: $"))

if monthly_loss >= 50000:
    print("high priority problem")
elif monthly_loss>=20000:
    print("medium level problem")
else:
    print("Low level problem")
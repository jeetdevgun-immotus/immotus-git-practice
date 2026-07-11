business_name = input("Business name: ")
problem = input("what problem does the client have?")
monthly_loss = int(input("Monthly loss in rupees: "))

yearly_loss = monthly_loss * 12

print("     client Intake Summary     ")
print("Business:", business_name)
print("Problem:", problem)
print("Monthly loss: $", monthly_loss)
print("Yearly loss: $", yearly_loss)
print("if solved, this problem could save the business $", yearly_loss, "per year")
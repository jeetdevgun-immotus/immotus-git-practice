try:
    number = int(input("Enter a number: "))

except ValueError:
    print("That is not a valid number")

else:
    print("You entered:", number)
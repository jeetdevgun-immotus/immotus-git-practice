import immotus_tools as tools

try:
    total = tools.calculate_total(500, 3)
    discounted_price = tools.calculate_discount(1000, 10)

    print(total)
    print(discounted_price)

except ValueError as error:
    print(error)
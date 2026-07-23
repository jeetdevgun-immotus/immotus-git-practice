def calculate_project_cost(hours, hourly_rate):
    project_cost = hours * hourly_rate
    return project_cost


work_hours = int(input("Enter project hours: "))
rate = int(input("Enter hourly rate: "))

base_cost = calculate_project_cost(work_hours, rate)

setup_fee = 1000
final_cost = base_cost + setup_fee

print("Basic project cost:", base_cost)
print("Setup fee:", setup_fee)
print("Final client cost:", final_cost)
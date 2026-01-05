def calculate_net_salary(basic_salary):

    hra = 0.20 * basic_salary
    da = 0.10 * basic_salary
    total_salary = basic_salary + hra + da
    
    tax = 0.05 * total_salary
    net_salary = total_salary - tax
    
    return net_salary

basic_salary = float(input("Enter the basic salary: "))
net_salary = calculate_net_salary(basic_salary)

print(f"The net salary is: {net_salary:.2f}")

import math



def get_pay (num_hours):
    pay_pretax = num_hours * 15
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

pay_fulltime = get_pay(40)
print(pay_fulltime)

def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket) :
    pay_pretax = num_hours * hourly_wage
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

higher_pay_aftertax = get_pay_with_more_inputs(40, 15, .12)
print(higher_pay_aftertax)


# Define the function with no arguments and with no return
def print_hello():
    print("Hello, you!")
    print("Good morning!")


# Call the function
print_hello()

sqft_walls = 432
sqft_ceiling = 144
sqft_per_gallon = 400
cost_per_gallon = 15


def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    new_value = math.ceil((sqft_walls + sqft_ceiling) / sqft_per_gallon)
    cost = new_value * cost_per_gallon
    return cost

actual_cost = get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
print(f"актуальная цена:{actual_cost} $")




from pyexpat.errors import messages

print(2 > 3)

print("_________________")

var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

print("_________________")
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))

print("_________________")

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(39))

print("_________________")

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

print(evaluate_temp_with_elif(33))

print("_________________")

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(9000*.25)
print(bob_taxes)
print(15000*.3)

print("_________________")

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

print(get_dose(5))

print("_________________")

def get_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

print(get_grade(51))
print(get_grade(61))
print(get_grade(71))
print(get_grade(81))
print(get_grade(91))

print("_________________")

def get_water_bill(num_gallons):
    if num_gallons >= 30001:
        bill = num_gallons / 1000 * 10
    elif num_gallons >= 22001:
        bill = num_gallons / 1000 * 7
    elif num_gallons >= 8001:
        bill = num_gallons / 1000 * 6
    elif num_gallons >= 0:
        bill = num_gallons / 1000 * 5
    return bill
print(get_water_bill(22300))

print("_________________")

def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    elif gb > 15:
        bill = 100 + (gb - 15) * 100
    return bill

print(get_phone_bill(15.5))

print("_________________")



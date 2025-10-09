#syntax 14 Lesson
def functional_name(parametrs):
    """Docstring for functional_name."""
    return parametrs #(expression

#why dunctions
num = 24
if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

def even_or_odd (num):
    """This function finds even or odd"""
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

# Call this function

even_or_odd(24)

#function with multiple parametrs

def add (a,b):
    """This function adds two numbers together"""
    return a+b
result = add(5,2)

print(result)

#Default parametrs

def greet(name):
    print(f"Hello {name} Welcome!")

greet("Kris")

def greet_2(name_2 = "Guest"): #Enter default parametrs
    print(f"Hello {name_2} Welcome!")
greet_2()

# Variable Length Arguments
#Positional and keyword arguments

def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1,2,3,4,5, "Kris")

# Keywords arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_details(a=1,b=2,c=3,d=4,town=3.4,name="Kris")

def print_details_2(*args, **kwargs):
    for num in args:
        print(f"Positional argument: {num}")
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_details_2(1, 3, 4, name = "John")

#return staitment
def multiply (a,b):
    return a*b, b, a

print(multiply(1,5))
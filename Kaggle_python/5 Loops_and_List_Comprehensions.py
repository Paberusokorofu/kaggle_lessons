#https://www.kaggle.com/code/colinmorris/loops-and-list-comprehensions

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line


multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')


for i in range(5):
    print("Doing important work. i =", i)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1

squares = [n**2 for n in range(10)]
squares

print(squares)

squares = []
for n in range(10):
    squares.append(n**2)
squares

print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

[
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]


def count_negatives(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

def count_negatives(nums):
    return len([num for num in nums if num < 0])
print(count_negatives)

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

help("append")

meals = ['fish', 'fish', 'bread', 'jam', 'chicken']#нет условия что они стоят рядом, хотя надо учитывать именно это

def menu_is_boring(meals):
    # Iterate over all indices of the list, except the last one
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
print(menu_is_boring(meals))

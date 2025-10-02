# Stop here https://www.kaggle.com/code/colinmorris/lists

primes = [2, 3, 5, 7]

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

print(primes[2])
print(planets[0:6])
print(planets[1:])
print(planets[:3])
print(planets[1:-1])

planets[3] = 'Malacandra'
print(planets[0:6])

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

print(len(planets))

print(sorted(planets))

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

print(x.bit_length())

planets.append('Earth')
planets.append('Pluto')
print(planets)

help(planets.append)
# planets.pop()
print(planets)
planets.index('Earth')

print("Earth" in planets)

#!!! help(planets)

#Tuples

t = (1, 2, 3)
print(t)
#They cannot be modified (they are immutable).

x = 0.125
x.as_integer_ratio()
print(x)

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)
select_second = [1,2,3,4,5]

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    return L[1] if len(L) > 1 else None
    pass







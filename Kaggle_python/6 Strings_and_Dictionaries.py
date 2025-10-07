# https://www.kaggle.com/code/colinmorris/strings-and-dictionaries

# x = 'Pluto\'s a planet!'
# print(x)
# What you type...	What you get	example	print(example)
# \'	'	'What\'s up?'	What's up?
# \"	"	"That's \"cool\""	That's "cool"
# \\	\	"Look, a mountain: /\\"	Look, a mountain: /\
# \n
# "1\n2 3"	1
# 2 3

# numbers = {'one':1, 'two':2, 'three':3}
# print(numbers['three'])
# numbers['one'] = 'Pluto'
# print(numbers['one'])
#
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# planet_to_initial = {planet: planet[0] for planet in planets}
# print(planet_to_initial)

planet = 'Pluto'
print(len(planet))

claim = "Pluto is a planet!"
claim.upper()

print(claim.upper())
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('planet'))

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(datestr.split())
'/'.join([month, day, year])
print(datestr)

print(planet + ', we miss you.')

position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
print(pluto_mass, earth_mass, population)
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
print('_________________')

numbers = {'one':1, 'two':2, 'three':3}
print(numbers['two'])

numbers['eleven'] = 11
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)

print('________________')

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial)

maps = ['jin', 'gooa', 'urto']
map_to_initial = {mipo: mipo[1] for mipo in maps}
print(map_to_initial)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

' '.join(sorted(planet_to_initial.values()))
print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

help(str.isdigit)




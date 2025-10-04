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

numbers = {'one':1, 'two':2, 'three':3}
print(numbers['three'])
numbers['one'] = 'Pluto'
print(numbers['one'])

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

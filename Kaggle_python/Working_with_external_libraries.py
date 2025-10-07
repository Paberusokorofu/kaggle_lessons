import math
import numpy

print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
from numpy import asarray #Можно импортировать только те функции которые необходимы для работы

print("It's math! It has type {}".format(type(mt)))

print(dir(math))

print("pi to 4 significant digits = {:.8}".format(math.pi))

print(math.log(32, 2))

print(math.acos(1))

print(math.pi)
print(math.log(32, 2))

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)
print(rolls + 10)
print(rolls <= 3)


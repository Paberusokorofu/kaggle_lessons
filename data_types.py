from tarfile import TruncatedHeaderError

x = 14.288
print(x)
print(type(x))

almost_pi = 22 / 7
print(almost_pi)
print(type(almost_pi))

z_one = True
print(z_one)
print(type(z_one))

z_tree = (1 < 2)
print(z_tree)
print(type(z_tree))

z_four = (5 < 2)
print(z_four)
print(type(z_four))

z_four = not z_four
print(z_four)
print(type(z_four))

w = "Hello, Python!"
print(w)
print(type(w))
print(len(w))

my_number = "1.34562"
print(my_number)
print(type(my_number))

also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

new_string = "avd" * 3
print(new_string)
print(type(new_string))

# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

print(-3.1 * True)
print(-3.1 * False)

print("_____________________________")

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

print("__________")

engraving = "08/10/2000"

solid_gold = True

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = len(engraving) * 10 + 100
    else:
        cost = len(engraving) * 7 + 50
    return cost

print(cost_of_project(engraving, solid_gold))

# variables in python
# Variables are containers for storing data values

x = 200
y = 5

print(x+y)

# Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.
b = 5  #b is int type
b = "string type"    # changed b value to string

print(b)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
r = str(3)    # r will be '3'
t = int(3)    # t will be 3
d = float(3)  # d will be 3.0

print(r)

# You can get the data type of a variable with the type() function.
print(type(r))
print(type(t))
print(type(d))


# Variable names are case-sensitive.
c = 'computer'
C = 'laptop'

print(c)
print(C)
#single line of string type, signle quote or double qoute
from typing import Concatenate

name = "Guled mohamed"
print(name)

#multiple lines of string type
name = """Guled waxa uu jooga imaka 
shaqodoon organization"""
print(name)

#string len function and index value
bits = 'HargaBits Academy'
print(bits)
print(bits[10:17])

#string function, lower, upper, count, and find
location = "Hargeisa Hello"
print(location.lower())
print(location.upper())
print(location.count('H'))
print(location.find('Hargeisa'))

# string Concatenate and formats 

org = "Hello"
org_name = "Shaqodoon org"

# string Concatenate 1
msg = org + ', ' + org_name +' welcome'

# string Concatenate 2
msg2 = '{}, {}. welcome!'.format(org, org_name)

print(msg)
print(msg2)

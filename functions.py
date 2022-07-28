
def delete_function():

    print("successfully deleted the record!")

# To call a function, use the function name followed by parenthesis:
delete_function()

# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.

def students(name): # one argument name

    print("Your name is:" +name)

students("Guled Mohamed")

# example 2 with two argument
def students(fname, age): # one argument name

    print("Your name: "+fname+ "\n"+"Your age: " +age)

students("Guled Mohamed", "31")


# example 3 with two argument
def students(fname, age): # one argument name

    print("Your name: "+fname+ "\n"+"Your age: " +age)

students(fname="Guled Mohamed", age="31")


# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
  
print(my_function(3))


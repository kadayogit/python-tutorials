
message = "Awesome"  #varibale declare outside of the function called global varibale

# Create a variable outside of a function, and use it inside the function
def mytest():
    x = "inside the function"
    print("Python is " + message)
    # call the function
    # print(x)
mytest()
print("Python is " + message)
"""
Decorator: Design Pattern
 - Writing function for common functionalities which is needed in all other
 functions
 -After writing function with functionalities, we can use this function in all
 other functions which need this functionality
"""

print("WITHOUT using decorator design pattern")
print("-"*20)
# ------------


def add(a, b):
    print('Result is:')
    print(a + b)
    print('End of the result', end="\n\n")


def sub(a, b):
    print('Result is:')
    print(a - b)
    print('End of the result', end="\n\n")


add(10, 20)
sub(10, 20)

print("#"*40, end="\n\n")
#################################

print("Using decorator design pattern: PARTIALLY IMPLEMENTED")
print("-"*20)
# ------------


def my_decorator(my_func): # my_func = sub
    def decorated_function(x, y):
        print("Result is:")
        my_func(x, y) # sub(10, 20)
        print("End of the result", end="\n\n")
    return decorated_function


def add(a, b):
    print(a + b)


received_function = my_decorator(add)
# received_function = decorated_function
received_function(10, 20)


def sub(a, b):
    print(a - b)

received_function = my_decorator(sub)
# received_function = decorated_function
received_function(10, 20)

print("#"*40, end="\n\n")
#################################

print("Using decorator design pattern: FINAL")
print("-"*20)
# ------------


def my_decorator(my_func): # my_func = sub
    def decorated_function(x, y):
        print("Result is:")
        my_func(x, y) # sub(10, 20)
        print("End of the result", end="\n\n")
    return decorated_function


@my_decorator
def add(a, b):
    print(a + b)


add(10, 20)

# @my_decorator will take care of executing below 2 lines
# received_function = my_decorator(add)
# received_function(10, 20)


@my_decorator
def sub(a, b):
    print(a - b)

sub(10, 20)

# @my_decorator will take care of executing below 2 lines
# received_function = my_decorator(sub)
# received_function(10, 20)

print("#"*40, end="\n\n")
#################################
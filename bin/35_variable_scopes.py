"""
Variable Scopes
1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Builtin Scope
"""

print("1. Local Scope")
print("-"*20)
# ------------


def my_function():
    a = 10 # Local Scope, Outside the function we can't access
    print("Value of a is:", a)


my_function()

print("#"*40, end="\n\n")
#################################

print("2. Enclosed Scope")
print("-"*20)
# ------------


def my_function_1():
    a = 100 # Enclosed scope, where current and nested functions can access
    def my_function_2():
        print("Accessing outer function a having value =:", a)
    my_function_2()


my_function_1()

print("#"*40, end="\n\n")
#################################

print("3. Global Scope")
print("-"*20)
# ------------


x = 1000 # Global scope, we can access anywhere
def my_function_1():
    print("In my_function_1:", x)
    def my_function_2():
        print("In my_function_2:", x)
    my_function_2()


my_function_1()
print("Outside of all function:", x)

print("#"*40, end="\n\n")
#################################

# How it will search for variable
#
# 1st search in local scope
# If not present
#
# then
#
# search in enclosed
# If not present
#
# then
#
# search in global
# If not present
#
# then
#
# search in builtins
# If not present
#
# then
#
# Error
"""
Function with VARIABLE POSITIONAL arguments
and
Function with VARIABLE KEYWORD arguments
"""

print("Function with VARIABLE POSITIONAL arguments")
print("-"*20)
# ------------
# *a is variable positional argument
def add(*a):
    print("Value of a is:", a)
    return sum(a)

add_result_1 = add()
print("add_result_1:", add_result_1, end="\n\n")

add_result_2 = add(10, 20, 30, 40, 50)
print("add_result_2:", add_result_2, end="\n\n")

print("#"*40, end="\n\n")
#################################

print("Function with VARIABLE KEYWORD arguments")
print("-"*20)
# ------------


def profile_function(**a):
    print("Value of a is:", a)


profile_function()
profile_function(name="emp-1")
profile_function(name="emp-2", company="XYZ Company")
profile_function(name="emp-3", company="ABC Company", email="email-1")


print("#"*40, end="\n\n")
#################################
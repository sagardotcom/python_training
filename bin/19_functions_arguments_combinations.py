"""
We can combine both positional & keyword argument in single function.

We need follow below ORDER of the argument in function definition

1st put all positional arguments IF ANY

then

put variable positional argument IF ANY

then

put all keyword arguments IF ANY

then

put variable keyword argument IF ANY
"""

print("Function POSITIONAL & KEYWORD Argument")
print("-"*20)
# ------------


# a,b are positional
# c & d are strictly keyword
def add(a, b, *, c, d):
    return a + b + c + d


add_result = add(10, 20, c=30, d=40)
print("add_result:", add_result)

print("#"*40, end="\n\n")
#################################


print("Function POSITIONAL & VARIABLE POSITIONAL & KEYWORD Argument")
print("-"*20)
# ------------


# a,b are positional
# c & d are strictly keyword
def add(a, b, *c, d, e):
    return a + b + sum(c) + d + e


add_result = add(10, 20, d=40, e=50)
print("add_result:", add_result)

add_result = add(10, 20,30, 40, 50, d=30, e=40)
print("add_result:", add_result)

print("#"*40, end="\n\n")
#################################


print("All type of argument in one functions")
print("-"*20)
# ------------


# a,b are positional
# c & d are strictly keyword
def add(a, b, *c, d, e, **f):
    return a + b + sum(c) + d + e + sum(f.values())


add_result = add(10, 20, d=30, e=40)
print("add_result:", add_result)

add_result = add(10, 20,30, 40, 50, d=60, e=70, x=80, y=90, z=100)
# f = {x:80, y:90, z:100}
print("add_result:", add_result)

print("#"*40, end="\n\n")
#################################
"""
Functions: If we want to rewrite/copy-paste same code more than one time
then instead of rewrite/copy-paste, we can keep that code in one block
and we can reuse that code
"""

print("WITHOUT using function")
print("-"*20)
# ------------

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

a = 10
b = 20
c = a + b
print("Value of c is:", c)

print("#"*40, end="\n\n")
#################################

print("Using function")
print("-"*20)
# ------------

# Function Definition
def my_func():
    a = 10
    b = 20
    c = a + b
    print("Value of c is:", c)

# Function call
my_func()
my_func()
my_func()
my_func()

print("#"*40, end="\n\n")
#################################
"""
How to get or create objects
- Answer: Using class

In this section:
1. CLASS OBJECT
2. INSTANCE OBJECTS
"""

print("Create objects")
print("-"*20)
# ------------


class Employee:
    pass
# 'pass' use this to keep any block empty
# Even though it is empty, it is valid class. Which means we can create objects


e1 = Employee()
e2 = Employee()

# Total objects: 3
# 1. CLASS OBJECT: 'Employee' which is created automatically
# 2. INSTANCE OBJECTS: 'e1' & 'e2' which we created

print("#"*40, end="\n\n")
#################################

print("DATA present inside object:")
print("-"*20)
# ------------

print("DATA present inside CLASS object 'Employee':", Employee)
print("DATA present inside INSTANCE object 'e1':", e1)
print("DATA present inside INSTANCE object 'e2':", e2)

print("#"*40, end="\n\n")
#################################

print("METHODS/VARIABLES present inside object:")
print("-"*20)
# ------------

print("METHODS/VARIABLES present inside CLASS object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside INSTANCE object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside INSTANCE object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#################################

# About 'object' class
# - it is builtin class
# - it has many methods
# - by default it is linked to all the classes
#   which we are writing: called INHERITANCE
# - by default, whatever there in 'object' class
#   will be available in our class as well
"""
How to put data inside object

In this section:
1. CLASS variables
2. INSTANCE Variables
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

print("Store data")
print("-"*20)
# ------------

Employee.company_name = "XYZ Company"
e1.name = "emp-1"
e2.name = "emp-2"

print("#"*40, end="\n\n")
#################################

print("DATA present inside object:")
print("-"*20)
# ------------

print("DATA present inside CLASS object 'Employee':", Employee.company_name)
print("DATA present inside INSTANCE object 'e1':", e1.name)
print("DATA present inside INSTANCE object 'e2':", e2.name)

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

# About class object 'Employee'
# - class object 'Employee' is common SPACE for all instance objects
# - data which is common for all instance objects can be stored in class object 'Employee'
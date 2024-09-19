"""
In this program, we are accessing
variables,
functions
classes
present in mymodule.py library
"""

print("1-way to import")
print("-"*20)
# ------------

import mymodule

print("Course name:", mymodule.course)

add_result = mymodule.add(10, 20)
print("add_result:", add_result)

e1 = mymodule.Employee()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
#################################

print("2-way to import")
print("-"*20)
# ------------

import mymodule as mm

print("Course name:", mm.course)

add_result = mm.add(10, 20)
print("add_result:", add_result)

e1 = mm.Employee()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
#################################

print("3-way to import")
print("-"*20)
# ------------

from mymodule import course, add, Employee

print("Course name:", course)

add_result = add(10, 20)
print("add_result:", add_result)

e1 = Employee()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
#################################

print("4-way to import")
print("-"*20)
# ------------

from mymodule import course as c, add as a, Employee as E

print("Course name:", c)

add_result = a(10, 20)
print("add_result:", add_result)

e1 = E()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
#################################
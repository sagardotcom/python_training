"""
When we create object, 2 methods will execute which coming from 'object' class.
one after the other both the methods will execute

1) __new__ : This has logic to construct the object : CONSTRUCTOR
2) __init__: Initializer : Nothing present in this method

We can always rewrite/OVERRIDE methods which is coming from object class
including __new__ and __init__


In this example, we are making use of __init__ for passing values at
the time of object creation
"""

print("Create objects")
print("-"*20)
# ------------


class Employee:

    def __init__(self, en):
        self.name = en

    def get_employee_name(self):
        return self.name

    company_name = "XYZ Company"
    # this will get stored in class object

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    @staticmethod # Instance/Class object will not be passed
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2) / 2


e1 = Employee("emp-1") # __init__
e2 = Employee("emp-1") # __init__

# Total objects: 3
# 1. CLASS OBJECT: 'Employee' which is created automatically
# 2. INSTANCE OBJECTS: 'e1' & 'e2' which we created

print("#"*40, end="\n\n")
#################################

print("DATA present inside object:")
print("-"*20)
# ------------

print("DATA present inside CLASS object 'Employee':", Employee.get_company_name())
print("DATA present inside INSTANCE object 'e1':", e1.get_employee_name())
print("DATA present inside INSTANCE object 'e2':", e2.get_employee_name())

salary1 = 10000
salary2 = 20000
avg_salary = Employee.compute_avg_salary(salary1, salary2)
print("avg_salary:", avg_salary)

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
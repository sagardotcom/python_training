"""
How to add methods

In this section,
1. CLASS METHODS
2. INSTANCE METHODS
3. STATIC METHODS
"""

print("Create objects")
print("-"*20)
# ------------


class Employee:

    def store_employee_name(self, en):
        self.name = en

    def get_employee_name(self):
        return self.name

    @classmethod # Decorator -> it will take care of passing class object to cls even if we are calling with e1 & e2
    def store_company_name(cls, cn):
        cls.company_name = cn

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    @staticmethod # Instance/Class object will not be passed
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2) / 2


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

Employee.store_company_name("XYZ Company")
# Internally object 'Employee' will be passed to 'cls'

e1.store_employee_name("emp-1")
# Internally object 'e1' will be passed to 'self'

e2.store_employee_name("emp-2")
# Internally object 'e2' will be passed to 'self'

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
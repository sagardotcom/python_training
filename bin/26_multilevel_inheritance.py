"""
Inheritance:
1) multi-level inheritance
2) multiple inheritance

In this section,
1) multi-level inheritance
"""

print("multi-level inheritance")
print("-"*20)
# ------------


# Assume below class is EXISTING class
class Salary:
    def add_salary(self, sal):
        self.salary = sal

    def get_salary(self):
        return self.salary

# Client requirement:
# 1) add/view tax methods
# 2) modify get_salary method to return (salary-tax)


# Salary: superclass/parent class
# Employee: subclass/child class
class Employee(Salary):

    # 1) add/view tax methods
    def add_tax(self, tax):
        self.tax = tax

    def get_tax(self):
        return self.tax

    # 2) modify get_salary method to return (salary-tax)
    # POLYMORPHISM: WE can use same name super class
    def get_salary(self):
        # CAll super class method

        # 1-way to access super class method
        # sal = super().get_salary()

        # 2-way to access super class method
        # sal = Salary.get_salary(self)

        return self.salary - self.tax


e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())

print("#"*40, end="\n\n")
#################################
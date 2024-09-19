"""
Operator Overloading:

In python, for each operator like +, - etc
there is special name given like __add__, __sub__ etc

If we want to support + for example then we need to write method
__add__ in our class
"""

print('Supporting + operator')
print("-"*20)
# ------------


class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self = e1, other = e2
        concat_result = self.name + other.name
        return concat_result


e1 = Employee("emp-1")
e2 = Employee("emp-2")
# Requirement: If we use + then it should concatinate both employee names
# and return
add_result = e1 + e2 # it calls e1.__add__(e2)
print("add_result:", add_result)


print("#"*40, end="\n\n")
#################################

class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self = e1, other = e2
        concat_result = self.name + other.name
        return concat_result

    def __len__(self): # self=e1
        return len(self.name)


e1 = Employee("emp-1")
e2 = Employee("emp-2")
# Requirement: If we use + then it should concatinate both employee names
# and return
add_result = e1 + e2 # it calls e1.__add__(e2)
print("add_result:", add_result, end="\n\n")

print("Length of e1:", len(e1)) # e1.__len__()


print("#"*40, end="\n\n")
#################################

print("Supported Iteration")
print("-"*20)
# ------------


class Employee:
    def __init__(self, en):
        self.name = en
    def __add__(self, other): # self = e1, other = e2
        concat_result = self.name + other.name
        return concat_result

    def __len__(self): # self=e1
        return len(self.name)

    def __iter__(self): # 1st time & one time it will call
        self.index_no = 0
        return self

    def __next__(self): # Every iteration this will be called
        current_index = self.index_no
        if current_index < len(self.name):
            self.index_no += 1
            return self.name[current_index]
        else:
            raise StopIteration


e1 = Employee("emp-1")
e2 = Employee("emp-2")
# Requirement: If we use + then it should concatinate both employee names
# and return
add_result = e1 + e2 # it calls e1.__add__(e2)
print("add_result:", add_result, end="\n\n")

print("Length of e1:", len(e1), end="\n\n") # e1.__len__()

print("iterating using for-loop:")
for i in e1:
    print("Value of i is:", i)
# e
# m
# p
# -
# 1
print("#"*40, end="\n\n")
#################################
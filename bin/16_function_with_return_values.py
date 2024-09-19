"""
2 Cases
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

In this section,
Case-1: How to access values outside the function
"""

print("Function with 1 return value")
print("-"*20)
# ------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return name


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#################################

print("Function with more than 1 return value: In Tuple")
print("-"*20)
# ------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return name, company # Default it will keep it in tuple and return


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#################################

print("Function with more than 1 return value: In LIST")
print("-"*20)
# ------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return [name, company]


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#################################

print("Function with more than 1 return value: In DICTIONARY")
print("-"*20)
# ------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
#################################
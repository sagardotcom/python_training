"""
In this section,
Case-2: How to pass values to variables present inside the function

3 ways to pass values to variables present inside the function

1-way: We can pass only value OR arg=value format
    EITHER POSITIONAL OR KEYWORD ARGUMENT

2-way: We can pass only values
    STRICTLY POSITIONAL ARGUMENT

3-way: We can pass values using arg=value format
    STRICTLY KEYWORD ARGUMENT

"""

print("""
1-way: We can pass only value OR arg=value format
    EITHER POSITIONAL OR KEYWORD ARGUMENT
""")
print("-"*20)
# ------------


def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee("emp-1", "comp-1") # POSITIONAL ARG
print("received_value:", received_value, end="\n\n")

# OR

received_value = employee(name="emp-1", company="comp-1") # KEYWORD ARG
print("received_value:", received_value, end="\n\n")

# OR

received_value = employee(company="comp-1", name="emp-1")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#################################

print("""
2-way: We can pass only values
    STRICTLY POSITIONAL ARGUMENT
""")
print("-"*20)
# ------------


# / is just syntax to tell this function is POSITIONAL ARGUMENT FUNCTIOn
#   where ONLY values we need to pass
# / is not counted as argument
# we are not passing values to /
def employee(name, company, /): # STRICLTY POSITIONAL ARGUMENT means we can pass only VALUES
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee("emp-1", "comp-1") # POSITIONAL ARG
print("received_value:", received_value, end="\n\n")

# OR

# THIS IS NOT ALLOWED to pass arg=value format
#
# received_value = employee(name="emp-1", company="comp-1") # KEYWORD ARG
# print("received_value:", received_value, end="\n\n")


print("#"*40, end="\n\n")
#################################

print("""
3-way: We can pass values using arg=value format
    STRICTLY KEYWORD ARGUMENT
""")
print("-"*20)
# ------------

# * is syntax to tell it is KEYWORD argument function where we need to pass values
#   using arg=value
# * is not counted as argument
# We are not passing any values to *
#
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}



# THIS IS NOT ALLOWED. Means we can't pass values
# received_value = employee("emp-1", "comp-1") # POSITIONAL ARG
# print("received_value:", received_value, end="\n\n")

# OR

received_value = employee(name="emp-1", company="comp-1") # KEYWORD ARG
print("received_value:", received_value, end="\n\n")

# OR

received_value = employee(company="comp-1", name="emp-1")
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#################################
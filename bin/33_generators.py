"""
Generator: We can generate or create objects whenever we want
"""

print("WITHOUT using generator")
print("-"*20)
# ------------


def my_square_function(my_list):
    squared_list = []
    for i in my_list:
        squared_list.append(i*i)
    return squared_list


L = [1, 2, 3, 4, 5]
squared_L = my_square_function(L)

for i in squared_L:
    print("Square of i:", i)

# Requirement here is, print each squared value of L

# Currently, function is squaring all the values, keeping in list
#   and returns that list

# In this case, not required to store all the squared values in list
# instead when for-loop ask values every iteration
# that time if we are able to create and provide value also FINE
# it avoids storing squared_list and also saves memory.

print("#"*40, end="\n\n")
#################################

print("USING generator")
print("-"*20)
# ------------


def generator_my_square_function(my_list):
    for i in my_list:
        yield i * i


L = [1, 2, 3, 4, 5]
generator_object = generator_my_square_function(L)

for i in generator_object:
    print("Square of i:", i)


print("#"*40, end="\n\n")
#################################
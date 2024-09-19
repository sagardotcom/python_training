"""
 Tuple:
        -- We have option to store collection of values like list of names, list of email-ids etc
        -- Here, we can store DUPLICATE values
        -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("How to store values")
print("-"*20)
# ------------

my_tuple_1 = (10, 12.5, "python", (100, 200))
# Internally it will create object of builtin class and store the values

# OR we can also use class name
my_tuple_2 = tuple((10, 12.5, "python", (100, 200)))

print(my_tuple_1, my_tuple_2, sep="\n")

print("#"*40, end="\n\n")
#################################


print("Tuple PART-2")
print("Indexes: Which is similar to strings")
print("-"*20)
# ------------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # "python"
print("2nd character in Course Name:", my_tuple[2][1], end="\n\n") # "python"

print("Inner tuple:", my_tuple[-1]) # (100, 200)
print("Last value of Inner tuple:", my_tuple[-1][-1]) # (100, 200)

print("#"*40, end="\n\n")
#################################

print("Tuple PART-3")
print("Methods inside 'tuple' class")
print("-"*20)
# ------------

print(dir(tuple))

print("#"*40, end="\n\n")
#################################
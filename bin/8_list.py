"""
 list:
        -- We have option to store collection of values like list of names, list of email-ids etc
        -- Here, we can store DUPLICATE values
        -- Automatically index number will be assigned to each value
"""

print("list PART-1")
print("How to store values")
print("-"*20)
# ------------

my_list_1 = [10, 12.5, "python", (100, 200)]
# Internally it will create object of builtin class and store the values

# OR we can also use class name
my_list_2 = list((10, 12.5, "python", (100, 200)))

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end="\n\n")
#################################

print("list PART-2")
print("Indexes: Which is similar to strings")
print("-"*20)
# ------------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # "python"
print("2nd character in Course Name:", my_list[2][1], end="\n\n") # "python"

print("Inner list:", my_list[-1]) # (100, 200)
print("Last value of Inner list:", my_list[-1][-1]) # (100, 200)

print("#"*40, end="\n\n")
#################################

print("list PART-3")
print("Methods inside 'list' class")
print("-"*20)
# ------------

print(dir(list))

print("#"*40, end="\n\n")
#################################
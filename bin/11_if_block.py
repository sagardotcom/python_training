"""
Conditional Statement 'if': Based on the condition we can execute block of code
"""

print("Only if block")
print("-"*20)
# ------------

x = 10
if x == 10:
    print("Value of x is equal to 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

if x > 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

if x < 10:
    print("Value of x is less than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

print("#"*40, end="\n\n")
#################################

print("'if-elif' block")
print("-"*20)
# ------------

x = 10
if x == 10:
    print("Value of x is equal to 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")
elif x > 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")
elif x < 10:
    print("Value of x is less than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

print("#"*40, end="\n\n")
#################################

print("'if-elif-else' block")
print("-"*20)
# ------------

x = 10
if x == 10:
    print("Value of x is equal to 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")
elif x > 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")
else:
    print("Value of x is less than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

print("#"*40, end="\n\n")
#################################

print("'if' with strings")
print("-"*20)
# ------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

if ("tho" in my_string) and ("XYZ" not in my_string):
    print("Substring found")

if my_string.startswith("Py"):
    print("my_string startswith Py")

print("#"*40, end="\n\n")
#################################


print("'if' with list/tuple/Any other collection")
print("-"*20)
# ------------

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

if "Java-1" in my_list:
    print("Course 'Java-1' found")

print("#"*40, end="\n\n")
#################################

print("'if' with dictionary")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.keys()
# ['course', 'duration', 'mode']
if 'course' in my_dictionary.keys():
    print("Key 'Course' Found")

# my_dictionary.values()
# ['python', 10, 'online']
if 'online' in my_dictionary.values():
    print("Value 'online' found")


# my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
if ('course', 'python') in my_dictionary.items():
    print("Item found")

# Example:
L = list(my_dictionary.items()) # [('course', 'python'), ('duration', 10), ('mode', 'online')]
print(L)
print(L[0]) # ('course', 'python')
print(L[0][1]) # 'python'
print(L[0][1][2]) # 't'

print("#"*40, end="\n\n")
#################################


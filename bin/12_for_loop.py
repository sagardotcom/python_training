"""
for-loop: Iterate any collection
"""

print("Iterate string:")
print("-"*20)
# ------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Value of i:", i)

print("#"*40, end="\n\n")
#################################


print("Iterate list/tuple/any other collection:")
print("-"*20)
# ------------

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

for i in my_list:
    print("Value of i:", i)

print("#"*40, end="\n\n")
#################################

print("'for-loop' with dictionary.keys()")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for each_key in my_dictionary.keys():
    print("Each Key:", each_key)
    print("Each Value:", my_dictionary[each_key])

print("#"*40, end="\n\n")
#################################

print("'for-loop' with dictionary.values()")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.values()
# ['python', 10, 'online']

for each_value in my_dictionary.values():
    print("Each Value:", each_value)

print("#"*40, end="\n\n")
#################################


print("'for-loop' with dictionary.items(): 1-way")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]

for each_item in my_dictionary.items():
    print("Each Item:", each_item)
    print("Key:", each_item[0])
    print("Value:", each_item[1])

print("#"*40, end="\n\n")
#################################

print("'for-loop' with dictionary.items(): 2-way")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]

for each_key, each_value in my_dictionary.items():
    print("Key:", each_key)
    print("Value:", each_value)


print("#"*40, end="\n\n")
#################################

# 2 Cases
# Case-1: 'break': How to end for-loop in between
# Case-2: 'continue': How to skip current iteration

print("# Case-1: 'break': How to end for-loop in between")
print("-"*20)
# ------------

# Requirement: Verify are there any course starting with Java

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

for each_course in my_list:
    if each_course.startswith("Java"):
        print("Course Java Found")
        break


print("#"*40, end="\n\n")
#################################

print("# Case-2: 'continue': How to skip current iteration")
print("-"*20)
# ------------

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

for each_course in my_list:
    if not each_course.startswith("Java"):
        continue
    # Below code is applicable only for JAVA courses
    # Other than Java courses not required from this line onwards
    # till end of for-block
    print("This Java course name is :", each_course)
    print("This is one version of Java")
    print("This java course duration is 10 days")


print("#"*40, end="\n\n")
#################################

print("'for-else' block")
print("-"*20)
# ------------

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

for each_course in my_list:
    print("Each Course:", each_course)
else:
    print("After completing for-loop, 'else' will execute")

# If normal end of 'for-loop' then 'else' will execute
# If 'for-loop' ended using 'break' then 'else' will NOT execute

print("#"*40, end="\n\n")
#################################

print("WITHOUT 'for-else' example-1")
print("-"*20)
# ------------

# Requirement: Verify are there any course starting with Java

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

# Requirement: print course FOUND or NOT-FOUND
my_flag = 0
for each_course in my_list:
    if each_course.startswith("Java"):
        print("Course Java Found")
        my_flag = 1
        break

if my_flag == 0:
    print("Java Course Not Found")


print("#"*40, end="\n\n")
#################################

print("'for-else' example-2")
print("-"*20)
# ------------

# Requirement: Verify are there any course starting with Java

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

# Requirement: print course FOUND or NOT-FOUND

for each_course in my_list:
    if each_course.startswith("Java"):
        print("Course Java Found")
        break
else:
    print("Java Course Not Found")
    del my_list


print("#"*40, end="\n\n")
#################################
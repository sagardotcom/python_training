"""
while loop: We can execute the loop based on the condition
"""
print("While loop example")
print("-"*20)
# ------------

x = 0
while x < 5:
    print("Value of x is:", x)
    x = x + 1

print("#"*40, end="\n\n")
#################################

# 2 Cases
# Case-1: 'break': How to end for-loop in between
# Case-2: 'continue': How to skip current iteration

print("# Case-1: 'break': How to end while-loop in between")
print("-"*20)
# ------------

# Requirement: Verify are there any course starting with Java

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course Java Found")
        break
    index_no = index_no + 1


# for each_course in my_list:
#     if each_course.startswith("Java"):
#         print("Course Java Found")
#         break


print("#"*40, end="\n\n")
#################################

print("# Case-2: 'continue': How to skip current iteration")
print("-"*20)
# ------------

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    if not my_list[index_no].startswith("Java"):
        index_no = index_no + 1
        continue
    # Below code is applicable only for JAVA courses
    # Other than Java courses not required from this line onwards
    # till end of for-block
    print("This Java course name is :", my_list[index_no])
    print("This is one version of Java")
    print("This java course duration is 10 days")
    index_no = index_no + 1


# for each_course in my_list:
#     if not each_course.startswith("Java"):
#         continue
#     # Below code is applicable only for JAVA courses
#     # Other than Java courses not required from this line onwards
#     # till end of for-block
#     print("This Java course name is :", each_course)
#     print("This is one version of Java")
#     print("This java course duration is 10 days")


print("#"*40, end="\n\n")
#################################

print("'while-else' example")
print("-"*20)
# ------------

# Requirement: Verify are there any course starting with Java

my_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_list:", my_list, end="\n\n")

# Requirement: print course FOUND or NOT-FOUND

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course Java Found")
        break
    index_no = index_no + 1
else:
    print("Java Course Not Found")
    del my_list

# for each_course in my_list:
#     if each_course.startswith("Java"):
#         print("Course Java Found")
#         break
# else:
#     print("Java Course Not Found")
#     del my_list


print("#"*40, end="\n\n")
#################################
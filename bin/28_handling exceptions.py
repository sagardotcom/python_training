"""
Exceptions Handling:
"""

# print("WITHOUT Exceptions Handling")
# print("-"*20)
# # ------------
#
# a = 10
# b = 0
# result = a/b # Program will terminate here abruptly
# print("result:", result)
#
# print("#"*40, end="\n\n")
# #################################

print("Exceptions Handling")
print("-"*20)
# ------------

try:
    a = 10
    b = 0
    result = a/b # Program will NOT terminate here. Instead control will be passed to except block
    print("result:", result)
except:
    print("Reached Except")
print("#"*40, end="\n\n")
#################################

print("Exceptions Handling: Using Classes")
print("-"*20)
# ------------

# About 'Exception' classes
# ------------
# - We need to have classes for each error
# - Few are present in builtins
# - If we are using libraries, libraries will also give use exception classes
# - We can also write our own classes
# If we don't have exception class then we can't handle, so it will terminate
# ------------

try:
    a = 10
    b = 0
    result = a/b
    print("result:", result)
except ZeroDivisionError:
    print("Reached Except, This is ZDE")
except NameError as ne:
    print("Reached Except, This is NE and ne is:", ne)

print("#"*40, end="\n\n")
#################################

print("try-except-else")
print("-"*20)
# ------------


try:
    print("Reached try")
    my_file_handle = open("xyzsdsd.txt", "r")

    # To avoid below code executing 'except' block which is wrtting for file-opn
    # error, we are moving this to else block

    # content = my_file_handle.read()
    # my_file_handle.close()

except:
    print("Reached except block")
    print("HERE strictly we wrote logic to handle file open error")
else:
    print("Reached else")
    content = my_file_handle.read()
    my_file_handle.close()

# if 'try' success then execute 'else' block and skip 'except' block
#       which means, it is continuation of 'try' block
#       so, it is equal to keeping 'else' block code in 'try'
#
# if 'try' failed then 'else' block will not execute and 'except' will execute

print("#"*40, end="\n\n")
#################################

print("try-except-else-finally")
print("-" * 20)
# ------------


try:
    print("Reached try")
    my_file_handle = open("xyzsdsd.txt", "r")

except:
    print("Reached except block")
    print("HERE strictly we wrote logic to handle file open error")
else:
    print("Reached else")
    content = my_file_handle.read()
finally:
    print("Reached finally")
    try:
        my_file_handle.close()
        print("file handle closed")
    except:
        print("file handle not open to close")

# if 'try' success/failure, finally will execute
# if 'except' success/failure, finally will execute
# if 'else' success/failure, finally will execute

print("#" * 40, end="\n\n")
#################################

print("User defined exception class example-1")
print("-"*20)
# ------------

# About 'Exception' class : is super class for all exception classes

# Mandatory step: it should be subclass of 'Exception' or
#   if some classes are already subclass of 'Exception'
#   then we can create subclass of those classes as well
#
#   Ex: builtin exception classes


class MyError(Exception):
    pass
# Even though it is empty, it is valid exception class

try:
    a = 10
    if a == 10:
        raise MyError

        # We can use raise to raise any exception
        # raise ZeroDivisionError
        # raise NameError

    if a > 10:
        raise MyError

    if a < 10:
        raise MyError

except MyError:
    print("Reached except block: It is MyError")


print("#"*40, end="\n\n")
#################################

print("User defined exception class example-2")
print("-"*20)
# ------------


class MyError(Exception):
    def __init__(self, m):
        self.error_message = m

try:
    a = 10
    if a == 10:
        raise MyError("Here value of a is 10 so raising MyError")

    if a > 10:
        raise MyError("Here value of a is > 10 so raising MyError")

    if a < 10:
        raise MyError("Here value of a is < 10 so raising MyError")

except MyError as me:
    print("Reached except block: It is MyError and me is:", me.error_message)


print("#"*40, end="\n\n")
#################################
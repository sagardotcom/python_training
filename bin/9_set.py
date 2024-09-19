"""
set:
        -- We have option to store collection of values like list of names, list of email-ids etc
        -- Here, it will always keep UNIQUE values
        -- No index to each value
"""

print("set PART-1")
print("How to store values")
print("-"*20)
# ------------

my_fs_1 = {10, 10, 10, "python", "python"}
print(my_fs_1)

my_fs_2 = set([10, 10, 10, "python", "python"])
print(my_fs_2)

print("#"*40, end="\n\n")
#################################


print("set PART-2")
print("Methods inside 'set' class")
print("-"*20)
# ------------

print(dir(set))

print("#"*40, end="\n\n")
#################################
"""
Dictionary:
        -- We have option to store collection of values like list of names, list of email-ids etc
        -- Here, we can store DUPLICATE values
        -- We need to provide index for each value called KEY
"""

print("Dictionary PART-1")
print("How to store values")
print("-"*20)
# ------------

my_dictionary_1 = {0:"python", 1:10, 2:"online"}
# Internally it will create object of 'dict' class and store the values

# OR
my_dictionary_2 = dict({0:"python", 1:10, 2:"online"})

# FOR KEYS: We can use any IMMUTABLE VALUES like numbers, string, tuple
my_dictionary_3 = {"course": "python", "duration": 10, "mode": "online"}

# FOR VALUES: We can store any type of values in dictionary
my_dictionary_4 = {
    "course": "python",
    "duration": 10,
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)
print("my_dictionary_4:", my_dictionary_4)

print("#"*40, end="\n\n")
#################################


print("Dictionary PART-2")
print("Access each value using KEY")
print("-"*20)
# ------------

my_dictionary = {
    "course": "python",
    "duration": 10,
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n")

print("Course Name:", my_dictionary["course"]) # "python"
print("2nd character in Course Name:", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("2nd value in Mode:", my_dictionary["mode"][1]) # "offline"
print("4th character in 2nd value in Mode:", my_dictionary["mode"][1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Lname of the Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("last character of Lname of the Trainer:", my_dictionary["trainer"]["lname"][-1]) # "z"

print("#"*40, end="\n\n")
#################################

print("Dictionary PART-3")
print("Methods present inside 'dict' class")
print("-"*20)
# ------------

print(dir(dict))

print("#"*40, end="\n\n")
#################################

print("Dictionary PART-4")
print("Add/Update elements to dictionary")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

my_dictionary["location"] = "India"
# If key present then UPDATE key with value 'India'
# else add new key/value pair

print("my_dictionary after Add/Update:", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
#################################

print("Dictionary PART-5")
print("Add/Update elements to dictionary: Using update() method")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

another_dictionary = {"location": "India"}
my_dictionary.update(another_dictionary)
# Same as above block, It will be useful when we have to merge other dictionary

print("my_dictionary after Add/Update:", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
#################################

print("Dictionary PART-6")
print("Delete items")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

item_value = my_dictionary.pop("course")
print("my_dictionary after  pop('course'):", my_dictionary)
print("removed value:", item_value, end="\n\n")

item_value = my_dictionary.popitem()
print("my_dictionary after popitem():", my_dictionary)
print("removed value:", item_value, end="\n\n")

del my_dictionary["duration"]
print("my_dictionary after del 'duration':", my_dictionary)
# del is to remove any object, not belongs to only dictionary
# Example
# x = 10
# del x

print("#"*40, end="\n\n")
#################################

print("Dictionary PART-7")
print("Get course name")
print("-"*20)
# ------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Course Name:", my_dictionary["course"], end="\n\n") # ERROR if key not found
print("Course Name using get method:", my_dictionary.get("course"), end="\n\n") # None if key not found

print("#"*40, end="\n\n")
#################################
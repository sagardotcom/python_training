"""
Text File Operations: Reading & Writing to text file with
any extension .txt, .log, .mylog, .yourlog etc
"""

"""
We need to follow 3 steps
Step-1: Connect file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: Connect file
    - open()
Step-2: Read/Write
    - FOR WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readlines 3) readline (OR for-loop to read line by line)
Step-3: Disconnect
    - close()
"""

print("All write operations")
print("-"*20)
# ------------

# Step-1: Connect file
# ------------
# my_file_handle = open("provide file name or file path", "mode")
my_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only, It will create new file, IMPORTANT it will erase, existing content of the file
# mode 'r': Read Only, It will not create new file if file not present
# mode 'a': Append Only, It will create new file only if file not present

# mode 'w+': RW, It will create new file, IMPORTANT it will erase, existing content of the file
# mode 'r+': RW, It will not create new file if file not present
# mode 'a+': RW, It will create new file only if file not present
#       RW means, using same file handle we can call read & wright methods

# Step-2: Write
# ------------
# Our Data
x = 10
y = "Python"

# Convert other type of data to string
# because write() & writelines expect data in string
x = str(x)

# 1) write: We can write single value/string
my_file_handle.write(x+"\n")
my_file_handle.write(y+"\n")

# 2) writelines: We can any collection of values
my_data_in_list = [x+"\n", y+"\n"]
my_file_handle.writelines(my_data_in_list)

# 3) print-function
print(x, y, 20, "Java", sep="\n",file=my_file_handle)

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("""All file operations are completed
check my-out_file.txt
""")

print("#"*40, end="\n\n")
#################################

print("Reading file using 1) read()")
print("-"*20)
# ------------

# Step-1: Connect file
# ------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ------------
file_content = my_file_handle.read()
# read() will return entire file content in string
print("file_content:", file_content)
print("file_content in raw format:", repr(file_content))

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40, end="\n\n")
#################################

print("Reading file using 2) readlines()")
print("-"*20)
# ------------

# Step-1: Connect file
# ------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ------------
file_content = my_file_handle.readlines()
# readlines() will return entire file content in list
print("file_content:", file_content)

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40, end="\n\n")
#################################

print("Reading file using 3) readline()")
print("-"*20)
# ------------

# Step-1: Connect file
# ------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ------------
file_content = my_file_handle.readline()
# readline() will return one line
print("1st line:", file_content)

file_content = my_file_handle.readline()
# readline() will return one line
print("2nd line:", file_content)

file_content = my_file_handle.readline()
# readline() will return one line
print("3rd line:", file_content)

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40, end="\n\n")
#################################

print("Reading file using 4) read line by line using for-loop")
print("-"*20)
# ------------

# Step-1: Connect file
# ------------
my_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# ------------
for each_line in my_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# ------------
my_file_handle.close()

print("#"*40, end="\n\n")
#################################
"""
 Strings:
        -- We have option to store collection of characters like name, email-id etc
        -- Automatically index number will be assigned to each char
"""

print("Strings PART-1")
print("How to store values")
print("-"*20)
# ------------

a = 'WEL COME'
# Internally it will create object of 'str' class and store the values

# OR
b = str('WEL COME')

print(a, b)

print("#"*40, end="\n\n")
#################################

print("Strings PART-2")
print("How to store values")
print("-"*20)
# ------------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = """PERSON'S HEIGHT IS XYZ" ( " represents inches)"""
e = '''PERSON'S HEIGHT IS XYZ" ( " represents inches)'''

print(a, b, c, d, e, end="\n\n")

print(a, b, c, d, e, sep="\n")


print("#"*40, end="\n\n")
#################################

print("Strings PART-3")
print("How to store values")
print("-"*20)
# ------------

a = "C:\n newfolder\t test.py"
# Bydefault: few chars with \ will be special meaning ex: \n -> replaced with newlinfe

print("Value of 'a' = ", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r - > raw string,
print("Raw string 'b' = ", b, end="\n\n")

print("Converting a to raw string:", repr(a))

print("#"*40, end="\n\n")
#################################

"""
 Strings:
        -- We have option to store collection of characters like name, email-id etc
        -- Automatically index number will be assigned to each char
"""

print("Strings PART-1")
print("How to store values")
print("-"*20)
# ------------

a = 'WEL COME'
# Internally it will create object of 'str' class and store the values

# OR
b = str('WEL COME')

print(a, b)

print("#"*40, end="\n\n")
#################################


print("Strings PART-2")
print("How to store values")
print("-"*20)
# ------------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = """PERSON'S HEIGHT IS XYZ" ( " represents inches)"""
e = '''PERSON'S HEIGHT IS XYZ" ( " represents inches)'''

print(a, b, c, d, e, end="\n\n")

print(a, b, c, d, e, sep="\n")


print("#"*40, end="\n\n")
#################################

print("Strings PART-3")
print("How to store values")
print("-"*20)
# ------------

a = "C:\newfolder\test.py"
# Bydefault: few chars with \ will be special meaning ex: \n -> replaced with newlinfe

print("Value of 'a' = ", a, end="\n\n")

b = r"C:\newfolder\test.py"
# r - > raw string,
print("Raw string 'b' = ", b, end="\n\n")

print("Converting a to raw string:", repr(a))

print("#"*40, end="\n\n")
#################################

print("Strings PART-4")
print("How to store values")
print("-"*20)
# ------------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f - > format
# f -> it will replace {variable name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
#################################

print("Strings PART-5")
print("Indexes: Access each character using index number")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-1

print("0th character using +ve index number:", my_string[0])
print("0th character using -ve index number:", my_string[-8])

# print("100th character using +ve index number:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
#################################

print("Strings PART-6")
print("Slicing: Pull substring")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-2

print("substring from index-1 to index-6 using +ve index number:", my_string[1:6])
print("substring from index-1 to index-6 using -ve index number:", my_string[-7:-2], end="\n\n")
# Default behavior, character at last index will not come

print("substring from index-1 to END using +ve index number:", my_string[1:])
print("substring from index-1 to END using -ve index number:", my_string[-7:], end="\n\n")

print("substring from BEGINNING to index-6 using +ve index number:", my_string[:6])
print("substring from BEGINNING to index-6 using -ve index number:", my_string[:-2], end="\n\n")


print("#"*40, end="\n\n")
#################################

print("Strings PART-7")
print("Step Value: We can skip values")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-3

print("substring from index-1 to index-6 using +ve index number:", my_string[1:6:2])
print("substring from index-1 to index-6 using -ve index number:", my_string[-7:-2:2], end="\n\n")


print("#"*40, end="\n\n")
#################################

print("Strings PART-8")
print("-ve Step Value: We can traverse in reverse direction")
print("-" * 20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx Section-4

# Steps
# Example: index- 6 to 1 in reverse direction
# start index should be : 6
# end index should be: 1
# step value should be -ve value

print("sub string from index 6 to 1 using +ve index number:step by -1", my_string[6:1:-1])
print("sub string from index 6 to 1 using -ve index number:step by -1", my_string[-2:-7:-1], end="\n\n")

print("sub string from index 6 to 1 using +ve index number:step by -2", my_string[6:1:-2])
print("sub string from index 6 to 1 using -ve index number:step by -2", my_string[-2:-7:-2], end="\n\n")

print("#" * 40, end="\n\n")
#################################

print("Strings PART-9")
print("Methods/Variables present inside 'str' class")
print("-"*20)
# ------------

# my_string = "WEL COME"
# print(dir(my_string))

# OR

print(dir(str))

print("#"*40, end="\n\n")
#################################

print("Strings PART-10")
print("Special Names which is starting with __ & ends with __")
print("-"*20)
# ------------

s1 = "Hello"
s2 = "python"
concat_result = s1 + s2 # internally + mapped-to/calls __add__ defined inside str class
length_of_s1 = len(s1) # Internally len() function calls __len__ defined inside str class

print("concat_result:", concat_result)
print("length_of_s1:", length_of_s1)

print("#"*40, end="\n\n")
#################################

print("Strings PART-11")
print("'startswith()' method")
print("-"*20)
# ------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

startswith_result = my_string.startswith("WEL") # True/False
print("startswith_result:", startswith_result)

print("#"*40, end="\n\n")
#################################


"""
Write 2nd to produce output in list of tuples.

Expected Output:
-----
[ (ip, dt, img, url), (ip, dt, img, url), (ip, dt, img, url),]
-----
"""

print("input data:")
print("-"*20)
# ------------

input_data = """
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print(input_data)

print("#"*40, end="\n\n")
#################################

print("type of input data:")
print("-"*20)
# ------------

print(type(input_data))

print("#"*40, end="\n\n")
#################################

print("input data in RAW FORMAT:")
print("-"*20)
# ------------

print(repr(input_data))

print("#"*40, end="\n\n")
#################################

print("Making list of lines")
print("-"*20)
# ------------

# list_of_lines = input_data.split("\n")
list_of_lines = input_data.splitlines()
print(list_of_lines)

print("#"*40, end="\n\n")
#################################

print("print each line")
print("-"*20)
# ------------

for each_line in list_of_lines:
    print("Each Line:", each_line)

print("#"*40, end="\n\n")
#################################

print("print only IP address line")
print("-"*20)
# ------------

for each_line in list_of_lines:
    if each_line.startswith("123"):
        print("Each Line:", each_line)

print("#"*40, end="\n\n")
#################################

print("Extract Info")
print("-"*20)
# ------------
extracted_info = []
for each_line in list_of_lines:
    if each_line.startswith("123"):

        sp = each_line.split()

        ip = sp[0]

        raw_date = sp[3]
        index_of_colon = raw_date.index(":")
        dt = raw_date[1:index_of_colon]

        raw_img = sp[6]
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"

        raw_url = sp[10]
        url = raw_url[1:-1]

        each_line_tuple = (ip, dt, img, url)
        extracted_info.append(each_line_tuple)

print(extracted_info)

print("#"*40, end="\n\n")
#################################


print("Write to log_report_1.json")
print("-"*20)
# ------------

my_json_file_handle = open("log_report_1.json", "w")

import json
json.dump(extracted_info, my_json_file_handle)

my_json_file_handle.close()

print("""
Created log_report_1.json file,please check
""")

print("#"*40, end="\n\n")
#################################


print("Read from log_report_1.json")
print("-"*20)
# ------------

my_json_file_handle = open("log_report_1.json", "r")

import json
data_from_json = json.load(my_json_file_handle)

my_json_file_handle.close()

print(data_from_json)

print("#"*40, end="\n\n")
#################################


"""
Write 2nd to produce output in Dictionary.

Expected Output:
-----
{
0: (ip, dt, img, url),
1: (ip, dt, img, url),
2: (ip, dt, img, url),
3: (ip, dt, img, url),
4: (ip, dt, img, url),
5: (ip, dt, img, url),
}
-----
"""

print("input data:")
print("-"*20)
# ------------

input_data = """
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print(input_data)

print("#"*40, end="\n\n")
#################################

print("type of input data:")
print("-"*20)
# ------------

print(type(input_data))

print("#"*40, end="\n\n")
#################################

print("input data in RAW FORMAT:")
print("-"*20)
# ------------

print(repr(input_data))

print("#"*40, end="\n\n")
#################################

print("Making list of lines")
print("-"*20)
# ------------

# list_of_lines = input_data.split("\n")
list_of_lines = input_data.splitlines()
print(list_of_lines)

print("#"*40, end="\n\n")
#################################

print("print each line")
print("-"*20)
# ------------

for each_line in list_of_lines:
    print("Each Line:", each_line)

print("#"*40, end="\n\n")
#################################

print("print only IP address line")
print("-"*20)
# ------------

for each_line in list_of_lines:
    if each_line.startswith("123"):
        print("Each Line:", each_line)

print("#"*40, end="\n\n")
#################################

print("Extract Info")
print("-"*20)
# ------------
extracted_info = {}
index_no = 0
for each_line in list_of_lines:
    if each_line.startswith("123"):

        sp = each_line.split()

        ip = sp[0]

        raw_date = sp[3]
        index_of_colon = raw_date.index(":")
        dt = raw_date[1:index_of_colon]

        raw_img = sp[6]
        if raw_img.startswith("/pics/"):
            img = raw_img[6:]
        else:
            img = "No Image"

        raw_url = sp[10]
        url = raw_url[1:-1]

        each_line_tuple = (ip, dt, img, url)
        extracted_info[index_no] = each_line_tuple
        index_no = index_no + 1

print(extracted_info)

print("#"*40, end="\n\n")
#################################


print("Write to log_report_2.json")
print("-"*20)
# ------------

my_json_file_handle = open("log_report_2.json", "w")

import json
json.dump(extracted_info, my_json_file_handle)

my_json_file_handle.close()

print("""
Created log_report_2.json file,please check
""")

print("#"*40, end="\n\n")
#################################


print("Read from log_report_2.json")
print("-"*20)
# ------------

my_json_file_handle = open("log_report_2.json", "r")

import json
data_from_json = json.load(my_json_file_handle)

my_json_file_handle.close()

print(data_from_json)

print("#"*40, end="\n\n")
#################################
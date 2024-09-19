"""
Get data from web_server.log
then
extract
IP
PICS
"""

print("Get data from web_server.log")
print("-"*20)
# ------------

my_log_file_handle = open("../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
#################################

print("Just print whether it is IP address line or not")
print("-"*20)
# ------------

import re

for each_line in log_file_content:
    match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT
r"""
IDENTIFIERS
---------------
\d -> represents ANY ONE digits b/n 0 to 9
\D -> represents ANY ONE non-digits. Except 0 to 9, any character
. -> represent any ONE ANY character
\. -> strictly DOT
[0-9] -> represents ANY ONE digits b/n 0 to 9
---------------

QUANTIFIERS
---------------
\d{3} -> it makes \d\d\d
[0-9]{3} -> It makes [0-9][0-9][0-9]
---------------

MODIFIERS
---------------
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 time
---------------
"""

print("#"*40, end="\n\n")
#################################

print("Extract IP")
print("-"*20)
# ------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print(ip)

# COMMENT
r"""
put () to IP address pattern to capture
- this is called GROUP
- Each group has index starting from 1

"""

print("#"*40, end="\n\n")
#################################


print("Extract IP, PICS: PARTIAL OUTPUT-1")
print("-"*20)
# ------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\w+\.(jpg|gif)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        img = match_result.group(2)
        print(ip, img)

# COMMENT
r"""

[0-9A-Za-z_]
OR
shortcut \w

\W is excluding these characters [0-9A-Za-z_]
"""

print("#"*40, end="\n\n")
#################################

print("Extract IP, PICS: PARTIAL OUTPUT-2")
print("Provided MORE INFORMATION/Landmark ")
print("-"*20)
# ------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST)\s+/pics/(\w+\.(gif|jpg)).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        img = match_result.group(3)
        print(ip, img)

# COMMENT
r"""
\s -> ONE Space
\s+ -> ONE or more Space
\S -> except space, any character
"""

print("#"*40, end="\n\n")
#################################

print("Extract IP, PICS: FINAL OUTPUT")
print("-"*20)
# ------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST)\s+/(pics/(\w+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        img = match_result.group(4)
        if img is None:
            img = "No Image"
        print(ip, img)

# COMMENT
r"""

Make this portion 'pics/wpaper.gif' optional
so that lines which is not having IP address also considered

So, 
(pics/(\w+\.(gif|jpg)))?
"""

print("#"*40, end="\n\n")
#################################
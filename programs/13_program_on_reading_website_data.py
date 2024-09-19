"""
Get data from website and print
"""

print("Get data from website and print")
print("-"*20)
# ------------

import urllib.request as u
my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
#################################

print("type of website data")
print("-"*20)
# ------------

print(type(web_content))

print("#"*40, end="\n\n")
#################################

print("Methods present inside 'bytes' class")
print("-"*20)
# ------------

print(dir(web_content))

print("#"*40, end="\n\n")
#################################

print("web_content in string")
print("-"*20)
# ------------

web_content = web_content.decode() # convert to string
print(web_content)

print("#"*40, end="\n\n")
#################################
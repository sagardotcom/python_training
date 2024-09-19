"""
Webscraping using Beautifulsoup4 library
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

print("Create object of beautifulsoup class")
print("-"*20)
# ------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#"*40, end="\n\n")
#################################

print("Head Tag")
print("-"*20)
# ------------

print(soup.head)

print("#"*40, end="\n\n")
#################################


print("body Tag")
print("-"*20)
# ------------

print(soup.body)

print("#"*40, end="\n\n")
#################################

print("Title Tag")
print("-"*20)
# ------------

print(soup.head.title)

print("#"*40, end="\n\n")
#################################

print("Title Tag Text")
print("-"*20)
# ------------

print(soup.head.title.text)

print("#"*40, end="\n\n")
#################################

print("1st link tag")
print("-"*20)
# ------------

print(soup.head.link)

print("#"*40, end="\n\n")
#################################

print("1st link tag Attributes")
print("-"*20)
# ------------

print("Tag:", soup.head.link)
print("REL:", soup.head.link.get('rel'))
print("HREF:", soup.head.link.get('href'))
print("TYPE:", soup.head.link.get('type'))

print("#"*40, end="\n\n")
#################################

print("log data")
print("-"*20)
# ------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
#################################

print("type of log data")
print("-"*20)
# ------------

print(type(log_data))

print("#"*40, end="\n\n")
#################################


print("log data in RAW FORMAT")
print("-"*20)
# ------------

print(repr(log_data))

print("#"*40, end="\n\n")
#################################

print("log data in list")
print("-"*20)
# ------------

log_data = log_data.splitlines()
print(log_data)

print("#"*40, end="\n\n")
#################################

print("Extract Info and write to file ")
print("-"*20)
# ------------

my_file_handle = open("web_scrap_report.txt", "w")
print("IP", "DATE", "PICS", "URL", sep="\t\t", file=my_file_handle)

for each_line in log_data:
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

        print(ip, dt, img, url, sep="\t\t", file=my_file_handle)

my_file_handle.close()

print("""
web_scrap_report.txt created, please check
""")

print("#"*40, end="\n\n")
#################################
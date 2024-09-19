"""
Get data from web_server.log

then

extract
IP
DATE
PICS
URL

then

write extracted data to txt_to_json.json file
"""

print("Get data from web_server.log")
print("-"*20)
# ------------

my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
#################################

print("Extract Info")
print("-"*20)
# ------------
extracted_info = {}
index_no = 0
for each_line in log_file_content:
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

print("Write to log_report_4.json")
print("-"*20)
# ------------

my_json_file_handle = open("log_report_4.json", "w")

import json
json.dump(extracted_info, my_json_file_handle)

my_json_file_handle.close()

print("""
Created log_report_4.json file,please check
""")

print("#"*40, end="\n\n")
#################################
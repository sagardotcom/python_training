"""
Get data from log_report_4.json

then

write to text file json_to_txt.txt
"""
print("Get data from log_report_4.json")
print("-"*20)
# ------------

my_json_file_handle = open("log_report_4.json", "r")

import json
json_file_content = json.load(my_json_file_handle)

my_json_file_handle.close()

print("json_file_content:", json_file_content, sep="\n", end="\n\n")

print("type of json_file_content:", type(json_file_content), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#################################

print("Write to log_report_5.txt")
print("-"*20)
# ------------

# json_file_content = {0:[ip,dt,img,url], 1:[ip,dt,img,url], 2:[ip,dt,img,url],}

my_txt_file_handle = open("log_report_5.txt", "w")
print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)

# json_file_content.values() = [[ip,dt,img,url], [ip,dt,img,url], [ip,dt,img,url]]
for i, j, k, l in json_file_content.values():
    print(i, j, k, l, sep="\t", file=my_txt_file_handle)

my_txt_file_handle.close()

print("""
log_report_5.txt created, Please check
""")

print("#"*40, end="\n\n")
#################################
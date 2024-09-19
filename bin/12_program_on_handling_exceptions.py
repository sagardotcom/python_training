"""
Rewrite 8th program to handle exceptions
"""

print("Get data from log_report_4.json")
print("-"*20)
# ------------
try:
    my_json_file_handle = open("log_report_4.json", "r")
except FileNotFoundError:
    print("Not able to open 'log_report_4.json', Please check and rerun")
    print("Exiting..")
    exit()
else:
    try:
        import json
    except ModuleNotFoundError:
        print("Not able to import json")
        print("Exiting..")
        exit()
    else:
        json_file_content = json.load(my_json_file_handle)
    finally:
        my_json_file_handle.close()


print("json_file_content:", json_file_content, sep="\n", end="\n\n")
print("type of json_file_content:", type(json_file_content), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#################################


print("Write to log_report_5.txt")
print("-"*20)
# ------------

try:
    my_txt_file_handle = open("log_report_5.txt", "w")
    print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)
    for i, j, k, l in json_file_content.values():
        print(i, j, k, l, sep="\t", file=my_txt_file_handle)
    my_txt_file_handle.close()
    print("log_report_5.txt created, Please check")
except Exception as e:
    print("Got error while writing log_report_5.txt")
    print("Error message is:", e)
    print("Exiting..")
    exit()

print("#"*40, end="\n\n")
#################################
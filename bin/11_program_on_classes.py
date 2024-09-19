"""
Write a class 'LogProcessClass' which has below functionalities

Example:
    L1 = LogProcessClass("../log/web_server.log")
    ips_list = L1.get_ips() # [ip, ip, ip]
    all_list = L1.get_all() # [(1p, dt, img, url), (1p, dt, img, url),]
    L1.to_json("log_report_6.json") # It should create json file
"""

"""
Write a class 'LogProcessClass' which has below functionalities

Example:
    L1 = LogProcessClass("../log/web_server.log")
    ips_list = L1.get_ips() # [ip, ip, ip]
    all_list = L1.get_all() # [(1p, dt, img, url), (1p, dt, img, url),]
    L1.to_json("log_report_6.json") # It should create json file
"""
print("LogProcessClass:")
print("-"*20)
# ------------


class LogProcessClass:
    def __init__(self, log_file_path):
        my_log_file_handle = open(log_file_path, "r")
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()

    def get_ips(self):
        extracted_info = []
        for each_line in self.log_file_content:
            if each_line.startswith("123"):
                sp = each_line.split()
                ip = sp[0]
                extracted_info.append(ip)
        return extracted_info

    def get_all(self):
        extracted_info = []
        for each_line in self.log_file_content:
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
        return extracted_info

    def to_json(self, out_file_path):
        # Get all records
        all_records = self.get_all()

        # Writ to json file
        my_json_file_handle = open(out_file_path, "w")
        import json
        json.dump(all_records, my_json_file_handle)
        my_json_file_handle.close()


print("#"*40, end="\n\n")
#################################

print("Using Class")
print("-"*20)
# ------------

L1 = LogProcessClass("../log/web_server.log")
ips_list = L1.get_ips()  # [ip, ip, ip]
all_list = L1.get_all()  # [(1p, dt, img, url), (1p, dt, img, url),]
L1.to_json("log_report_6.json")

print("ips_list:", ips_list, sep="\n", end="\n\n")
print("all_list:", all_list, sep="\n", end="\n\n")
print("log_report_6.json created, Please check ")

print("#"*40, end="\n\n")
#################################
"""
Write a function
that should one argument i.e log file path,
that function should read log file, extract info
then it should keep extracted information in dictionary
then it should return dictionary
"""

print("Function to process lof file")
print("-"*20)
# ------------

def log_process_function(*, log_file_path):
    """
    read log file, extract info
    :param log_file_path:
    :return dictionary:
    """

    my_log_file_handle = open(log_file_path, "r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()

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
    return extracted_info


print("#"*40, end="\n\n")
#################################

print("Accessing function to process files")
print("-"*20)
# ------------

func_result = log_process_function(log_file_path=r"../log/web_server.log")
print("func_result:", func_result, end="\n\n")

print("#"*40, end="\n\n")
#################################
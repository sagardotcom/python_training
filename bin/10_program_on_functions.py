"""
Write 9th program function to receive multiple log files
like if we call
log_process_func('log1.log', 'log2.log')

that function should return list of dictionaries like
[dictionary1, dictionary2, dictionary3, ]
"""

print("Function to process log file")
print("-"*20)
# ------------

def main_log_process_function(*log_file_paths):
    extracted_info = []
    for each_log_file_path in log_file_paths:
        each_file_extract_data = _log_process_function(log_file_path=each_log_file_path)
        extracted_info.append(each_file_extract_data)
    return extracted_info

def _log_process_function(*, log_file_path):
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

print("Calling log process function")
print("-"*20)
# ------------

func_result = main_log_process_function("../log/web_server.log", "../log/web_server.log", "../log/web_server.log")
print("func_result:", func_result, sep="\n", end="\n\n")
print("#"*40, end="\n\n")
#################################
def find_error_in_log(log_file):
    all_lines = open(log_file,'r').readlines()
    err_lines = []

    for line in all_lines:
        if "ERROR" in line:
            err_lines.append(line)
    return err_lines

# print(
#     find_error_in_log("sample.log")
# )




# generator 
def read_log_lines(log_file):
    with open(log_file, 'r') as f:
        for lines in f:
            yield lines

error_count = 0

for log_line in read_log_lines("sample.log"):
    if "ERROR"in log_line:
        error_count +=1
print(f"Found {error_count} error lines.")




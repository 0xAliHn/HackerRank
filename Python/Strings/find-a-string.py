def count_substring(string, sub_string):
    # Using generate expressions
    # 1 is for incrementing count by 1 each time
    # if for checking and matching sub string
    return sum((1 for i in range(len(string)) if string[i:len(sub_string)+i] == sub_string))

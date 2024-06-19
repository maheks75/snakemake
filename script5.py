import sys
import os
print('script5 start')
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Remove leading and trailing whitespace, and split into a list of strings
        string_list = [line.strip() for line in lines if isinstance(line, str)]
    return string_list

# Read and process the text files
file1_strings_5g = read_text_file(sys.argv[1])
file2_strings_4g = read_text_file(sys.argv[2])

# Check if file2_strings_4g is empty
if not file2_strings_4g:
    print(f"{sys.argv[2]} is empty. Creating an empty output file.")
    with open(sys.argv[3], 'w'):
        pass
else:
    # Find the common strings
    common_strings = set(file1_strings_5g).intersection(file2_strings_4g)
    unique_string = []
    # Print the common strings
    for string in file2_strings_4g:
        if isinstance(string, str) and string not in common_strings:
            #print(string)
            unique_string.append(string)
    with open(sys.argv[3], 'w') as file:
        for strg in unique_string:
            file.write(strg+'\n')
print('script5 finish')

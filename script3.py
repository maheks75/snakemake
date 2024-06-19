import sys
filename_5G = sys.argv[1]
filename_4G = sys.argv[2]
repeating_filename_5G = sys.argv[3]
repeating_filename_4G = sys.argv[4]
print('script3 start')
# Read the strings from the file
with open(filename_5G, 'r') as file_5G:
    strings_5G = [line.strip() for line in file_5G]

string_count_5G = {}
for string_5G in strings_5G:
    if string_5G in string_count_5G:
        string_count_5G[string_5G] += 1
    else:
        string_count_5G[string_5G] = 1

repeating_strings_count_5G = 0
non_repeating_strings_count_5G = 0



repeating_strings_5G = []
non_repeating_strings_5G = []

# Separate repeating and non-repeating strings
for string_5G, count_5G in string_count_5G.items():
    if count_5G > 1:
        repeating_strings_5G.append((string_5G, count_5G))
        repeating_strings_count_5G += count_5G
repeating_strings_5G.sort(key=lambda x: x[1], reverse=True)


# Write repeating strings to file with count
with open(repeating_filename_5G, 'w') as file_5G:
    for string_5G, count_5G in repeating_strings_5G:
        file_5G.write(f"{string_5G}: {count_5G}\n")
with open(filename_4G, 'r') as file:
    strings_4G = [line.strip() for line in file]

string_count_4G = {}
for string_4G in strings_4G:
    if string_4G in string_count_4G:
        string_count_4G[string_4G] += 1
    else:
        string_count_4G[string_4G] = 1

repeating_strings_count_4G = 0
non_repeating_strings_count_4G = 0



repeating_strings_4G = []
non_repeating_strings_4G = []

# Separate repeating and non-repeating strings
for string_4G, count_4G in string_count_4G.items():
    if count_4G > 1:
        repeating_strings_4G.append((string_4G, count_4G))
        repeating_strings_count_4G += count_4G
repeating_strings_4G.sort(key=lambda x: x[1], reverse=True)


# Write repeating strings to file with count
with open(repeating_filename_4G, 'w') as file:
    for string_4G, count_4G in repeating_strings_4G:
        file.write(f"{string_4G}: {count_4G}\n") 
print('script3 finish')

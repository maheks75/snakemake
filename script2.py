from Bio import SeqIO
import sys
input_5g_txt_file = sys.argv[1]
input_4g_txt_file = sys.argv[2]
target_sequence_4g = 'GGGG'
target_sequence_5g = 'GGGGG'
output_file_5G = sys.argv[3]
output_file_4G = sys.argv[4]

sequences_written = 0
print('script2 starts')
with open(input_5g_txt_file, "r") as file, open(output_file_5G, 'w') as output_handle:
    strings = [line.strip() for line in file]
    for string in strings:
        if target_sequence_5g in string[:18]:
            extracted_sequence = string[:12]
            output_handle.write(extracted_sequence + "\n")
            sequences_written += 1
            #print("Extracted Sequence:", extracted_sequence)

with open(input_4g_txt_file, "r") as file, open(output_file_4G, 'w') as output_handle:
    strings = [line.strip() for line in file]
    for string in strings:
        if target_sequence_4g in string[:18]:
            extracted_sequence = string[:12]
            output_handle.write(extracted_sequence + "\n")
            sequences_written += 1
print('script2 finsih')
       

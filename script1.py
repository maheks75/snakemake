from Bio import SeqIO
#import random
import sys
input_fastq_file = sys.argv[1]
output_file_5g_with_g = sys.argv[2]
output_file_4g_with_g = sys.argv[3]
with open(output_file_5g_with_g, 'w') as output_handle_with_5g:
    for i, record in enumerate(SeqIO.parse(input_fastq_file, "fastq")):
        sequence_data = str(record.seq)[:25]
        #print(sequence_data)

        if 'GGGGG' in sequence_data:
            output_handle_with_5g.write(f"{sequence_data}\n")
with open(output_file_4g_with_g, 'w') as output_handle_with_4g:
    for i, record in enumerate(SeqIO.parse(input_fastq_file, "fastq")):
        sequence_data = str(record.seq)[:25]
        #print(sequence_data)

        if 'GGGG' in sequence_data:
            output_handle_with_4g.write(f"{sequence_data}\n")

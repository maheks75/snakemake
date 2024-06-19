from Bio import SeqIO
import sys
input_fastq_file_5g = sys.argv[1]
input_fastq_file_4g = sys.argv[2]
output_file_full = sys.argv[3]
sequence_list_file = sys.argv[4]

sequence_full_list = []
sequence_list_only = []
print('script8 start')
with open(output_file_full, 'w') as file:
    for i, record in enumerate(SeqIO.parse(input_fastq_file_5g, "fasta")):
        header_parts = record.description.split(":")
        header = f"> {header_parts[0].strip()}"
        sequence_data_5g = str(record.seq)
        #print(sequence_data_5g)
        sequence_full_list.append(f"{header}\n{sequence_data_5g}")
        sequence_list_only.append(header_parts[1].strip())

    for i, record in enumerate(SeqIO.parse(input_fastq_file_4g, "fasta")):
        header_parts = record.description.split(":")
        header = f"> {header_parts[0].strip()}"
        sequence_data_4g = str(record.seq)
        #print(sequence_data_4g)
        sequence_full_list.append(f"{header}\n{sequence_data_4g}")
        sequence_list_only.append(header_parts[1].strip())

    for seq_full in sequence_full_list:
        file.write(seq_full + '\n')

# Save the sequence_list_only to a file
with open(sequence_list_file, 'w') as seq_file:
    for seq_part in sequence_list_only:
        seq_file.write(seq_part + '\n')
print('script8 finish')


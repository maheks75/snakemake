#SCRIPT TO FIND PERCENTAGE according to last occurence of 5 gs
from Bio import SeqIO
from multiprocessing import Pool, Manager
import sys
# Function to process a single string
def process_string(string, seq_number):
    sequences = []
    
    # Open the output file within the process_string function
    with open(sys.argv[3], "a") as outfile:
        for record in SeqIO.parse(input_fastq_file, "fastq"):
            sequence = str(record.seq)
            if string in sequence[:12]:
                sequences.append(sequence)        
        if sequences:
            consensus_sequence = calculate_consensus(sequences)
            percentage_low_mismatch = calculate_percentage_low_mismatch(sequences, consensus_sequence) 
            sequence_header = f">Seq{seq_number.value}"  # Access the shared seq_number using .value
            outfile.write(f"> {len(sequences)} : {string} : {percentage_low_mismatch}\n{consensus_sequence}\n")
            seq_number.value += 1

def calculate_consensus(sequences):
    length_counts = {}
    
    seq_list2 = []
    #print(sequences)
    for seq in sequences:
        seq_length = len(seq)
        if seq_length in length_counts:
            length_counts[seq_length] += 1
        else:
            length_counts[seq_length] = 1
    most_common_length = max(length_counts, key=length_counts.get)
    #print(most_common_length)
    for seq in sequences:
        if len(seq) == most_common_length:
            consensus_sequence = ""
            last_index = seq[:25].rfind("GGGGG")
            if last_index != -1:
                start_index = last_index + 5
                #print(start_index)
                seq_list2.append(seq[start_index:most_common_length])
    #print(len(sequences))
    for sl in seq_list2:
        consensus_sequence = ""
        BASES_CALCULATE = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0}
        bases = ["A", "C", "G", "T", "N"]
        for k in range(len(sl)):
            for base in bases:
                BASES_CALCULATE[base] = 0
            for j in range(len(seq_list2)):
                if len(seq_list2[j]) > k:
                    base = seq_list2[j][k]
                    BASES_CALCULATE[base] += 1
            most_common_base = max(BASES_CALCULATE, key=BASES_CALCULATE.get)
            consensus_sequence += most_common_base 
    #print(consensus_sequence)    
    return consensus_sequence

def calculate_percentage_low_mismatch(sequences, consensus_sequence):
    length_counts = {}
    seq_list = []
    mismatch_threshold = 10
    total_sequences = 0
    low_mismatch_count = 0  
    #print(sequences)
    for seq in sequences:
        seq_length = len(seq)
        if seq_length in length_counts:
            length_counts[seq_length] += 1
        else:
            length_counts[seq_length] = 1
    most_common_length = max(length_counts, key=length_counts.get)
    #print(most_common_length)
   # print(len(consensus_sequence))
    for seq in sequences:
        seq_length = len(seq)
        if seq_length == most_common_length:
            last_index = seq[:25].rfind("GGGGG")
            if last_index != -1:
                start_index = last_index + 5
                #print(start_index)
                seq_list.append(seq[start_index:most_common_length])
    #print(len(consensus_sequence))
    #print(len(seq_list))
    for se in seq_list:
        mismatch_count = 0
        if len(se) == len(consensus_sequence):
            for k in range(len(se)):
                if se[k] != consensus_sequence[k]:
                    mismatch_count += 1
        #print(mismatch_count)
        if mismatch_count <= mismatch_threshold:
            low_mismatch_count += 1
    #print(count)       
    #print(low_mismatch_count)
    #print(len(seq_list))
    percentage_low_mismatch = (low_mismatch_count / len(seq_list)) * 100 if len(seq_list) > 0 else 0
    #print(percentage_low_mismatch)
    return percentage_low_mismatch

if __name__ == "__main__":
    input_fastq_file = sys.argv[1]
    
    with open(sys.argv[2], 'r') as file:
        strings = [line.strip() for line in file]
    
    # Number of CPU cores to use for multiprocessing
    num_cores = 48  # You can adjust this based on your machine's capabilities
    
    # Check if the list of strings is empty
    if not strings:
        print("No strings found in the input file. Creating an empty output file.")
        with open(sys.argv[3], 'w') as outfile:
            pass
    else:
        with Manager() as manager:
            seq_number = manager.Value('k', 1)  # Create a shared integer variable
            
            with Pool(processes=num_cores) as pool:
                pool.starmap(process_string, [(string, seq_number) for string in strings])
    
    # Additional check at the end to create an empty output file if needed
    if not os.path.isfile(sys.argv[3]):
        print("Output file not created. Creating an empty output file.")
        with open(sys.argv[3], 'w') as outfile:
            pass
